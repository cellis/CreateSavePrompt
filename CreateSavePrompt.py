import sublime, sublime_plugin
import os, shutil
import threading, time

class CreateSavePromptCommand(sublime_plugin.TextCommand):
  def onFileEntered(self, location):
    if os.path.isdir(location):
      sublime.error_message("CreateSavePrompt doesnt save directories. Yet.")
    else:
      if os.path.lexists(location):
        overwrite = sublime.ok_cancel_dialog("Destination exists. Overwrite?", "Overwrite")
        if overwrite:
          from .send2trash import send2trash
          send2trash(location)
        else:
          return

      with open(location, 'w', encoding='utf8') as f:
        f.write(self.view.substr(sublime.Region(0, self.view.size())))

      self.view.set_scratch(True)
      self.view.window().run_command('close')
      self.window().open_file(location)

      self.window().run_command('hide_panel')


  def run(self, edit):
    if self.view.file_name():
      # file exists, simply save it
      self.view.run_command("save")
    else:
      self.s = sublime.load_settings("CreateSavePrompt.sublime-settings")

      use_first_line_as_file = self.s.get("use_first_line_as_file")

      folders = sublime.active_window().folders()
      if len(folders) == 0:
        home_dir = self.s.get("home_dir")
        if not home_dir:
          home_dir = "/"
      else:
        home_dir = folders[0]

      if use_first_line_as_file:
        home_dir = os.path.join(home_dir, self.view.substr(self.view.line(0)))

      self.window().show_input_panel("File Location:", home_dir, self.onFileEntered, None, None)

  def window(self):
    return sublime.active_window()
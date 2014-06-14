import sublime, sublime_plugin
import os, shutil
import threading, time


class SavePromptCommand(sublime_plugin.TextCommand):
  def onFileEntered(self, name):
    print("name is %s" % name)


  def run(self, edit):
    # self.window().run_command('hide_panel')
    self.window().show_input_panel("File Location:", "cameron", self.onFileEntered, None, None)

  def window(self):
    return sublime.active_window()
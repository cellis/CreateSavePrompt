## Sublime Create Save Prompt (ST3 tested)

## Why?

I was tired of trying to create new files with `CMD+N` and not being able to save them to arbitrary locations using `CMD+S` without using mac's awful save file experience. This plugin fixes that.

## Installation

Working on getting this accepted into the package manager. For now, clone this into your `/Users/<yourusername>/Library/Application Support/Sublime Text 3/Packages/` directory (or wherever you have ST installed).

Once it's accepted into the repo, you should be able to install it by opening the package manager and typing `CreateSavePrompt`.

## IMPORTANT notes!

* Tested only on OSX. should work on linux.
* This will attempt to override your `CMD+S` command! If you don't want this to happen, you can map the `create_save_prompt` command to a new key in your keybindings (user) file, like this.

```
  {
    "keys": ["super+e"],
    "command": "create_save_prompt"
  }
```
Remember to remap the save key too:

```
{
  "keys": ["super+s"],
  "command": "save"
}
```

* Should work on ST2, haven't tested yet.
* May/probably won't work on windows (python pathing...). Send me a pull req if you want it to.
* If you have the `subl` symlink setup like me, and want to open a ST window from the terminal,then press `CMD+N` and then save the file with `CMD+S`, you'll need to create a `CreateSavePrompt.sublime-settings` file somewhere in the ST directory lookup chain and add your `home_dir` directory to it so CreateSavePrompt knows which default directory to start out in. If you're in a project, the default directory is the first folder in the project (the first root).
* If you create a new file with `CMD+N` and type something on the first line, that will be the suggested name of the file.
* Doesn't support uncreated directories or creating directories.


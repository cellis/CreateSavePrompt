## Sublime Create Save Prompt (ST3 tested)

## Why?

I was tired of trying to create new files with `CMD+N` and not being able to save them to arbitrary locations using `CMD+S` without using mac's awful save file experience. This plugin fixes that.

## Installation

If you have the package manager installed, simply open it and install the `Create Save Prompt` package.

Otherwise, clone this into your `/Users/<yourusername>/Library/Application Support/Sublime Text 3/Packages/` directory (or wherever you have ST installed).


## IMPORTANT notes!

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

* If you create a new file with `CMD+N` and type something on the first line, that will be the suggested name of the file.
* Doesn't support uncreated directories or creating directories.


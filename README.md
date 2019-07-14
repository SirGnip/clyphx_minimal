# ClyphX Minimal examples

These scripts serve as a demonstration of how to create ClyphX custom user action scripts.
They don't do anything useful, but simply serve as a starting point.

This approach to writing custom user action scripts for ClyphX had a number of goals:

- Minimized the edits necessary to `MIDI Remote Scripts/ClyphX/ClyphXUserActions.py` to get custom user actions installed.
- Minimize the amount of clutter added to the `MIDI Remote Scripts/ClyphX` directory by having each set of custom commands be in its own directory.
- Each directory can be committed to git so a simple `git checkout` can be used to get the files in the `MIDI Remote Scripts/ClyphX` directory.

### `minimal.py`

This script shows a custom user action implemented with a simple function.  

### `minimal_with_obj.py`

This script shows a custom user action implemented with a class.  This allows the commands to store data
between each call. 


# How to install

- Have [ClyphX](http://forum.nativekontrol.com/thread/992/current-version-clyphx-live-9) installed and working in Ableton Live
- Do a `git checkout` of this repo in the folder where you installed the ClyphX scripts
(usually something like C:\ProgramData\Ableton\Live 10 Intro\Resources\MIDI Remote Scripts\ClyphX)
- Edit `MIDI Resource Scrits\ClyphX\ClyphXUserActions.py` and add the following lines to the bottom of the `__init__` method:


        import clyphx_minimal.minimal
        clyphx_minimal.minimal.register(self)
        import clyphx_minimal.minimal_with_obj
        clyphx_minimal.minimal_with_obj.register(self)
         

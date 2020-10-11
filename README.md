# xbacklight wrapper script

This script provides nonlinear steps for controlling screen backlight with xbacklight.

Previously I've used xbacklight like this:
```
xbacklight +5%
xbacklight -5%
```
but on my screen those brightness intervals are too wide on low levels.

Here is link for desmos calculator:
https://www.desmos.com/calculator/f4yuku1e7g

You can for example configure your i3wm hotkeys like this:
```
bindsym XF86MonBrightnessUp exec --no-startup-id "python ~/scripts/backlight.py +"
bindsym XF86MonBrightnessDown exec --no-startup-id "python ~/scripts/backlight.py -"
```

Use generateSteps.py to generate invervals array.

#!/bin/sh

feh --bg-scale ~/.config/qtile/background.jpg &

nm-applet &

blueman-applet &

compton &

exit 0

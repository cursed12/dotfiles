#!/bin/sh

feh --bg-scale ~/.config/qtile/background.jpg &

nm-applet &

ibus-daemon &

blueman-applet &

compton &

exit 0

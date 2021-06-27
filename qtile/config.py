# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os, socket, subprocess
from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import qtile
from libqtile import hook

mod = "mod4"

# Some useful default apps on the system
# terminal = guess_terminal()
terminal = "gnome-terminal"
browser = "firefox"
calc = "gnome-calculator"
bluetooth = "blueman-manager"
wifi= "nm-connection-editor"
file_explorer = "nautilus"
calendar = "gnome-calendar"
screenshot = "gnome-screenshot"
spotify = "spotify"
search_command = "rofi -show run"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "s", lazy.spawncmd(),
        # desc="Spawn a command using a prompt widget"),

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn('amixer -q -D pulse sset Master 5%-')),
    Key([], "XF86AudioRaiseVolume", lazy.spawn('amixer -q -D pulse sset Master 5%+')),
    Key([], "XF86AudioMute", lazy.spawn('amixer -q -D pulse sset Master toggle')),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn('brightnessctl -d "intel_backlight" set +5%')),
    Key([], "XF86MonBrightnessDown", lazy.spawn('brightnessctl -d "intel_backlight" set 5%-')),

    # Some default apps
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "c", lazy.spawn(calc), desc="Launch calculator"),
    Key([mod], "e", lazy.spawn(file_explorer), desc="Launch file explorer"),
    Key([mod], "Print", lazy.spawn(screenshot+" -i"), desc="Screenshot Menu"),
    Key([mod, "shift"], "Print", lazy.spawn(screenshot+" -c -a"), desc="Screenshot Area"),
    # Key([mod, "control"], "Print", lazy.spawn(screenshot+" -c"), desc="Screenshot to clipboard"),
    Key([mod], "s", lazy.spawn(search_command), desc="Launch rofi"),

]

# Setting group names
group_list = ["Code", "Web", "Music", "Mail", "Fun", "What", "Even", "Is", "This"]
groups = [Group(i) for i in group_list]

for i, grp in enumerate(groups):
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(i+1), lazy.group[grp.name].toscreen(),
            desc="Switch to group {}".format(grp.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(i+1), lazy.window.togroup(grp.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(grp.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "50fa7b",
                "border_normal": "f8f8f2"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 14,
         sections = ["First", "Second", "Third", "Fourth"],
         section_fontsize = 13,
         border_width = 2,
         bg_color = "282a36",
         active_bg = "ffb86c",
         active_fg = "282a36",
         inactive_bg = "6272a4",
         inactive_fg = "282a36",
         padding_left = 0,
         padding_x = 2,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
]


mycolors = {
        "bg": ["#282a36", "#282a36"],
        "bglight": ["#44475a", "#44475a"],
        "white": ["#f8f8f2","#f8f8f2"],
        "purple": ["#bd93f9", "#bd93f9"],
        "green": ["#50fa7b", "#50fa7b"],
        "pink": ["#ff79c6", "#ff79c6"],
        "cyan": ["#8be9fd", "#8be9fd"],
        "yellow": ["#f1fa8c", "#f1fa8c"],
        "red": ["#ff5555", "#ff5555"],
        "orange": ["#ffb86c", "#ffb86c"],
        "dark purple": ["#6272a4", "#6272a4"]
        }

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu",
    fontsize = 14,
    padding = 2,
    background=mycolors["bg"],
    foreground=mycolors["white"]
)
extension_defaults = widget_defaults.copy()


widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground=mycolors["white"],
                       background = mycolors["bg"]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/python.png",
                       scale = 0.02,
                       ),
             widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground=mycolors["white"],
                       background = mycolors["bg"]
                       ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 14,
                       spacing = 2,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = mycolors["white"],
                       inactive = mycolors["dark purple"],
                       rounded = False,
                       highlight_color = mycolors["bglight"],
                       highlight_method = "line",
                       this_current_screen_border = mycolors["green"],
                       this_screen_border = mycolors["orange"],
                       other_current_screen_border = mycolors["green"],
                       other_screen_border = mycolors["orange"],
                       foreground = mycolors["white"],
                       background = mycolors["bg"]
                       ),
              # widget.Prompt(
                       # prompt = prompt,
                       # font = "Ubuntu",
                       # padding = 10,
                       # foreground = mycolors["red"],
                       # background = mycolors["bg"]
                       # ),
              widget.Sep(
                       linewidth = 0,
                       padding = 20,
                       foreground=mycolors["white"],
                       background = mycolors["bg"]
                       ),
              # widget.WindowName(
                       # foreground = mycolors["green"],
                       # background = mycolors["bg"],
                       # padding = 0
                       # ),
              # widget.TextBox(
                       # text = '\u25e2',
                       # background = mycolors["bg"],
                       # foreground = ["#d5c4a1", "#d5c4a1"],
                       # padding = 0,
                       # fontsize = 42
                       # ),
              widget.Spacer(
                       length=425,
                       background=mycolors["bg"]
                      ),
              widget.Image(
                       filename = "~/.config/qtile/icons/clock.png",
                       background = mycolors["bg"],
                       mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(calendar)},
                       padding=6,
                       ),
              widget.Clock(
                       foreground = mycolors["white"],
                       background = mycolors["bg"],
                       format = "%A, %B %d  %H:%M ",
                       padding=6
                       ),
              widget.Spacer(
                       background=mycolors["bg"]
                      ),
              # widget.CheckUpdates(
                       # update_interval = 1800,
                       # distro = "Ubuntu",
                       # display_format = "{updates} updates",
                       # foreground = mycolors["purple"],
                       # background = mycolors["bglight"],
                       # padding=6,
                       # no_update_string="0 updates"
                       # ),
              widget.Image(
                       filename = "~/.config/qtile/icons/wifi.png",
                       background = mycolors["bg"],
                       mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(wifi)},
                       padding=6,
                       ),
             widget.Net(
                       format="{up}↑↓{down}",
                       foreground = mycolors["green"],
                       background = mycolors["bg"],
                       rounded=True,
                       padding = 6
                       ),
              widget.Systray(
                       background = mycolors["bg"],
                       padding = 6
                       ),
             widget.Sep(
                       linewidth = 3,
                       padding = 10,
                       foreground=mycolors["bglight"],
                       background = mycolors["bg"]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/bluetooth.png",
                       background = mycolors["bg"],
                       mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(bluetooth)},
                       padding=6,
                       ),
             widget.Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground=mycolors["bglight"],
                       background = mycolors["bg"]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/spotify.png",
                       background = mycolors["bg"],
                       mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(spotify)},
                       padding=6,
                       scale=0.5
                       ),
             widget.Sep(
                       linewidth = 3,
                       padding = 10,
                       foreground=mycolors["bglight"],
                       background = mycolors["bg"]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/volume.png",
                       background = mycolors["bg"],
                       padding=6,
                       ),
              widget.Volume(
                       foreground = mycolors["orange"],
                       background = mycolors["bg"],
                       device='pulse',
                       padding = 6
                       ),
             widget.Sep(
                       linewidth = 3,
                       padding = 10,
                       foreground=mycolors["bglight"],
                       background = mycolors["bg"]
                       ),
              widget.CurrentLayout(
                       foreground = mycolors["yellow"],
                       background = mycolors["bg"],
                       padding = 6
                       ),
             widget.Sep(
                       linewidth = 3,
                       padding = 10,
                       foreground=mycolors["bglight"],
                       background = mycolors["bg"]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/battery.png",
                       background = mycolors["bg"],
                       ),
              widget.Battery(
                       foreground = mycolors["cyan"],
                       background = mycolors["bg"],
                       format = '{percent:2.0%} {char}',
                       charge_char="↑",
                       discharge_char="↓",
                       full_char="~",
                       show_short_text=False,
                       padding=6
                      ),
             widget.Sep(
                       linewidth = 3,
                       padding = 10,
                       foreground=mycolors["bglight"],
                       background = mycolors["bg"]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/refresh.png",
                       background = mycolors["bg"],
                       mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn('reboot')}
                       ),
             widget.Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground=mycolors["bglight"],
                       background = mycolors["bg"]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/power.png",
                       background = mycolors["bg"],
                       mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn('shutdown now')}
                       ),
             widget.Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground=mycolors["bglight"],
                       background = mycolors["bg"]
                       ),
              # widget.QuickExit(
                      # default_text = "Shutdown ಥ_ಥ",
                       # countdown_format = "T-minus {} s",
                       # foreground = mycolors["red"],
                       # background = mycolors["bglight"],
                       # padding=6
                       # ),

              ]

screens = [
    Screen(
        top=bar.Bar(
            widgets_list,
            24,
            opacity=1.0
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag(["shift"], "Button1", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='nm-connection-editor'),
    Match(wm_class='blueman-manager'),
    Match(wm_class='gnome-calendar'),
    Match(wm_class='pavucontrol'),
    Match(wm_class='simplescreenrecorder'),
    # Match(wm_class='org.gnome.Nautilus'),
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# Startup hookj
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

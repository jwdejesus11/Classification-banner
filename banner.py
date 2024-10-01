from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import sys
import os
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from tempfile import TemporaryFile
import time
from socket import gethostname

# Global Configuration File
CONF_FILE = "/etc/classification-banner"

# Returns Username
def get_user():
    try:
        user = os.getlogin()
    except:
        user = ''
    return user

# Returns Hostname
def get_host():
    host = gethostname()
    host = host.split('.')[0]
    return host


# Classification Banner Class
class ClassificationBanner:
    """Class to create and refresh the actual banner."""

    def __init__(self, message="TOP SECRET", fgcolor="#FFFFFF",
                 bgcolor="#FF0000", face="liberation-sans", size="small",
                 weight="bold", x=0, y=0, esc=True, opacity=0.75,
                 sys_info=False, taskbar_offset=40, banner_width=0, 
                 click_to_move=False, banner_height=15):

        """Set up and display the main window"""
        self.hres = x
        self.vres = y

        # Create Main Window
        self.window = Gtk.Window()
        self.window.set_position(Gtk.WindowPosition.CENTER)
        if esc:
            self.window.connect("key-press-event", self.keypress)

        # Prevent window from appearing in taskbar
        self.window.set_property('skip-taskbar-hint', True)
        self.window.set_property('skip-pager-hint', True)

        # Set type hint to make it stay above
        self.window.set_type_hint(Gdk.WindowTypeHint.UTILITY)  # Change to UTILITY

        # Prevent window from being closed
        self.window.connect("delete-event", self.on_delete_event)

        self.window.set_decorated(False)
        self.window.set_keep_above(True)
        self.window.set_app_paintable(True)

        try:
            self.window.set_opacity(opacity)
        except:
            pass

        # Set the default window size, change height to banner_height (e.g., 15)
        self.window.set_default_size(int(self.hres), banner_height)

        # Create Main Box with red background
        self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.box.set_size_request(int(self.hres), banner_height)
        self.box.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 0, 0, 1))  # Rojo

        # Create the label with markup
        self.center_label = Gtk.Label()
        self.center_label.set_markup("<span font_family='%s' weight='%s' foreground='%s' size='%s'>%s</span>" %
                                     (face, weight, fgcolor, size, message))
        self.box.pack_start(self.center_label, True, True, 0)

        self.window.add(self.box)
        self.window.show_all()

    def on_delete_event(self, widget, event):
        # When the close event is triggered, minimize the window instead
        self.window.iconify()
        return True  # Prevent the window from being destroyed

    # Press ESC to hide window for 15 seconds
    def keypress(self, widget, event=None):
        if event.keyval == 65307:  # ESC key
            if not Gtk.events_pending():
                self.window.iconify()
                self.window.hide()
                time.sleep(15)
                self.window.show()
                self.window.deiconify()
                self.window.present()
        return True


class DisplayBanner:
    """Display Classification Banner Message"""
    def __init__(self):
        self.monitor = Gdk.Screen.get_default()
        
        self.config = self.configure()
        self.execute(self.config)

    # Read configuration(s)
    def configure(self):
        defaults = {
            "message": "TOP SECRET",  # Updated message
            "fgcolor": "#FFFFFF",
            "bgcolor": "#FF0000",  # Updated background color to red
            "face": "liberation-sans",
            "size": "small",
            "weight": "bold",
            "show_top": True,
            "show_bottom": True,
            "hres": 0,
            "vres": 0,
            "sys_info": False,
            "opacity": 0.75,
            "esc": True,
            "taskbar_offset": 40,
            "banner_height": 15  # Reduced banner height
        }
        
        return defaults

    # Launch the Classification Banner Window(s)
    def execute(self, options):
        screen = self.monitor
        self.x = screen.get_width()
        self.y = screen.get_height()

        if options["show_top"]:
            top = ClassificationBanner(
                options["message"],
                options["fgcolor"],
                options["bgcolor"],
                options["face"],
                options["size"],
                options["weight"],
                self.x,
                self.y,
                options["esc"],
                options["opacity"],
                options["sys_info"],
                options["taskbar_offset"],
                options.get("banner_width", 0),
                options.get("click_to_move", False),
                banner_height=options["banner_height"]
            )
            top.window.move(0, 0)  # Banner at the top

        if options["show_bottom"]:
            bottom = ClassificationBanner(
                options["message"],
                options["fgcolor"],
                options["bgcolor"],
                options["face"],
                options["size"],
                options["weight"],
                self.x,
                self.y,
                options["esc"],
                options["opacity"],
                options["sys_info"],
                options["taskbar_offset"],
                options.get("banner_width", 0),
                options.get("click_to_move", False),
                banner_height=options["banner_height"]
            )
            bottom.window.move(0, self.y - options["banner_height"] - options["taskbar_offset"])  # Banner at the bottom

    # Relaunch the Classification Banner on Screen Resize
    def resize(self, widget, data=None):
        self.config = self.configure()
        self.execute(self.config)
        return True


def main():
    run = DisplayBanner()
    Gtk.main()

if __name__ == "__main__":
    main()

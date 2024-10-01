# Classification-banner
Step-by-step guide for setting up the Classification Banner

Step 1: Install necessary dependencies
Run the following commands in the terminal to install all the required dependencies:

1. Update the system and repositories:
   sudo yum update

2. Install necessary dependencies:
   sudo yum install epel-release -y
   sudo yum install python3 python3-pip python3-gobject cairo-gobject cairo-gobject-devel -y

3. Install PyGObject using pip (for GTK):
   sudo pip3 install PyGObject


Step 2: Download and configure the Classification Banner code
1. Clone or download the project:
   - If you have the code in a ZIP file, extract it.
   - If the code is in a git repository, clone it with the following command:
     git clone https://github.com/your-repo/classification-banner.git

2. Navigate to the project directory:
   cd classification_banner/src/


Step 3: Run the Classification Banner
1. Run the banner script:
   From the "src" directory, execute the banner.py file:
     python3 banner.py


Step 4: Customize the Banner message (Optional)
If you want to change the banner message, colors, or size, you can modify the default values in the code:

- Default message (message): Change the "TOP SECRET" value in the code.
- Colors: Modify the value of bgcolor (background) and fgcolor (text).
- Banner height: Adjust the value of banner_height (25 for a thin line).


Step 5: Set the banner to run automatically at startup (Optional)
1. Create a .desktop file in ~/.config/autostart/:
   mkdir -p ~/.config/autostart
   nano ~/.config/autostart/banner.desktop

2. Add the following content to the file:
   [Desktop Entry]
   Type=Application
   Exec=python3 /path/to/your/classification_banner/src/banner.py
   Hidden=false
   NoDisplay=false
   X-GNOME-Autostart-enabled=true
   Name=Classification Banner
   Comment=Run classification banner at startup

3. Save and close the file.


Final Summary
Dependencies:
   - Python 3, PyGObject, cairo-gobject

Instructions to run:
   - Navigate to the project directory: cd classification_banner/src/
   - Run the banner: python3 banner.py

Optional configurations:
   - Change the message, color, and size of the banner in the source code.
   - Set the banner to start automatically with a .desktop file.



from PanelBuilder import PanelBuilder
import os
import re
import sys

dest_dir_options = """
1. Root panel extension folder
2. User panel extension folder
3. Custom path
"""
print dest_dir_options

dest_dir_input = raw_input("Where would you like to save this panel? >>  ")
validate_input(r"[1-3]",dest_dir_input)

if dest_dir_input == "3":
	dest_dir_input = raw_input("Please provide the path here >>  ")
	validate_input(r"[^\0]+",dest_dir_input)
elif dest_dir_input == "2":
	dest_dir_input = os.path.expanduser("~") + "/Library/Application Support/Adobe/CEP/extensions/"
elif dest_dir_input == "1":
	dest_dir_input = "/Library/Application Support/Adobe/CEP/extensions/"
	print "Make sure to start the application with sudo access"

bunle_id_input = raw_input("Please choose your bundle id here >>  ")
validate_input(r"[^\0]+",bunle_id_input)
dest_dir_input += bunle_id_input

menu_name_input = raw_input("Please choose your menu name here >>  ")
validate_input(r"[^\0]+",menu_name_input)

cc_version_options = """
1. CC 2014
2. CC 2015
3. CC 2015.5
4. CC 2017
5. CC 2018
6. Older
"""
print cc_version_options

cc_version_input = raw_input("what's the newest version of CC is this extension going to be built to support? (select one)")
validate_input(r"[1-6]",cc_version_input)

version_dict = {
	"1":"2014",
	"2":"2015",
	"3":"2015.5",
	"4":"2017",
	"5":"2018",
	"6":"default"
}
cc_version_input_converted = version_dict[cc_version_input]

# Set host list
host_options = """
1. Photoshop
2. InDesign
3. InCopy
4. Illustrator
5. Premier Pro
6. Prelude
7. After Effects
8. Animate
9. Audition
10. Dreamweaver
11. Muse
12. Bridge
"""
print host_options
host_input = raw_input("Which application is this exntension built for? (comma seprated numbers only)")
validate_input(r"^([1-9]|[1][0-2])(,([1-9]|[1][0-2]))*$",host_input)

host_dict = {
	"1":["PHSP", "PHXS"],
	"2":["IDSN"],
	"3":["AICY"],
	"4":["ILST"],
	"5":["PPRO"],
	"6":["PRLD"],
	"7":["AEFT"],
	"8":["FLPR"],
	"9":["AUDT"],
	"10":["DRWV"],
	"11":["MUSE"],
	"12":["KBRG"],
}

suppported_apps_input = list()
for choice in host_input.split(","):
	suppported_apps_input += host_dict[choice]

panel = PanelBuilder(dest_dir_input, bunle_id_input, menu_name_input, cc_version_input_converted, suppported_apps_input)
panel.copy_panel()
panel.setup_manifest()
print_followup_directions()

def validate_input(regex, user_input):
	if not re.match(regex, user_input):
	  print "invalid user input"
	  sys.exit()

def print_followup_directions():
    print("")
    print("Your panel has been created!")
    print("")
    print("Don't forget to do the following: ")
    print("1. Add CSInterface.js to /client/js/lib/")
    print("(Available here: https://github.com/Adobe-CEP/CEP-Resources)")
    print("2. git init")
    print("3. Add this directory to the root or user's .../Adobe/CEO/extensions/ directory.")
    print("(See the CEP documentation for details)")

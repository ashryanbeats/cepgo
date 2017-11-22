import re
import sys

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

dest_dir_options = """
	1. Root panel extension folder
	2. User panel extension folder
	3. Custom path
	"""

cc_version_options = """
	1. CC 2014
	2. CC 2015
	3. CC 2015.5
	4. CC 2017
	5. CC 2018
	6. Older
	"""

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

version_dict = {
	"1":"2014",
	"2":"2015",
	"3":"2015.5",
	"4":"2017",
	"5":"2018",
	"6":"default"
}

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
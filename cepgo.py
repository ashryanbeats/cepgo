import os
import sys
from PanelBuilder import PanelBuilder
from cli_helper import dest_dir_options, cc_version_options, host_options, version_dict, host_dict, validate_input, print_followup_directions

def main ():
	print dest_dir_options

	dest_dir_input = raw_input("Where would you like to save this panel? >>  ")
	validate_input(r"[1-3]", dest_dir_input)

	if dest_dir_input == "3":
		dest_dir_input = raw_input("Please provide the path here >>  ")
		validate_input(r"[^\0]+", dest_dir_input)
	elif dest_dir_input == "2":
		if sys.platform == "win32":
			dest_dir_input = os.path.expanduser("~") + "\AppData\Roaming\Adobe\CEP/extensions"
		elif sys.platform == "darwin":
			dest_dir_input = os.path.expanduser("~") + "/Library/Application Support/Adobe/CEP/extensions/"
		else:
			print "Only Mac and Windows are currently supported. Please use option 3 to provide a custom path"
			main()
	elif dest_dir_input == "1":
		if sys.platform == "win32":
			dest_dir_input = "C:\Program Files\Common Files\Adobe\CEP\extensions/"
		elif sys.platform == "darwin":	
			dest_dir_input = "/Library/Application Support/Adobe/CEP/extensions/"
		else:
			print "Only Mac and Windows are currently supported. Please use option 3 to provide a custom path"
			main()
		print "Make sure to start the application with sudo access"

	bunle_id_input = raw_input("Please choose your bundle id here >>  ")
	validate_input(r"[^\0]+", bunle_id_input)
	dest_dir_input += bunle_id_input

	menu_name_input = raw_input("Please choose your menu name here >>  ")
	validate_input(r"[^\0]+", menu_name_input)

	print cc_version_options

	cc_version_input = raw_input("what's the newest version of CC is this extension going to be built to support? (select one)")
	validate_input(r"[1-6]", cc_version_input)

	cc_version_input_converted = version_dict[cc_version_input]

	print host_options
	host_input = raw_input("Which application is this exntension built for? (comma seprated numbers only)")
	validate_input(r"^([1-9]|[1][0-2])(,([1-9]|[1][0-2]))*$",host_input)

	suppported_apps_input = list()
	for choice in host_input.split(","):
		suppported_apps_input += host_dict[choice]

	panel = PanelBuilder(dest_dir_input, bunle_id_input, menu_name_input, cc_version_input_converted, suppported_apps_input)
	panel.copy_panel()
	panel.setup_manifest()
	print_followup_directions()

if __name__ == "__main__":
	main()


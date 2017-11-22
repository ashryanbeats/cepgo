#!/usr/bin/env python
import sys
sys.dont_write_bytecode = True
import os
from shutil import copytree, rmtree, ignore_patterns
import product_version
import xml.etree.ElementTree as ET


class PanelBuilder(object):
    def __init__(self, dest_dir, bundle_id, menu_name, version, suppported_apps=[]):
        self.dest_dir = dest_dir
        self.bundle_id = bundle_id
        self.menu_name = menu_name
        self.version = version
        self.suppported_apps = suppported_apps
        self.xml_path = None
        self._script_dir = self._get_script_dir()

    def copy_panel(self):
    	try:
    	    copytree(self._script_dir, self.dest_dir, ignore=ignore_patterns('*.gitignore', '*.py', '*.DS_Store', '*.git', '*.pyc'))
    	except (IOError, OSError) as e:
    	    print("OS Error: ")
    	    print(e)
    	    print("Please try again.")
    	    sys.exit()

    def setup_manifest(self, manifest_path=None):
    	if not manifest_path:
    		if self.dest_dir.endswith('/'):
    			self.dest_dir = self.dest_dir[:-1]
    		manifest_path = self.dest_dir + "/CSXS/manifest.xml"
    	# Read in manifest
    	self.xml_path = manifest_path
    	manifest_tree = ET.parse(manifest_path)
    	manifest_root = manifest_tree.getroot()

    	# Set attributes
    	manifest_root.set("ExtensionBundleId", self.bundle_id)
    	manifest_root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")

    	extension_elements = manifest_tree.findall(".//Extension")
    	for element in extension_elements:
    	    element.set("Id", self.bundle_id + ".panel")

    	# Set menu name
    	menu_element = manifest_tree.find(".//Menu")
    	menu_element.text = self.menu_name
    	host_element = manifest_tree.find(".//HostList")
    	for host_id in self.suppported_apps:
	    	if host_id not in product_version.data:
	    		print "invalid host application id"
	    		sys.exit()
    		elif self.version not in product_version.data["PHSP"]:
    			print "invalid version"
    			sys.exit()
    		else:
    			PS = ET.SubElement(host_element, "Host")
    			PS.set("Name", host_id)
    			PS.set("Version", product_version.data[host_id][self.version])
		indent(manifest_root)
		manifest_tree.write(manifest_path, encoding="UTF-8", xml_declaration=True, method="xml")

	def setup_debug(self, debug_path = None):
	    ## DEBUG
	    # Read in debug file
	    if not debug_path:
	    	debug_path = self.dest_dir + "/.debug"
	    debug_tree = ET.parse(debug_path)

	    # Set attribute
	    debug_extension_element = debug_tree.find(".//Extension")
	    debug_extension_element.set("Id", self.bundle_id + ".panel")

	    # Write debug file
	    debug_tree.write(debug_path, encoding="UTF-8", xml_declaration=True, method="xml")

    def _get_script_dir(self):
	    return os.path.dirname(os.path.realpath(__file__))


def indent(elem, level=0):
  	i = "\n" + level*"  "
  	if len(elem):
		if not elem.text or not elem.text.strip():
			elem.text = i + "  "
		if not elem.tail or not elem.tail.strip():
			elem.tail = i
		for elem in elem:
			indent(elem, level+1)
		if not elem.tail or not elem.tail.strip():
			elem.tail = i
  	else:
	    if level and (not elem.tail or not elem.tail.strip()):
	    	elem.tail = i

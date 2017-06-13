#!/usr/bin/env python
import xml.etree.ElementTree as ET
import os
import sys
sys.dont_write_bytecode = True

def run_xml_setup(dest_dir):
    extension_bundle_id = raw_input("Extension Bundle ID: ")
    menu_name = raw_input("Menu name: ")

    setup_manifest(dest_dir, extension_bundle_id, menu_name)
    setup_debug(dest_dir, extension_bundle_id)

def setup_manifest(dest_dir, extension_bundle_id, menu_name):
    ## MANIFEST
    # Read in manifest
    manifest_tree = ET.parse(dest_dir + "/CSXS/manifest.xml")
    manifest_root = manifest_tree.getroot()

    # Set attributes
    manifest_root.set("ExtensionBundleId", extension_bundle_id)
    manifest_root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")

    extension_elements = manifest_tree.findall(".//Extension")
    for element in extension_elements:
        element.set("Id", extension_bundle_id + ".panel")

    # Set menu name
    menu_element = manifest_tree.find(".//Menu")
    menu_element.text = menu_name

    # Write manifest
    manifest_tree.write(dest_dir + "/CSXS/manifest.xml", encoding="UTF-8", xml_declaration=True, method="xml")

def setup_debug(dest_dir, extension_bundle_id):
    ## DEBUG
    # Read in debug file
    debug_tree = ET.parse(dest_dir + "/.debug")

    # Set attribute
    debug_extension_element = debug_tree.find(".//Extension")
    debug_extension_element.set("Id", extension_bundle_id + ".panel")

    # Write debug file
    debug_tree.write(dest_dir + "/.debug", encoding="UTF-8", xml_declaration=True, method="xml")

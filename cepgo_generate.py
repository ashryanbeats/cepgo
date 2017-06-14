#!/usr/bin/env python
import sys
sys.dont_write_bytecode = True
import cepgo_xml
import cepgo_crud
import cepgo_postprint


# Make sure you aren't in the script folder
cepgo_crud.check_dir_location()

# Copy files to destination
dest_dir = cepgo_crud.get_dest_dir()
cepgo_crud.copy_files(cepgo_crud.get_script_dir(), dest_dir)

# Set up xml files
cepgo_xml.run_xml_setup(dest_dir)

# Clean up the destination folder
cepgo_crud.cleanup(dest_dir)

# Tell the user what to do next
cepgo_postprint.print_followup_directions()

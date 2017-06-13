#!/usr/bin/env python
import os
import shutil
import sys


def get_script_dir():
    return os.path.dirname(os.path.realpath(__file__))

def get_cwd():
    return os.getcwd()

def check_dir_location():
    # Check dir location
    if get_script_dir() == get_cwd():
        print("You're in the script directory.")
        print("Please make a new directory and try again.")
        sys.exit()

def get_dest_dir():
    dirname = raw_input("Extension dir name: ")
    return get_cwd() + "/" + dirname

def copy_files(script_dir, dest_dir):
    # Setup destination
    try:
        shutil.copytree(script_dir, dest_dir)
    except OSError as e:
        print("")
        print("This directory already exists: " + e.filename)
        print("Please try again.")
        sys.exit()

def cleanup(dest_dir):
    filenames = ["cepgo_generate.py", "cepgo_xml.py", "cepgo_crud.py", ".gitignore", ".DS_Store"]

    for filename in filenames:
        try:
            os.remove(dest_dir + "/" + filename)
        except OSError as e:
            print(e)
            pass    # File wasn't removed. Ignore and continue.

    shutil.rmtree(dest_dir + "/.git")
    os.rename(dest_dir + "/target-repo-gitignore", dest_dir + "/.gitignore")

#!/usr/bin/env python3
# Sample script that writes to a file
# By Sam 10/31
import os

# find current directory
script_path = os.path.realpath(__file__)
script_folder = os.path.split(script_path)
#print(script_path)
#print(script_folder)

# Open file for writing
test_file = open(script_folder[0] + "/testfile.txt", "w")

# Write lines to the file
test_file.write("Hello World\n")
test_file.write("\taonther line\n")
test_file.write("Last line\n")

# Close the file
test_file.close()
import sys, getopt
import fileinput

from acom_config import *

# Read in the arguments that will perform the replacements of the values specified
# The following paramters are accepted:
#
#   -g, --resourcegroup
#   -s, --storageaccount
#   -v, --virtualmachine
#   -c, --custom
#   -r, --replace
#
# --custom and --replace provide a means for something specific to a single doc to be handled
# This could be something like specifying the size of a disk to be added to a VM, something not common or should coded for catching every possibility
# Use case would be something like `code_cleaner.py --custom=<size_in_GB> --replace 5`

try:
    opts, args = getopt.getopt(sys.argv[1:], 'g:s:n:c:r', ["resourcegroup=", "storageaccount=", "virtualmachine=", "custom=", "replace="])
except getopt.GetoptError:
    print("Encountered an error parsing the provided arguments")
    sys.exit(2)

# Loop through all the arguments provided and create the appropriate resources
for opt, arg in opts:
    # Create a resource group
    if opt in ('-g', '--resourcegroup'):
        for line in fileinput.FileInput(commands_list, inplace=True):
            line = line.replace(arg,resourcegroup_name)
            print(line)

    # Create a storage account
    elif opt in ('-s', '--storageaccount'):
        for line in fileinput.FileInput(commands_list, inplace=True):
            line = line.replace(arg,storageaccount_name)
            print(line)

    # Create a virtual machine
    elif opt in ('-v', '--virtualmachine'):
        for line in fileinput.FileInput(commands_list, inplace=True):
            line = line.replace(arg,vm_name)
            print(line)

    # Handle a custom replacement request
    elif opt in ('-c', '--custom'):
        custom=arg

    # Perform the handling a custom replacement request
    elif opt in ('-r', '--replace'):
        for line in fileinput.FileInput(commands_list, inplace=True):
            line = line.replace(custom,arg)
            print(line)

    # Otherwise we have an unknown parameter
    else:
        print("Unknown parameter passed")
        sys.exit(2)


# Try to catch any special characters that may be in the code samples
# For example, values that user should enter may be written <likethis>
# Otherwise we'll replace names below with these characters still in place
for line in fileinput.FileInput(commands_list, inplace=True):
    line = line.replace('<','')
    line = line.replace('>','')
    print(line)

# Do some house-keeping to clean up blank lines  
for line in fileinput.FileInput(commands_list,inplace=True):
    if line.rstrip():
        print(line)
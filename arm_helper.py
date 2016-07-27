import sys, getopt
import fileinput

from acom_config import *

# Create an empty list to hold the Azure CLI commandsto create the requested resources
# Once all arguments have been processed, we'll then just make one write out to commands list file
resources = []

# Read in the arguments that will create whatever resources the user requires
# The following paramters are accepted:
#
#   -g, --resourcegroup
#   -s, --storageaccount
#   -n, --virtualnetwork
#   -v, --virtualmachine

try:
    opts, args = getopt.getopt(sys.argv[1:], 'g:s:n:v', ["resourcegroup", "storageaccount", "virtualnetwork", "virtualmachine"])
except getopt.GetoptError:
    print("Encountered an error parsing the provided arguments")
    sys.exit(2)

# Loop through all the arguments provided and create the appropriate resources
for opt, arg in opts:
    # Create a resource group
    if opt in ('-g', '--resourcegroup'):
        with open(commands_list, 'r+') as f:
            resources.append('azure group create ' + resourcegroup_name + ' -l ' + location + '\n')

    # Create a storage account
    elif opt in ('-s', '--storageaccount'):
        with open(commands_list, 'r+') as f:
            resources.append('azure storage account create -g ' + resourcegroup_name + ' -l ' + location + ' --kind Storage --sku-name LRS ' + storageaccount_name + '\n')

    # Create a virtual network
    elif opt in ('-n', '--virtualnetwork'):
        resources.append('azure network vnet create -g ' + resourcegroup_name + ' -l ' + location + ' -n ' + virtualnetwork_name + ' -a ' + virtualnetwork_prefix + '\n')
        resources.append('azure network vnet subnet create -g ' + resourcegroup_name + ' -e ' + virtualnetwork_name + ' -n ' + virtualnetwork_subnet_name + ' -a ' + virtualnetwork_subnet_prefix + '\n')

    # Create a virtual machine
    elif opt in ('-v', '--virtualmachine'):
        with open(commands_list, 'r+') as f:
            resources.append('azure vm create -g ' + resourcegroup_name + ' -n ' + vm_name + ' -y ' + vm_os_type + ' -l ' + location + ' -Q ' + vm_image + ' -o ' + storageaccount_name + ' -F ' + virtualnetwork_name + ' -j ' + virtualnetwork_subnet_name + ' -f ' + vm_nic_name + ' -u ' + vm_username + ' -p ' + vm_password + ' -z ' + vm_size + ' \n')

    # Otherwise we have an unknown parameter
    else:
        print("Unknown parameter passed")
        sys.exit(2)

# Now write back out to file so that our build tool can import it
# We actually read in the existing file, write out our new commands to the top, then write the existing commands back in
with open(commands_list, "r+") as f:
    lines = f.readlines()
    f.seek(0)

    for s in resources:
       f.write(s)
    
    f.writelines(lines)
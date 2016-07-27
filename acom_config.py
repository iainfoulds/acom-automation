# Change the following variables to match your setup

# Do not enter your primary Azure account or MSFT account!
# Create a user within Azure AAD that has rights to create resources within your subscription
azure_username = "username@domain.onlive.microsoft.com"
azure_password = "password"

# Location for creating your Azure resources
location = "westus"


# These can largely be left alone since a random integer is appended each time
# If you really want to change them, go ahead
# Created resources should also be cleaned up after each run, so really, don't worry too much :)
resourcegroup_name = "ACOMAutomationRG"
storageaccount_name = "acomstorage"

virtualnetwork_name = "ACOMAutomationVNet"
virtualnetwork_prefix = "10.0.0.0/8"
virtualnetwork_subnet_name = "ACOMAutomationSubnet"
virtualnetwork_subnet_prefix = "10.0.1.0/24"

vm_name = "TestVM"
vm_os_type = "Linux"
vm_image = "CoreOS"
vm_nic_name = "TestVM-NIC"
vm_username = "ops"
vm_password = "ACOMP@ssw0rd!"
vm_size = "Standard_D1_v2"

base_path = "/usr/local/acomautomation/azure-content-pr/"
commands_list = "commands_list.txt"
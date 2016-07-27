import subprocess

from acom_config import *

# We're just calling a bash script here to execute all the Docker commands and run the Azure CLI against it
# The alternative is to drop a whole bunch of subprocess statements in to Python to essentially just execute bash commands
# So, let bash do it's thing, and just have Python kick it off so we can pass in parameters from the config file
subprocess.call(['bash', '/usr/local/acomautomation/docker_builder.sh', azure_username, azure_password, commands_list, resourcegroup_name])
#!/bin/bash

# Generate some randomness when we create our Docker container in case a job gets stuck
# If we don't, remaining jobs may fail as an `acomautomation` container already exists
RandomInt=$RANDOM
DockerName=acomautomation$RandomInt

# Now actually go ahead and create the Docker container of the Azure CLI tools
# We use this rather than a custom Docker container so that we'd always have the latest Azure CLI
# Really, the whole point is to try and catch a breaking change in the Azure CLI
docker create -it --name $DockerName microsoft/azure-cli
docker start $DockerName

# Copy over the list of Azure CLI commands parsed from the MD file and then run the Azure CLI commands
docker cp commands_list.txt $DockerName:/root/
docker exec $DockerName /bin/sh -c "azure login -u $1 -p $2;sh < /root/$3"

# Grab any azure.err files that are generated and copy them out of the Docker container for later review
docker cp $DockerName:/root/.azure/azure.err $DockerName.err

# Remove the Azure resources created during this build
docker exec $DockerName /bin/sh -c "azure group delete -n $4 --quiet"

# Clean up the Docker container by stopping and then removing it
docker stop $DockerName
docker rm $DockerName
#!/bin/bash

# Azure should have done this when the VM was provisioned, but just in case...
sudo apt-get update && sudo apt-get upgrade -y

# Grab the latest Jenkins build and install
wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update && sudo apt-get install jenkins -y

# Grab the latest Docker build and install
curl -sSL https://get.docker.com/ | sh
sudo usermod -aG docker jenkins

# Add a group for automation, add the Jenkins user, create a local directory
sudo groupadd acomautomation
sudo usermod -aG acomautomation jenkins
sudo mkdir /usr/local/acomautomation

# Configure git to grab the azure-content repo, configure permissions
sudo git clone https://github.com/azure/azure-content.git
cd azure-content
sudo git remote add upstream https://github.com/Azure/azure-content.git
sudo it fetch upstream
sudo git pull upstream master

sudo chown -R jenkins:acomautomation /usr/local/acomautomation

# Pull down the sample Jenkins project and restart Jenkins to load it in to memory
sudo mkdir /var/lib/jenkins/jobs/sample-acom-job
sudo wget -q -O /var/lib/jenkins/jobs/sample-acom-job/config.xml https://raw.githubusercontent.com/iainfoulds/acom-automation/master/scripts/jenkins_example_config.xml
sudo chown -R jenkins:jenkins /var/lib/jenkins/jobs/sample-acom-job
sudo service jenkins force-reload
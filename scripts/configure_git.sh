#!/bin/bash

cd /usr/local/acomautomation/

git clone https://[your GitHub user name]:[token]@github.com/[your GitHub user name]/azure-content-pr.git
cd azure-content-pr
git remote add upstream https://[your GitHub user name]:[token]@github.com/Azure/azure-content-pr.git
git fetch upstream
git pull upstream master

chown -R jenkins:acomautomation azure-content-pr
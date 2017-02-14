#! /bin/bash

# Update repo
#git checkout master
#git pull -q --ff-only

# make sure theme submodule is initialized
git submodule update --init --recursive

# Enable venv
if [ ! -d venv ]; then
    virtualenv venv
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt

# Build the site
make rsync_copy

# Disable venv
deactivate

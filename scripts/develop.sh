#! /bin/bash

# Update repo
git checkout master
git pull -q --ff-only
git submodule update --init --recursive

# Enable venv
if [ ! -d venv ]; then
    virtualenv venv -p python3
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt

# Build the site
make devserver

# Disable venv
deactivate

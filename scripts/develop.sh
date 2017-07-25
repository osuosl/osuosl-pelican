#! /bin/bash

# Update repo
git checkout master
git pull -q --ff-only

# this should update the dougfir pelican theme
git submodule update --init --recursive

# Enable venv
if [ ! -d venv ]; then
    virtualenv-2.7 venv
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt

# Build the site
make devserver

# Disable venv
deactivate

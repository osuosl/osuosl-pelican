#! /bin/bash

# Update repo
git checkout master
git pull -q --ff-only
git submodule update --init

# Enable venv
if [ ! -d venv ]; then
    virtualenv venv
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt
pip install pelican

# Build the site
make publish

# Disable venv
deactivate

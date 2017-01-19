#! /bin/bash

# Update repo
git checkout thai/https_protocol
git pull -q --ff-only
git submodule update --init --recursive

# Enable venv
if [ ! -d venv ]; then
    virtualenv venv
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt
pip install pelican

# Build the site
make staging

# Disable venv
deactivate

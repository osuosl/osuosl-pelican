#! /bin/bash

# Update repo
git checkout master
git pull -q --ff-only
git submodule update --init --recursive

# Enable venv
if [ ! -d venv ]; then
    python3.11 -m venv venv
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt

# Build the site
make devserver

# Disable venv
deactivate

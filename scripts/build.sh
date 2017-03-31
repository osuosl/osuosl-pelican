#! /bin/bash

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
# make rsync_copy first calls make publish, which builds using publishconf.py
make rsync_copy >&1

if [ $? -eq 0 ]
then
  deactivate
else
  exit 1
fi

# Disable venv
# deactivate

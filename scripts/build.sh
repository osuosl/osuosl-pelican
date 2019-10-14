#! /bin/bash

# make sure theme submodule is initialized
git submodule update --init --recursive

# Enable venv
if [ ! -d venv ]; then
    virtualenv venv -p python3
fi

source venv/bin/activate

# Update packages
pip install -r requirements.txt

# Build the site
# make rsync_copy first calls make publish, which builds using publishconf.py
make rsync_copy

# if we don't exit here, this script exits with status 0, even if the build
# had failures or warnings

if [ $? -eq 0 ]
then
  deactivate
else
  deactivate
  exit 1
fi

#! /bin/bash

# make sure theme submodule is initialized
git submodule update --init --recursive

# Enable venv
if [ ! -d venv ]; then
    python3.11 -m venv venv
fi

source venv/bin/activate

# Update packages
pip install -r requirements.txt

if [ -n "${CHECK_LINT}" ]; then
  make -e lint_changed
fi

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

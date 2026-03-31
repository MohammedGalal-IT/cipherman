#!/bin/bash

# Install python package
if ! pip3 install .; then
    echo "
### pip3 command failed. Trying alternative commands...
"

fi

if ! pipx install .; then
    echo "pipx command failed. Ensure pipx is installed and try again."
    sudo apt install pipx
    pipx install .
    pipx ensurepath
    echo "Open new terminal to use cipherman command"
fi




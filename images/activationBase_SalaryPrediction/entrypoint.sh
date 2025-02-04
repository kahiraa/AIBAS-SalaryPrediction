#!/bin/sh

# Ensure the volume directory exists
mkdir -p /tmp/activationBase

# Copy the file if it's missing or empty
if [ ! -s /tmp/activationBase/activation_data.csv ]; then
    cp data/activation_data.csv /tmp/activationBase/
fi

# Keep the container running
exec sh

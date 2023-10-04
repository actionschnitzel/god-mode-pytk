#!/bin/bash

# Define the GitHub repository
REPO="lutris/lutris"

# Retrieve the download URL for the latest release
LATEST_URL=$(curl -sL "https://api.github.com/repos/$REPO/releases/latest" | jq -r '.assets[] | select(.name | contains(".deb")) | .browser_download_url')

# Define the directory where the .deb package will be downloaded
DOWNLOAD_DIR="$HOME/Downloads"

# Create the download directory if it doesn't exist
mkdir -p "$DOWNLOAD_DIR"

# Navigate to the download directory
cd "$DOWNLOAD_DIR"

# Download the .deb package
wget "$LATEST_URL" -O "lutris_latest.deb"

# Install the .deb package using apt
sudo apt install "./lutris_latest.deb"

# Clean up: remove the downloaded .deb file (optional)
rm "./lutris_latest.deb"

# Print a message indicating that the installation is complete
echo "Lutris installation is complete."

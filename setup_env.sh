#!/bin/bash

# 1. Create the project structure
echo "Creating project directories..."
mkdir -p data outputs

# 2. Install Python dependencies
echo "Installing Python libraries from requirements.txt..."
pip install -r requirements.txt

# 3. Optional: System dependencies
# echo "Note: Chrome installation skipped. Uncomment lines below if Selenium is needed."
# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# sudo apt install ./google-chrome-stable_current_amd64.deb

echo "--- Setup Complete! Project is ready. ---"
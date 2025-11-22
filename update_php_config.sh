#!/bin/bash
# AI-generated code - Script to update PHP configuration for OpenEMR
# This script updates the php.ini file to meet OpenEMR's requirements

PHP_INI="/opt/homebrew/etc/php/8.5/php.ini"

echo "Updating PHP configuration at $PHP_INI..."

# Backup first
sudo cp "$PHP_INI" "${PHP_INI}.backup.$(date +%Y%m%d_%H%M%S)"

# Update display_errors
sudo sed -i '' 's/^display_errors = On/display_errors = Off/' "$PHP_INI"

# Update max_input_vars
sudo sed -i '' 's/^max_input_vars = 1000/max_input_vars = 3000/' "$PHP_INI"

# Update max_execution_time
sudo sed -i '' 's/^max_execution_time = 30/max_execution_time = 60/' "$PHP_INI"

# Update max_input_time
sudo sed -i '' 's/^max_input_time = 60/max_input_time = -1/' "$PHP_INI"

# Update post_max_size
sudo sed -i '' 's/^post_max_size = 8M/post_max_size = 30M/' "$PHP_INI"

# Update memory_limit
sudo sed -i '' 's/^memory_limit = 128M/memory_limit = 512M/' "$PHP_INI"

# Update upload_max_filesize
sudo sed -i '' 's/^upload_max_filesize = 2M/upload_max_filesize = 30M/' "$PHP_INI"

# Enable mysqli.allow_local_infile (add if not exists)
if ! grep -q "^mysqli.allow_local_infile" "$PHP_INI"; then
    echo "" | sudo tee -a "$PHP_INI"
    echo "mysqli.allow_local_infile = On" | sudo tee -a "$PHP_INI"
else
    sudo sed -i '' 's/^mysqli.allow_local_infile = Off/mysqli.allow_local_infile = On/' "$PHP_INI"
fi

echo "PHP configuration updated successfully!"
echo "You need to restart the PHP server for changes to take effect."

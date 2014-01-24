#!/bin/sh
# Setup a machine for Sublime Text
set -x

# Main Sublime Text 2 Application installation
sublime_dir=/Applications/Sublime\ Text.app/Contents

# symlink subl command
ln -s "$sublime_dir/SharedSupport/bin/subl" "$HOME/.dotfiles/bin/subl"

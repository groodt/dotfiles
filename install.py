#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import shutil
import sys


def install():
    linkables = glob.glob("*/*.symlink")
    cwd = os.getcwd()

    skip_all = False
    overwrite_all = False
    backup_all = False

    for linkable in linkables:
        overwrite = False
        backup = False
        skip = False

        dotfile_name = linkable.split("/").pop().replace(".symlink", "")
        dotfile_target = "%s/.%s" % (os.environ["HOME"], dotfile_name)

        if os.path.exists(dotfile_target):
            if not (skip_all or overwrite_all or backup_all):
                print "File already exists: %s, what do you want to do? [s]kip, [S]kip all, [o]verwrite, [O]verwrite all, [b]ackup, [B]ackup all" % dotfile_target
                choice = raw_input().strip()
                if choice == "o":
                    overwrite = True
                elif choice == "O":
                    overwrite_all = True
                elif choice == "b":
                    backup = True
                elif choice == "B":
                    backup_all = True
                elif choice == "s":
                    skip = True
                elif choice == "S":
                    skip_all = True
                else:
                    raise ValueError("Invalid input.")

            if (skip or skip_all):
                print "Skipping..."
                continue
            else:
                if (overwrite or overwrite_all):
                    print "Overwriting..."
                    if os.path.islink(dotfile_target):
                        os.remove(dotfile_target)
                    else:
                        shutil.rmtree(dotfile_target)

                if (backup or backup_all):
                    print "Backing up..."
                    shutil.move(dotfile_target, dotfile_target + ".backup")

        print "Installing..."
        os.symlink("%s/%s" % (cwd, linkable), dotfile_target)

def uninstall():
    linkables = glob.glob("*/*.symlink")

    for linkable in linkables:
        dotfile_name = linkable.split("/").pop().replace(".symlink", "")
        dotfile_target = "%s/.%s" % (os.environ["HOME"], dotfile_name)

        if os.path.islink(dotfile_target):
            print "Removing dotfile: %s" % dotfile_target
            os.remove(dotfile_target)

        potential_backup_dotfile = dotfile_target + ".backup"
        if os.path.exists(potential_backup_dotfile):
            print "Reverting to backup: %s" % potential_backup_dotfile
            shutil.move(potential_backup_dotfile, dotfile_target)

if __name__ == "__main__":
    command = sys.argv[1].strip()
    if (command == "install"):
        install()
    elif (command == "uninstall"):
        uninstall()
    else:
        print "Valid commands: install, uninstall"

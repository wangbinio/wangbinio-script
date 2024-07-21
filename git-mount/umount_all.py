#!/usr/bin/env python3

import os
import subprocess

from dirs import directories

print(directories)

ip = "192.168.11.215"

base_path = "/home/szzh/git"

for dir in directories:
    git_dir = f"{base_path}/{dir}.git"
    if os.path.exists(git_dir):
        command = [
            "sudo",
            "umount",
            git_dir,
        ]
        print(command)
        subprocess.run(command)
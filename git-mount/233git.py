#!/usr/bin/env python3

import os
import subprocess

from dirs import directories

print(directories)

ip = "192.168.1.233"

base_path = "/home/szzh/git"

os.makedirs(base_path, exist_ok=True)

for dir in directories:
    git_dir = f"{base_path}/{dir}.git"
    os.makedirs(git_dir, exist_ok=True)
    command = [
        "sudo",
        "mount",
        "-t",
        "cifs",
        f"//{ip}/git/{dir}.git",
        git_dir,
        "-o",
        "username=summer,password=wangbinio",
    ]
    print(command)
    subprocess.run(command)

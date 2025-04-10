#!/usr/bin/env python3

import os
import subprocess

from dirs import *

print(directories)

base_path = "/home/szzh"

os.makedirs(base_path, exist_ok=True)

for dir in directories:
    target_dir = f"{base_path}/{dir}"
    command = ""    
    if os.path.isdir(target_dir):
        command = f"git -C {target_dir} pull"
    else:
        command = f"git clone {base_path}/git/{dir}.git {target_dir}"
    print(command)
    subprocess.run(command, shell=True)
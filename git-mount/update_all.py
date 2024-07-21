#!/usr/bin/env python3

import os
import subprocess

from dirs import directories

print(directories)

base_dirs = directories[:2]
base_path = "/home/szzh"
biandao_path=f"{base_path}/biandao_code"

for dir in directories:
    target_dir = ""
    if dir in base_dirs:
        target_dir = f"{base_path}/{dir}"
    else:
        target_dir = f"{biandao_path}/{dir}"
    
    command = ""    
    if os.path.isdir(target_dir):
        command = f"git -C {target_dir} pull"
    else:
        command = f"git clone {base_path}/git/{dir}.git {target_dir}"
    print(command)
    subprocess.run(command, shell=True)
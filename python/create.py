#!/usr/bin/env python3

import argparse
import shutil
import os

def replace_demo_in_cmake(target_dir, new_name):
    cmake_path = os.path.join(target_dir, "CMakeLists.txt")
    if not os.path.exists(cmake_path):
        print(f"Error: CMakeLists.txt not found in {target_dir}")
        return

    with open(cmake_path, 'r') as f:
        content = f.read()
    content = content.replace("demo", new_name)
    with open(cmake_path, 'w') as f:
        f.write(content)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("type", choices=['c', 'q'], help="Project type: c(cpp) or q(qt)")
    parser.add_argument("target_name", help="New project directory name")
    args = parser.parse_args()

    base_path = "/home/sun/project"
    source_map = {
        'c': os.path.join(base_path, "cpp", "cpp-demo"),
        'q': os.path.join(base_path, "qt", "qt-demo")
    }
    target_parent = os.path.join(base_path, "cpp" if args.type == 'c' else "qt")
    target_dir = os.path.join(target_parent, args.target_name)

    if not os.path.exists(source_map[args.type]):
        print(f"Error: Source directory {source_map[args.type]} does not exist")
        return

    if os.path.exists(target_dir):
        print(f"Error: Target directory {target_dir} already exists")
        return

    shutil.copytree(source_map[args.type], target_dir)
    replace_demo_in_cmake(target_dir, args.target_name)
    print(f"Project copied to {target_dir} and CMakeLists.txt updated")

if __name__ == "__main__":
    main()

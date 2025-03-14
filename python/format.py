#!/usr/bin/env/python3
import os
import subprocess
import argparse
import sys

def find_files(root_dir, extensions):
    """
    在指定目录及其子目录中查找具有特定扩展名的文件。
    只遍历根目录下的第一层子目录，以及名为 'src' 的子目录（递归）。
    Args:
        root_dir: 要搜索的根目录。
        extensions: 要查找的文件扩展名列表（例如：['.h', '.cpp']）。
    Returns:
        一个包含所有匹配文件路径的列表。
    """
    found_files = []
    
    # 处理根目录下的文件
    for filename in os.listdir(root_dir):
        filepath = os.path.join(root_dir, filename)
        if os.path.isfile(filepath) and any(filename.endswith(ext) for ext in extensions):
            found_files.append(filepath)
        elif os.path.isdir(filepath) and 'src' == filename:
            for src_dirpath, _, src_filenames in os.walk(filepath):  # 递归遍历 src
                    for src_filename in src_filenames:
                        if any(src_filename.endswith(ext) for ext in extensions):
                            found_files.append(os.path.join(src_dirpath, src_filename))

    return found_files


def format_files(files, clang_format_path, config_file):
    """
    使用 clang-format 格式化文件列表。

    Args:
        files: 要格式化的文件路径列表。
        clang_format_path: clang-format 可执行文件的路径。
        config_file: .clang-format 配置文件的路径。
    """
    for file_path in files:
        try:
            command = [clang_format_path, "-i", "-style=file:" + config_file, file_path]
            subprocess.run(command, check=True, capture_output=True, text=True)
            print(f"Formatted: {file_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error formatting {file_path}:")
            print(e.stderr)
        except FileNotFoundError:
            print(f"Error: clang-format not found at {clang_format_path}.  Please ensure it's installed and in your PATH, or provide the full path.")
            sys.exit(1)

def main():
    """
    主函数，解析命令行参数并执行格式化。
    """
    parser = argparse.ArgumentParser(description="Format C++ files using clang-format.")
    parser.add_argument("directory", nargs='?', default=os.getcwd(),
                        help="The directory to format (defaults to current directory).")
    parser.add_argument("--clang-format", default="clang-format",
                        help="Path to the clang-format executable (defaults to 'clang-format').")
    parser.add_argument("--config", default="~/.clang-format",
                        help="Path to the .clang-format config file (defaults to '~/.clang-format').")
    args = parser.parse_args()

    target_directory = os.path.abspath(args.directory)  # 获取绝对路径
    clang_format_path = args.clang_format
    config_file = os.path.expanduser(args.config) # 展开~

    if not os.path.exists(target_directory):
        print(f"Error: Directory '{target_directory}' does not exist.")
        sys.exit(1)
    if not os.path.isfile(config_file):
        print(f"Error: .clang-format file '{config_file}' not found. Using LLVM style.")
        config_file = "LLVM" #如果找不到配置文件，就用LLVM


    extensions = ['.h', '.hpp', '.cpp']
    files_to_format = find_files(target_directory, extensions)

    if not files_to_format:
        print(f"No files with extensions {extensions} found in '{target_directory}' or its 'src' subdirectories.")
        sys.exit(0)

    format_files(files_to_format, clang_format_path, config_file)


if __name__ == "__main__":
    main()



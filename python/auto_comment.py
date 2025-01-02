import os


def process_file(file_path, encoding="utf-8"):
    with open(file_path, "r", encoding=encoding) as f:
        content = f.read()
    content = content.replace(
        "{\n",
        "{\n\t/*\n\t * Start of Implement, this method is use for calculating...\n\t * function body, logic code, etc.\n\t * End of Implement\n\t */\n",
    )
    with open(file_path, "w", encoding=encoding) as f:
        f.write(content)


def process_cpp_files(folder_path):
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".cpp"):
                    file_path = os.path.join(root, file)
                    try:
                        process_file(file_path)
                    except Exception as e:
                        try:
                            process_file(file_path, encoding="gbk")
                        except Exception as e:
                            print(e)
    except Exception as e:
        print(e)


# 将"/home/szzh/code"改为要处理的代码的根目录
# 然后终端运行 python auto_comment.py 或者 python3 auto_comment.py
if __name__ == "__main__":
    folder_path = "/home/szzh/code"
    process_cpp_files(folder_path)

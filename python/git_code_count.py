import subprocess
import datetime
import argparse
import os

def get_code_stats(repo_path, author="wangbinio", start_date=None, end_date=None):
    """
    统计一段时间内某个提交者在指定 Git 仓库中提交的代码行数。

    Args:
        repo_path (str): Git 仓库的目录.
        author (str): 作者姓名. Defaults to "wangbinio".
        start_date (str, optional): 开始日期 (YYYY-MM-DD). Defaults to 一周之前.
        end_date (str, optional): 结束日期 (YYYY-MM-DD). Defaults to 明天.
    """

    if not os.path.isdir(repo_path):
        print(f"Error: Invalid repository path: {repo_path}")
        return

    if start_date is None:
        start_date = (datetime.date.today() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    if end_date is None:
        end_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    command = [
        "git",
        "log",
        f"--author={author}",
        f"--since={start_date}",
        f"--until={end_date}",
        "--pretty=tformat:",
        "--numstat",
    ]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, cwd=repo_path)
        output = result.stdout

        added_lines = 0
        removed_lines = 0
        for line in output.splitlines():
            if not line.strip():  # Skip empty lines
                continue
            parts = line.split()
            if len(parts) >= 3 and parts[0].isdigit() and parts[1].isdigit():
                added_lines += int(parts[0])
                removed_lines += int(parts[1])

        total_lines = added_lines - removed_lines
        print(f"Repository Path: {repo_path}")
        print(f"Author: {author}")
        print(f"Start Date: {start_date}")
        print(f"End Date: {end_date}")
        print(f"Added lines: {added_lines}")
        print(f"Removed lines: {removed_lines}")
        print(f"Total lines: {total_lines}")

    except subprocess.CalledProcessError as e:
        print(f"Error executing git command: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="统计 Git 代码行数.")
    parser.add_argument("repo_path", help="Git 仓库的目录") # 必须参数
    parser.add_argument("--author", default="wangbinio", help="作者姓名")
    parser.add_argument("--start_date", help="开始日期 (YYYY-MM-DD), 默认为一周前")
    parser.add_argument("--end_date", help="结束日期 (YYYY-MM-DD), 默认为明天")

    args = parser.parse_args()

    get_code_stats(args.repo_path, author=args.author, start_date=args.start_date, end_date=args.end_date)

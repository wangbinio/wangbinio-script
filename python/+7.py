import re

# 读取文件
with open('战斗分队要点夺控行动-原.mission', 'r', encoding='utf-8',  errors='replace') as file:
    content = file.read()

# 使用正则表达式查找并替换
def replace_match(match):
    original_number = int(match.group(1))
    if original_number >= 9:
        return f'class_id="{original_number + 7}"'
    else:
        return f'class_id="{original_number}"'

updated_content = re.sub(r'class_id="(\d+)"', replace_match, content)

# 写入更新后的内容到文件
with open('yourfile.mission', 'w', encoding='utf-8') as file:
    file.write(updated_content)

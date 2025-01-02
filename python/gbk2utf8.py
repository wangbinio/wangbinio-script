import os
import argparse


def gbk2utf8(file):
    """read gbk file, ignore errors, then save in utf-8"""
    try:
        with open(file, 'r', encoding='gbk') as f:
            f.read()
    except UnicodeDecodeError:
        print(f'{file} seens not gbk encoded!!!')
        return False
    with open(file, 'rb') as f:
        content = f.read().decode('gbk', errors='ignore')
    with open(file, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
        return True
        

def trans_dir_files(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            # if file.endswith('.h') or file.endswith('.cpp'):
            if gbk2utf8(os.path.join(root, file)):
                print(f'convert {file} to utf-8')
                
                
if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='Convert gbk file to utf-8')
    parse.add_argument('directory', help='directory to convert')
    
    args = parse.parse_args()
    
    trans_dir_files(args.directory)
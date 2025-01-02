import os
import argparse


def replace_content(file, old, new):
    with open(file, 'r', encoding='utf8') as f:
        content = f.read()
    with open(file, "w", encoding='utf8') as f:
        f.write(content.replace(old, new))
  
        
def replace_path_files(path, old, new):
    for root, dir, files in os.walk(path):
        for file in files:
            file_name = os.path.join(root, file)
            new_file_name = os.path.join(root, file.replace(old, new))
            print(file_name)
            replace_content(file_name, old, new)
            os.rename(file_name, new_file_name)
   
            
if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='Replace strings in file')
    parse.add_argument('directory', type=str)
    parse.add_argument('old_str', type=str)
    parse.add_argument('new_str', type=str)
    
    args = parse.parse_args()
    print(args)
    
    replace_path_files(args.directory, args.old_str, args.new_str)
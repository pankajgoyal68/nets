import os
import shutil


source_dir = "/Users/localadmin/nets_project/source/"
dest_dir = "/Users/localadmin/nets_project/failure/"


for top, dirs, files in  os.walk(source_dir):
    for filename in files:
        if filename.endswith('.txt'):
            continue
        file_path = os.path.join(top, filename)
        with open(file_path, 'r') as f:
            if '* Test Outcome : failure' in f.read():
                shutil.move(file_path, os.path.join(dest_dir, filename))

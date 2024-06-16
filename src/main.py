import os
import shutil
def recursive_file_copy(source_path, target_path):
    if os.path.exists(target_path):
        shutil.rmtree(target_path)
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    source_items = os.listdir(source_path)
    for item in source_items:
        path = os.path.join(source_path, item)
        if os.path.isfile(path):
            shutil.copy2(path, os.path.join(target_path, item))
        elif os.path.isdir(path):
            recursive_file_copy(path, os.path.join(target_path, item))

def main():
    recursive_file_copy('../static', "../target_directory")
    


main()

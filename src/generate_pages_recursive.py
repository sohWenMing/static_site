from generate_page import generate_page
import os
import shutil
import re

def generate_pages_recursive(source_path, template_path, target_path):
    if os.path.exists(target_path):
        shutil.rmtree(target_path)
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    source_items = os.listdir(source_path)
    for item in source_items:
        path = os.path.join(source_path, item)
        if os.path.isfile(path):
            split = os.path.split(path)
            html_filename = re.sub(r"md", "html", split[1])
            generate_page(f"{source_path}/{split[1]}", template_path, f"{target_path}/{html_filename}")
        elif os.path.isdir(path):
            generate_pages_recursive(path, template_path, f"{target_path}/{item}")
            
        #     shutil.copy2(path, os.path.join(target_path, item))
        # elif os.path.isdir(path):
        #     recursive_file_copy(path, os.path.join(target_path, item))


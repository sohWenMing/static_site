import re
from markdown_to_html_node import markdown_to_htmlnode
import os

def extract_title(markdown):
    #the markdown passed in will already be a open file
    title_line = None
    for line in markdown:
        if re.search(r"^# .*", line):
            title_line = line
            break
    if title_line == None:
        raise Exception("Markdown must have a h1 title")
    title_line = re.sub(r"^# ", "", title_line)
    return title_line
       
        

def generate_page(read_path, template_path, dest_path):
    markdown_lines = []
    markdown_data = ""
    template_data = ""
    with open(read_path) as markdown:
        markdown_lines = markdown.readlines()
        markdown.seek(0)
        markdown_data = markdown.read()
    with open(template_path) as template:
        template_data = template.read()
    title_line = extract_title(markdown_lines)
    content = markdown_to_htmlnode(markdown_data).to_html()
    template_data = re.sub(r"{{ Title }}", title_line, template_data)
    template_data = re.sub(r"{{ Content }}", content, template_data)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as file:
        file.write(template_data)
    
    


import os
import shutil
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive

def main():
    # recursive_file_copy('../static', "../target_directory")
    generate_pages_recursive("./content", "./template.html", "./public")
    
main()

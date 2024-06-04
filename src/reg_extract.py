import re

def reg_findall(regex):
    def wrapper(text):
        return re.findall(regex, text)
    return wrapper

def check_string(text):
    if not isinstance(text, str):
        raise ValueError(f"{text} is not a string")

def extract_markdown_images(text):
    check_string(text)
    return reg_findall(r"!\[(.*?)\]\((.*?)\)")(text)

def extract_markdown_links(text):
    check_string(text)
    return reg_findall(r"(?<!!)\[(.*?)\]\((.*?)\)")(text)



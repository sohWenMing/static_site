import re
from htmlnode import ParentNode
from split_node import text_to_textnodes


def heading_to_htmlnode(string):
    regex = r"^\#{1,6} "
    cleaned_string = re.sub(regex, "", string)
    children = text_to_textnodes(cleaned_string)
    textnodes_to_html_nodes = []
    for child in children:
        textnodes_to_html_nodes.append(child.text_node_to_html_node())
    node = ParentNode("heading", textnodes_to_html_nodes)
    return node

def quote_to_htmlnode(string):
    lines = string.split("\n")
    cleaned_lines = []
    for line in lines:
        cleaned_lines.append(line[1:].strip())
    blockquote = text_to_textnodes("<br>".join(cleaned_lines))
    textnodes_to_html_nodes = []
    for quote in blockquote:
        textnodes_to_html_nodes.append(quote.text_node_to_html_node())
    node = ParentNode("blockquote", textnodes_to_html_nodes)
    return node

def unordered_list_to_htmlnode(string):
    lines = string.split("\n")
    cleaned_lines = []
    for line in lines:
        cleaned_lines.append(f"<li>{line[2:].strip()}</li>")
    unordered_text_line = "".join(cleaned_lines)
    children = text_to_textnodes(unordered_text_line)
    textnodes_to_html_nodes = []
    for child in children:
        textnodes_to_html_nodes.append(child.text_node_to_html_node())
    node = ParentNode("ul", textnodes_to_html_nodes)
    return node

def ordered_list_to_htmlnode(string):
    lines = string.split("\n")
    cleaned_lines = []
    for line in lines:
        cleaned_lines.append(f"<li>{line[2:].strip()}</li>")
    ordered_text_line = "".join(cleaned_lines)
    children = text_to_textnodes(ordered_text_line)
    textnodes_to_html_nodes = []
    for child in children:
        textnodes_to_html_nodes.append(child.text_node_to_html_node())
    node = ParentNode("ol", textnodes_to_html_nodes)
    return node

def code_to_htmlnode(string):
    lines = string.split("\n")
    cleaned_lines = []
    for line in lines:
        cleaned_line_front = re.sub(r"^```", "", line)
        full_cleaned_line = re.sub(r"```$", "", cleaned_line_front)
        cleaned_lines.append(full_cleaned_line)
    children = text_to_textnodes("\n".join(cleaned_lines))
    textnodes_to_html_nodes = []
    for child in children:
        textnodes_to_html_nodes.append(child.text_node_to_html_node())
    code_node = ParentNode("code", textnodes_to_html_nodes)
    pre_code_node = ParentNode("pre", [code_node])
    print(pre_code_node.to_html())

def heading_to_htmlnode(string):
    heading = re.findall(r"^#{1,6}", string)
    heading_number = len(heading[0])
    tag = f"h{heading_number}"
    cleaned_string = re.sub(r"^#{1,6}", "", string)
    children = text_to_textnodes(cleaned_string)
    textnodes_to_html_nodes = []
    for child in children:
        textnodes_to_html_nodes.append(child.text_node_to_html_node())
    node = ParentNode(tag, textnodes_to_html_nodes)
    return node
        
def paragraph_to_htmlnode(string):
    children = text_to_textnodes(string)
    textnodes_to_html_nodes = []
    for child in children:
        textnodes_to_html_nodes.append(child.text_node_to_html_node())
    node = ParentNode("p", textnodes_to_html_nodes)
    return node

string = "this is a paragraph"

print(paragraph_to_htmlnode(string).to_html())

    
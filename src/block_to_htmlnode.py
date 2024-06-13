import re
from htmlnode import ParentNode
from textnode import TextNode
from split_node import text_to_textnodes
def heading_to_htmlnode(string):
    regex = r"^\#{1,6} "
    cleaned_string = re.sub(regex, "", string)
    children = text_to_textnodes(cleaned_string)
    print("children", children)
    textnodes_to_html_nodes = []
    for child in children:
        textnodes_to_html_nodes.append(child.text_node_to_html_node())
    print(textnodes_to_html_nodes)
    node = ParentNode("blockquote", textnodes_to_html_nodes)
    return node

heading = heading_to_htmlnode("### **string** ![image](Some stuff) *italics*")
print(heading.to_html())



    
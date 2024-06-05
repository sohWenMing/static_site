from textnode import TextNode
from htmlnode import ParentNode
from reg_extract import extract_markdown_images, extract_markdown_links

delimiter_to_type = {
    "**": "bold",
    "*": "italic",
    "`": "code"
}

def flatten_array(array):
    flat_array = []
    for value in array:
        if isinstance(value, list):
            flat_array.extend(flatten_array(value))
        else: 
            flat_array.append(value)
    return flat_array

def split_nodes_text(node, delimiter):
    split_list = node.text.split(delimiter)
    if len(split_list) % 2 == 0:
        raise Exception("Invalid markdown syntax")
    for i in range(0, len(split_list)):
        if i % 2 != 0:
            split_list[i] = TextNode(split_list[i], delimiter_to_type[delimiter])
        else:
            if split_list[i] == " " or split_list[i] == "":
                split_list[i] = TextNode(split_list[i], "text")
            else:
                if delimiter == "**":
                    split_list[i] = split_nodes_text(TextNode(split_list[i], "text"), "*")
                if delimiter == "*":
                    split_list[i] = split_nodes_text(TextNode(split_list[i], "text"), "`")
                if delimiter == "`":
                    split_list[i] = TextNode(split_list[i], "text")
    flattened_array = flatten_array(split_list)
    return flattened_array

def get_textnode_list(node):
    flattened_array = split_nodes_text(node, "**")
    for i in range(0, len(flattened_array)):
        if flattened_array[i].text == " ":
            flattened_array[i+1].text = flattened_array[i].text + flattened_array[i+1].text
    returned_array = list(filter(lambda x: x.text !="" and x.text!=" ", flattened_array))
    return returned_array

def split_nodes_delimiter(old_nodes):
    returned_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode) == False:
            returned_nodes.append(node)
        else:
            returned_nodes.extend(get_textnode_list(node))
    return returned_nodes

def split_nodes_image(old_nodes):
    print("Old nodes: ", old_nodes)
    returned_nodes = []
    for value in old_nodes:
        if not isinstance(value, TextNode):
            returned_nodes.append(value)
        else:
            extracted_tups = extract_markdown_images(value.text)
            if len(extracted_tups) == 0:
                # this would mean that the regex couldn't find anymore
                returned_nodes.append(value)
            else:
                tuple = extracted_tups[0]
                tup_delimiter = f"![{tuple[0]}]({tuple[1]})"
                text_split = value.text.split(tup_delimiter, 1)
                if text_split[0] == "":
                    returned_nodes.append(TextNode(tuple[1], "image"))
                else:
                    returned_nodes.append(TextNode(text_split[0], "text"))
                    returned_nodes.append(TextNode(tuple[1], "image"))
                if text_split[1] != "":
                    returned_nodes.extend(flatten_array(split_nodes_image([TextNode(text_split[1], "text")])))
    return returned_nodes
    
    

node = TextNode(
    "##Test text## ![image](http://www.google.com/image1.jpg) ##Here is some test text## ![another](http://www.google.com/image2.jpg) ##more text## ___", "text")
parentNode = ParentNode("div", [node], None)

print(split_nodes_image([node, parentNode]))



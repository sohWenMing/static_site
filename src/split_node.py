from textnode import TextNode
from htmlnode import ParentNode
from reg_extract import extract_markdown_images, extract_markdown_links
from node_functions.helpers import get_func_name, flatten_array
####################HELPERS##################
delimiter_to_type = {
    "**": "bold",
    "*": "italic",
    "`": "code"
}

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

def get_tuple_delimiter(extractor, tup_index_1, tup_index_2):
    extractor_name = get_func_name(extractor)
    if extractor_name != "extract_markdown_images" and extractor_name != "extract_markdown_links":
        raise Exception("Extractor must be \"extract_markdown_images\" or \"extract_markdown_links\"")
    if extractor_name == "extract_markdown_images":
        return extractor_name, f"![{tup_index_1}]({tup_index_2})"
    return extractor_name, f"[{tup_index_1}]({tup_index_2})"

def get_tag(extractor_name):
    if extractor_name != "extract_markdown_images" and extractor_name != "extract_markdown_links":
        raise Exception("Extractor must be \"extract_markdown_images\" or \"extract_markdown_links\"")
    return "image" if extractor_name == "extract_markdown_images" else "link"

def split_nodes_image_or_links(old_nodes, extractor):
    extractor_name = get_func_name(extractor)
    tag = get_tag(extractor_name)
    returned_nodes = []
    for value in old_nodes:
        if not isinstance(value, TextNode):
            returned_nodes.append(value)
        else:
            extracted_tups = extractor(value.text)
            if len(extracted_tups) == 0:
                # this would mean that the regex couldn't find anymore
                returned_nodes.append(value)
            else:
                tuple = extracted_tups[0]
                extractor_name, tup_delimiter = get_tuple_delimiter(extractor, tuple[0], tuple[1])
                text_split = value.text.split(tup_delimiter, 1)
                # print("text split: ", text_split)
                if text_split[0] == "":
                    returned_nodes.append(TextNode(tuple[0], tag, tuple[1]))
                        
                else:
                    returned_nodes.append(TextNode(text_split[0], "text"))
                    returned_nodes.append(TextNode(tuple[0], tag, tuple[1]))

                    
                if len(text_split) > 1:
                    # print("text after split: ", text_split)
                    if text_split[1] != "":
                        returned_nodes.extend(flatten_array(split_nodes_image_or_links([TextNode(text_split[1], "text")], extractor)))
    return returned_nodes
####################HELPERS###################

####################FUNCTION EXPORTS##########
def split_nodes_delimiter(old_nodes):
    returned_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode) == False:
            returned_nodes.append(node)
        else:
            returned_nodes.extend(get_textnode_list(node))
    return returned_nodes

def split_node_images(old_nodes):
    return split_nodes_image_or_links(old_nodes, extract_markdown_images)

def split_node_links(old_nodes):
    return split_nodes_image_or_links(old_nodes, extract_markdown_links)

def text_to_textnodes(text):
    textnode = TextNode(text, "text")
    nodes = split_node_links(split_node_images(split_nodes_delimiter([textnode])))
    return nodes
    
    
 
from markdown_to_block import markdown_to_blocks, block_to_block_type
from block_to_htmlnode import (heading_to_htmlnode, quote_to_htmlnode, 
                               unordered_list_to_htmlnode, 
                               ordered_list_to_htmlnode, code_to_htmlnode, 
                               heading_to_htmlnode, paragraph_to_htmlnode)
from htmlnode import ParentNode

def markdown_to_htmlnode(markdown):
    blocks_list = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks_list:
        block_type = block_to_block_type(block)
        if block_type == "paragraph":  
            block_nodes.append(paragraph_to_htmlnode(block))
        elif block_type == "heading":
            block_nodes.append(heading_to_htmlnode(block))
        elif block_type == "code":
            block_nodes.append(code_to_htmlnode(block))
        elif block_type == "quote":
            block_nodes.append(quote_to_htmlnode(block))
        elif block_type == "unordered_list":
            block_nodes.append(unordered_list_to_htmlnode(block))
        elif block_type == "ordered_list":
            block_nodes.append(ordered_list_to_htmlnode(block))
    node = ParentNode("div", block_nodes)
    return node
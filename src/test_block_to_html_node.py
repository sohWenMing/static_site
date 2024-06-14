import unittest
from block_to_htmlnode import heading_to_htmlnode, quote_to_htmlnode
from htmlnode import ParentNode
from textnode import TextNode
import pprint
from split_node import text_to_textnodes
from bs4 import BeautifulSoup

def parse_html(html):
    return BeautifulSoup(html, 'html.parser')

def generate_heading_string(num_hex):
    heading_string = ""
    for i in range(0, num_hex):
        heading_string += "#"
    return heading_string

bold_string = "**bold string**"
italic_string = "*italic string*"
image_string = "![alt-text](http://url.com)"
link_string = "[link-text](http://this-is-a-link.com)"
code_string = r"`print(hello world!)`"

bold_textnode = TextNode("bold string", "bold")
bold_htmlnode = bold_textnode.text_node_to_html_node()
italic_textnode = TextNode("italic string", "italic")
italic_htmlnode = italic_textnode.text_node_to_html_node()
image_textnode = TextNode("alt-text", "image", "http://url.com")
image_htmlnode = image_textnode.text_node_to_html_node()
link_textnode = TextNode("link-text", "link", "http://this-is-a-link.com")
link_htmlnode = link_textnode.text_node_to_html_node()
code_textnode = TextNode("print(hello world!)", "code")
code_htmlnode = code_textnode.text_node_to_html_node()
space_textnode = TextNode(" ", "text")
space_htmlnode = space_textnode.text_node_to_html_node()

test_heading = f"{generate_heading_string(3)} {bold_string}"
test_heading_complex = f"{generate_heading_string(3)} {bold_string} {italic_string}{image_string}{link_string}{code_string}"

class TestBlockToHTMLNode(unittest.TestCase):
    def test_heading_basic(self):
        node = heading_to_htmlnode(test_heading)
        test_node = ParentNode("heading", [bold_htmlnode])
        self.assertEqual(node, test_node)
    def test_heading_complex(self):
        node = heading_to_htmlnode(test_heading_complex)
        test_node = ParentNode("heading", [bold_htmlnode, space_htmlnode, italic_htmlnode, image_htmlnode, link_htmlnode, code_htmlnode])
        # self.assertEqual(node.to_html(), test_node.to_html())   
        generated_html = parse_html(node.to_html())
        expected_html = parse_html(test_node.to_html()) 
    def test_blockquote(self):
        node = quote_to_htmlnode(">line1\n>line2\n>line3")
        self.assertEqual(node.to_html(), "<blockquote>line1<br>line2<br>line3</blockquote>")

        

        
    
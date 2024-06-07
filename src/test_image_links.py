from test_helpers.test_helpers import printToIO
from split_node import split_node_images, split_node_links
import unittest
from textnode import TextNode
from htmlnode import ParentNode
from node_functions.helpers import flatten_array

text_no_space = "text no space"
text_leading_space = " text leading space"
text_trailing_space = "text trailing space "
text_both_space = " text both space "
image_text = "![alt-text](http://www.google.com/jpeg1)"
link_text = "[description of link](http://www.google.com)"

text_tests = [text_no_space, text_leading_space, text_trailing_space, text_both_space]
text_test_tuples = [
    (text_no_space, text_leading_space),
    (text_leading_space, text_trailing_space),
    (text_trailing_space, text_both_space),
    (text_both_space, text_no_space)
]

textnode_no_tags = TextNode(text_no_space + text_leading_space + text_trailing_space, "text")
textnode_no_space = TextNode(text_no_space, "text")
textnode_leading_space = TextNode(text_leading_space, "text")
textnode_trailing_space = TextNode(text_trailing_space, "text")
textnode_both_space = TextNode(text_both_space, "text")

image_text_node = TextNode(image_text, "text")
image_test_textnode = TextNode("alt-text", "image", "http://www.google.com/jpeg1")

link_text_node = TextNode(link_text, "text")
link_test_textnode = TextNode("description of link", "link", "http://www.google.com")

def generate_middle_tag_nodes(node_text):
    nodes = []
    for tuple in text_test_tuples:
        nodes.append(TextNode(tuple[0] + node_text + tuple[1], "text"))
    return nodes

def generate_nested_node_tag_leading(textnode):
    def wrapper(node_text):
        nodes = [textnode]
        nodes.extend(generate_middle_tag_nodes(node_text))
        return nodes
    return wrapper



def get_nodes_one_textnode(textinput, split_function):
    test_textnode = TextNode(textinput, "text")
    nodes = split_function([test_textnode])
    return nodes

def get_nodes_multiple_nodes(list, split_function):
    returned_nodes = []
    for item in list:
        returned_nodes.extend(split_function([item]))
    return returned_nodes


class ImageLinksTest(unittest.TestCase):
    def test_no_image(self): 
        nodes = split_node_images([textnode_no_tags])
        self.assertEqual(nodes, [textnode_no_tags])

    def test_no_link(self):
        nodes = split_node_links([textnode_no_tags])
        self.assertEqual(nodes, [textnode_no_tags])

    def test_one_image(self):
        nodes = split_node_images([image_text_node])
        self.assertEqual(nodes, [image_test_textnode])

    def test_one_link(self):
        nodes = split_node_links([link_text_node])
        self.assertEqual(nodes, [link_test_textnode])

    def test_image_front(self):
        for text in text_tests:
            nodes = get_nodes_one_textnode(image_text + text, split_node_images)
            self.assertEqual(nodes, [image_test_textnode, TextNode(text, "text")])
    
    def test_image_back(self):
        for text in text_tests:
            nodes = get_nodes_one_textnode(text + image_text, split_node_images)
            self.assertEqual(nodes, [TextNode(text, "text"), image_test_textnode])
    
    def test_image_middle(self):
        for tuple in text_test_tuples:
            nodes = get_nodes_one_textnode(tuple[0] + image_text + tuple[1], split_node_images)
            self.assertEqual(nodes, [TextNode(tuple[0], "text"), image_test_textnode, TextNode(tuple[1], "text")])
    
    def test_two_textnode_images(self):
        list = [image_text_node, image_text_node]
        nodes = get_nodes_multiple_nodes(list, split_node_images)
        self.assertEqual(nodes, [image_test_textnode, image_test_textnode])
    
    def test_textnode_front_image_textnode_end(self):
        list = [textnode_no_tags, image_test_textnode]
        nodes = get_nodes_multiple_nodes(list, split_node_images)
        self.assertEqual(nodes, [textnode_no_tags, image_test_textnode])

    def test(self):
        nodes = generate_nested_node_tag_leading(textnode_no_tags)(image_text)
        print(nodes)
        cleaned_nodes = get_nodes_multiple_nodes(nodes, split_node_images)
        expected = [textnode_no_tags]
        for tuple in text_test_tuples:
            text_nodes = []
            text_nodes.append(TextNode(tuple[0], "text"))
            text_nodes.append(image_test_textnode)
            text_nodes.append(TextNode(tuple[1], "text"))
            expected.extend(text_nodes)
        self.assertEqual(cleaned_nodes, expected)
        

    
        
        
        
import unittest

from split_node import split_nodes_delimiter, split_node_links, split_node_images
from textnode import TextNode

test_string = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"

test_textnode = TextNode(test_string, "text")
class FullSplitTest(unittest.TestCase):
    def test_full_string(self):
        nodes = split_node_links(split_node_images(split_nodes_delimiter([test_textnode])))
        self.assertEqual(nodes, [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev"),
        ])
        
        
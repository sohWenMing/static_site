import unittest
from textnode import TextNode
from htmlnode import ParentNode, LeafNode
from split_node_delimiter import split_nodes_delimiter

textnode_right_delimiters = TextNode("`This` **should** *be* correct.", "text")
textnode_another_right_delimiters = TextNode("The *quick* **brown** `fox` jumped over the `lazy` dog.", "text")
textnode_wrong_delimiters = TextNode("*But **THis** should be `absolutely* wrong", "text")
leafnode_link = LeafNode("a", textnode_right_delimiters, {"href": "http://www.google.com"})
class TestSplitNodeDelimiter(unittest.TestCase):
    def test_wrong_delimiter(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter[textnode_wrong_delimiters]
    def test_right_delimiter(self):
        split = split_nodes_delimiter([textnode_right_delimiters])
        self.assertEqual(split, [TextNode("This", "code", None), 
                                 TextNode(" should", "bold", None), 
                                 TextNode(" be", "italic", None), 
                                 TextNode(" correct.", "text", None)])
    def test_multiple_text_nodes(self):
        split = split_nodes_delimiter([textnode_right_delimiters, textnode_another_right_delimiters])
        self.assertEqual(split, [TextNode("This", "code", None),
                                  TextNode(" should", "bold", None),
                                  TextNode(" be", "italic", None),
                                  TextNode(" correct.", "text", None),
                                  TextNode("The ", "text", None),
                                  TextNode("quick", "italic", None),
                                  TextNode(" brown", "bold", None),
                                  TextNode(" fox", "code", None),
                                  TextNode(" jumped over the ", "text", None),
                                  TextNode("lazy", "code", None),
                                  TextNode( " dog.", "text", None)
                                  ])
    
    def test_different_nodes(self):
        split = split_nodes_delimiter([textnode_right_delimiters, leafnode_link])
        print(split)
        
    
    


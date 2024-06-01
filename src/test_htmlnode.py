import unittest
from io import StringIO
import sys 
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode

def create_one_leaf_no_tag():
    leafnode = LeafNode(None, "this is a div", None)
    return leafnode

def create_one_leaf_one_prop():
    leafnode = LeafNode("div", "this is a div", {"class": "test-div"})
    return leafnode

def create_one_leaf_mult_props():
    leafnode = LeafNode("div", "this is a div", {"class": "test-div", "alt": "some-image"})
    return leafnode

def create_one_parent_one_leaf():
     parent_node = ParentNode("div", [create_one_leaf_no_tag()])
     return parent_node

def create_one_parent_two_leaf():
    parent_node = ParentNode("div", [
                       create_one_leaf_one_prop(), 
                       create_one_leaf_mult_props()])
    return parent_node

def create_nested_parent():
    parent_node = ParentNode("div", [create_one_parent_one_leaf()])
    return parent_node

def printToIO(node):
    original_stdout = sys.stdout 
    captured_output = StringIO()
    try:
        sys.stdout = captured_output
        print(node)
        printed_output = captured_output.getvalue().strip()
    finally:
        sys.stdout = original_stdout
    return printed_output

wrong_text_types = [None, "", "href"]
upper_text_types = ["TEXT", "BOLD", "ITALIC", "CODE", "LINK", "IMAGE"]

def create_test_textnode_by_type(text_type):
    textnode = TextNode("This is a test text node", text_type, None)
    return textnode

def create_test_textnode_link():
    textnode = TextNode("This is a link test node", "link", "www.google.com")
    return textnode

def create_test_textnode_image():
    textnode = TextNode("This is the alt text", "image", "http://i-died-at-your=house.com/img-1")
    return textnode

class TestHTMLNode(unittest.TestCase):
    def test_print(self):
        node = HTMLNode("<div>", "test value", None, None)
        printed_output = printToIO(node)
        expected_output =  "Tag: <div> Value: test value Children: [] Props: {}"
        self.assertEqual(printed_output, expected_output)

    def test_props(self):
        second_node = HTMLNode("<div>", "test value", None, {"alt": "image"})
        printed_output = printToIO(second_node)
        expected_output = "Tag: <div> Value: test value Children: [] Props: {'alt': 'image'}"
        self.assertEqual(printed_output, expected_output)

    def test_children(self):
        child_node_one = HTMLNode("<div>", "test value", None, None)
        child_node_two = HTMLNode("<span>", "another test value", None, None)
        parent_node = HTMLNode("<div>", "test value", [child_node_one, child_node_two], None)
        self.assertEqual(len(parent_node.children), 2)
        self.assertEqual(parent_node.children, [child_node_one, child_node_two])
      
    def test_leafnode_no_tag(self):
        leafnode_html = create_one_leaf_no_tag().to_html()
        expected_value = "this is a div"
        self.assertEqual(leafnode_html, expected_value)
    
    def test_leafnode_one_prop(self):
        leafnode_html = create_one_leaf_one_prop().to_html()
        expected_value = "<div class=\"test-div\">this is a div</div>"
        self.assertEqual(leafnode_html, expected_value)
    
    def test_leafnode_multiple_props(self):
        leafnode_html = create_one_leaf_mult_props().to_html()
        expected_value = "<div class=\"test-div\" alt=\"some-image\">this is a div</div>"
        self.assertEqual(leafnode_html, expected_value)

    def test_parentnode_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [create_one_leaf_no_tag()])
    
    def test_parentnode_children_none(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)
    
    def test_parentnode_children_empty(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])
    
    def test_parentnode_one_leaf_child(self):
        parent_node = create_one_parent_one_leaf()
        to_html = parent_node.to_html()
        self.assertEqual(to_html, "<div>this is a div</div>")

    def test_parentnode_two_leaf_children(self):
        parent_node = create_one_parent_two_leaf()
        to_html = parent_node.to_html()
        expected_output = (
            "<div>"
                "<div class=\"test-div\">this is a div</div>"
                "<div class=\"test-div\" alt=\"some-image\">this is a div</div>"
            "</div>"
        )
        self.assertEqual(to_html, expected_output)

    def test_parentnode_one_parent_node_one_leaf_child(self):
        parent_node = ParentNode("div", [create_one_parent_one_leaf(), create_one_parent_one_leaf()])
        to_html = parent_node.to_html()
        self.assertEqual(to_html, "<div><div>this is a div</div><div>this is a div</div></div>")

    def test_nested_parent(self):
        parent_node = ParentNode("div", [create_nested_parent(), create_nested_parent()])
        to_html = parent_node.to_html()
        self.assertEqual(to_html, "<div><div><div>this is a div</div></div><div><div>this is a div</div></div></div>")
   
    def test_text_node_to_html_exceptions(self):
       for type in wrong_text_types:
           with self.assertRaises(Exception):
               text_node_to_html_node(create_test_textnode_by_type(type))
    
    def test_upper_text_types(self):
        for type in upper_text_types:
            create_test_textnode_by_type(type)

    def test_text_textnode(self):
        text_textnode_to_html = text_node_to_html_node((create_test_textnode_by_type("text"))).to_html()
        self.assertEqual(text_textnode_to_html, "This is a test text node")

    def test_bold_textnode(self):
        text_node_to_html = text_node_to_html_node(create_test_textnode_by_type("bold")).to_html()
        self.assertEqual(text_node_to_html, "<b>This is a test text node</b>")

    def test_bold_textnode(self):
        text_node_to_html = text_node_to_html_node(create_test_textnode_by_type("italic")).to_html()
        self.assertEqual(text_node_to_html, "<i>This is a test text node</i>")

    def test_bold_textnode(self):
        text_node_to_html = text_node_to_html_node(create_test_textnode_by_type("code")).to_html()
        self.assertEqual(text_node_to_html, "<code>This is a test text node</code>")
        test = text_node_to_html_node(create_test_textnode_by_type("code"))
    
    def test_link_textnode(self):
        text_node_to_html = text_node_to_html_node(create_test_textnode_link()).to_html()
        self.assertEqual(text_node_to_html, "<a href=\"www.google.com\">This is a link test node</a>")
    
    def test_image_textnode(self):
        text_node_to_html = text_node_to_html_node(create_test_textnode_image()).to_html()
        self.assertEqual(text_node_to_html, "<img src=\"http://i-died-at-your=house.com/img-1\" alt=\"This is the alt text\"></img>")


if __name__ == '__main__':
    unittest.main(buffer=False)


    

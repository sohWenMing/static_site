import unittest
from io import StringIO
import sys 
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    captured_output = StringIO()
    sys.stdout = captured_output
    print(node)
    printed_output = captured_output.getvalue().strip()
    return printed_output

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

    def test_leafnode_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("div", None, None)
     
    
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
   
                         


    

    
        
        

if __name__ == '__main__':
    unittest.main()


    

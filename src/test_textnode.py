import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_none(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("THis is a text node", "bold", None)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("THIS IS A TEXT NODE", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
if __name__ == "__main__":
    unittest.main()
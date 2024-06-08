import unittest
from markdown_to_block import markdown_to_block

heading = "# this is a heading"
paragraph = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
newline = "\n"
list_item = "* this is a list item"
space = "                                        "

class TestMarkDownToBlock(unittest.TestCase):
    def test_basic(self):
        test_text = heading + newline + newline + paragraph + newline + list_item + newline + list_item 
        result = markdown_to_block(test_text)
        self.assertEqual(result, [heading, paragraph, list_item, list_item])
    
    def test_exception(self):
        with self.assertRaises(ValueError):
            markdown_to_block(3)

    def test_basic(self):
        test_text = newline + newline
        result = markdown_to_block(test_text)
        self.assertEqual(result, [])
    
    def test_spaces(self):
        test_text = space + heading + space + newline + newline + paragraph
        result = markdown_to_block(test_text)
        self.assertEqual(result, [heading, paragraph])
    
    def test_nullspace(self):
        test_text = space + newline + space
        result = markdown_to_block(test_text)
        self.assertEqual(result, [])

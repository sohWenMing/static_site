import unittest
from markdown_to_block import markdown_to_block
import textwrap

heading = "# this is a heading"
paragraph = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
newline = "\n"
list_item = "* this is a list item"
space = "                     "
def print_result(result):
    for block in result:
        print('-' * 40)
        block_split_lines = block.split("\n")
        for line in block_split_lines:
            print(line)


class TestMarkDownToBlock(unittest.TestCase):
    def test_basic(self):
        test_text = heading + newline + newline + paragraph + newline + list_item + newline + list_item 
        result = markdown_to_block(test_text)
        # print_result(result)
        self.assertEqual(result, [heading, paragraph + newline + list_item + newline + list_item])
    
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

    def test_multiple_newlines(self):
        test_text = newline + heading + newline*40 + paragraph + newline + list_item + newline + list_item
        result = markdown_to_block(test_text)
        # print_result(result)
        self.assertEqual(result, [heading, paragraph + newline + list_item + newline + list_item])

    def test_from_boot_dev(self):
        markdown = textwrap.dedent("""
        This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
            This is the same paragraph on a new line             

        * This is a list
            * with items             
        """)

        result = markdown_to_block(markdown)
        self.assertEqual(result, ["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\n    This is the same paragraph on a new line", "* This is a list\n    * with items"])

    def test_mixed_elements(self):
        markdown = "# Heading\n\nParagraph with **bold** text.\n\n* List item 1\n\n* List item 2\n\nEnd paragraph with `code`.\nAnother line in the same paragraph."
        expected = [
            "# Heading",
            "Paragraph with **bold** text.",
            "* List item 1",
            "* List item 2",
            "End paragraph with `code`.\nAnother line in the same paragraph."
        ]
        result = markdown_to_block(markdown)
        self.assertEqual(result, expected)

    def test_nested_lists(self):
        markdown = "# The Heading\n\n1. First item\n   1. Sub-item 1\n   2. Sub-item 2\n\n2. Second item\n\n- Bullet 1\n- Bullet 2\n  - Sub-bullet 1\n  - Sub-bullet 2\n\nAnother paragraph."
        expected = [
            "# The Heading",
            "1. First item\n   1. Sub-item 1\n   2. Sub-item 2",
            "2. Second item",
            "- Bullet 1\n- Bullet 2\n  - Sub-bullet 1\n  - Sub-bullet 2",
            "Another paragraph."
        ]
        result = markdown_to_block(markdown)
        self.assertEqual(result, expected)
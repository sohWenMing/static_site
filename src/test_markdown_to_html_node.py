from markdown_to_html_node import markdown_to_htmlnode
from markdown_to_block import markdown_to_blocks, block_to_block_type
import unittest

paragraph_block = "This is a paragraph block \n\n"
heading_one_block = "# Heading 1 \n\n"
heading_two_block = "## Heading 2 \n\n"
heading_three_block = "### Heading 3 \n\n"
heading_four_block = "#### Heading 4 \n\n"
heading_five_block = "##### Heading 5 \n\n"
heading_six_block = "###### Heading 6 \n\n"
quote_block = ">quote line 1 \n>quote line 2 \n>quote line 3 \n\n"
ul_block = "* ul line 1 \n* ul line 2 \n\n" 
ol_block = "1 ol line 1 \n2 ol line 2 \n\n"
code_block = "```this is some code \n this is some other code``` \n\n"

class TestMarkDownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        returned_html = markdown_to_htmlnode(paragraph_block + paragraph_block).to_html()
        # print(returned_html)
    def test_headings(self):
        returned_html = markdown_to_htmlnode(
            heading_one_block + heading_two_block + heading_three_block
            + heading_four_block + heading_five_block + heading_six_block
        ).to_html()
        # print(returned_html)
    def test_quotes(self):
        returned_html = markdown_to_htmlnode(quote_block + quote_block).to_html()
    def test_ul_block(self):
        returned_html = markdown_to_htmlnode(ul_block + ul_block).to_html()
    def test_ol_block(self):
        returned_html = markdown_to_htmlnode(ol_block + ol_block).to_html()
        # print(returned_html)
    def test_code_block(self):
        returned_html = markdown_to_htmlnode(code_block + code_block).to_html()
        print(returned_html)    
    

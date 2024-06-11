from markdown_to_block import markdown_to_blocks, block_to_block_type
import unittest

block_break = "\n" + "\n"
newline = "\n"

def generate_heading_text(num_hex, with_space = True):
    text_string = ""
    for i in range(0, num_hex):
        text_string += "#"
    if with_space:
        text_string += " "
    text_string += "This is a heading"
    return text_string

code_block_one = "```" + newline + "This is some code" + newline + "```"
code_block_two = "``` This should also be some code ```"

def generate_quote(num_quote_lines, with_space = True):
    text_string = ""
    for i in range(1, num_quote_lines + 1):
        if with_space:
            text_string += f"> This is quote line {str(i)}\n"
        else:
            text_string += f">This is quote line {str(i)}\n"
    return(text_string)

def generate_unordered_list(num_lines, with_space=True):
    text_string = ""
    for i in range(1, num_lines + 1):
        if with_space:
            text_string += f"* This is line {i}\n"
        else:
            text_string += f"*This is line {i}\n"
    return text_string

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_basic(self):
        for i in range(1, 7):
            heading_text = generate_heading_text(i)
            generated_blocks = markdown_to_blocks(heading_text)
            self.assertEqual(block_to_block_type(generated_blocks[0]), "heading")

    def test_too_many_hex(self):
        heading_text = generate_heading_text(100)
        generated_blocks = markdown_to_blocks(heading_text)
        self.assertEqual(block_to_block_type(generated_blocks[0]), "paragraph")

    def test_code_block_basic(self):
        generated_blocks = markdown_to_blocks(code_block_one)
        self.assertEqual(block_to_block_type(generated_blocks[0]), "code")

    def test_single_line_code_block(self):
        generated_blocks = markdown_to_blocks(code_block_two)
        self.assertEqual(block_to_block_type(generated_blocks[0]), "code")

    def test_combination(self):
        generated_blocks = markdown_to_blocks(generate_heading_text(1) + block_break + code_block_one)
        self.assertEqual(len(generated_blocks), 2)
        self.assertEqual(block_to_block_type(generated_blocks[0]), "heading")
        self.assertEqual(block_to_block_type(generated_blocks[1]), "code")
        generated_blocks = markdown_to_blocks(generate_heading_text(1) + newline + code_block_one)
        self.assertEqual(len(generated_blocks), 1)
        self.assertEqual(block_to_block_type(generated_blocks[0]), "heading")

    def test_quote_basic(self):
        generated_blocks = markdown_to_blocks(generate_quote(7, False) + block_break + generate_quote(7))
        for block in generated_blocks:
            self.assertEqual(block_to_block_type(block), "quote")
    
    def test_quotes_together(self):
        generated_blocks = markdown_to_blocks(generate_quote(7, False) + generate_quote(7))
        for block in generated_blocks:
            self.assertEqual(block_to_block_type(block), "quote")
        self.assertEqual(len(generated_blocks), 1)

    def test_unordered_list(self):
        generated_blocks = markdown_to_blocks(generate_unordered_list(7) + block_break + generate_unordered_list(7))
        for block in generated_blocks:
            self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_wrong_unordered_list(self):
        generated_blocks = markdown_to_blocks(generate_unordered_list(7) + block_break + generate_unordered_list(7, False))
        self.assertEqual(len(generated_blocks), 2)
        self.assertEqual(block_to_block_type(generated_blocks[0]), "unordered_list")
        self.assertEqual(block_to_block_type(generated_blocks[1]), "paragraph")

    


        






import unittest
from reg_extract import extract_markdown_links, extract_markdown_images

class TestRegex(unittest.TestCase):
    def test_image_regex_basic(self):
        returned_val = extract_markdown_images(
            "![image](http://www.google.com/image1.jpg)![another](http://www.google.com/image2.jpg)")
        self.assertEqual(returned_val, 
                         [('image', 'http://www.google.com/image1.jpg'),
                          ('another', 'http://www.google.com/image2.jpg')
                          ])
    
    def test_image_not_matched_alt(self):
        returned_val = extract_markdown_images(
             "![image](http://www.google.com/image1.jpg)![another]"
        )
        self.assertEqual(returned_val,
                         [('image', 'http://www.google.com/image1.jpg')])
    
    def test_no_image_alts(self):
        returned_val = extract_markdown_images("[image](http://www.google.com/image1.jpg) [another](http://www.google.com/image2.jpg)")
        self.assertEqual(returned_val, [])

    def check_types_passed(self):
        with self.assertRaises(ValueError):
            extract_markdown_images(["![image](http://www.google.com/image1.jpg)![another](http://www.google.com/image2.jpg)"])
        with self.assertRaises(ValueError):
            extract_markdown_links(["[image](http://www.google.com/image1.jpg) [another](http://www.google.com/image2.jpg)"])

    def test_link_regex_basic(self):
        returned_val = extract_markdown_links("[image](http://www.google.com/image1.jpg) [another](http://www.google.com/image2.jpg)")
        self.assertEqual(returned_val, [("image", "http://www.google.com/image1.jpg"), ("another", "http://www.google.com/image2.jpg")])

    def test_link_not_matched(self):
        returned_val = extract_markdown_links("[image](http://www.google.com/image1.jpg)   ![another](http://www.google.com/image2.jpg)")
        self.assertEqual(returned_val, [("image", "http://www.google.com/image1.jpg")])

    def test_no_link_alts(self):
        returned_value = extract_markdown_links("![image](http://www.google.com/image1.jpg)![another](http://www.google.com/image2.jpg)")
        self.assertEqual(returned_value, [])
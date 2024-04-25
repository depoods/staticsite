import unittest

from htmlnode import *
from textnode import TextNode

#from enum import Enum

class TestMarkdown_to_blocks(unittest.TestCase):
    
    def test_block_test(self):
        document = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

        expected_blocks = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ]

        # Assuming markdown_to_blocks is a function you've defined elsewhere
        actual_blocks = markdown_to_blocks(document)
        
        # Check if the actual output matches the expected output
        self.assertEqual(actual_blocks, expected_blocks)
        


if __name__ == "__main__":
    unittest.main()
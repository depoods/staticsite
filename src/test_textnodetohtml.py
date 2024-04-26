import unittest

from htmlnode import *
from textnode import TextNode

#from enum import Enum

class TestMarkdownParser(unittest.TestCase):
    
    def test_heading(self):
        # Example of a heading test
        heading = "# This is a heading"
        self.assertEqual(block_to_block_type(heading), BlockType.HEAD)
    
    def test_code(self):
        # Example of a code block test
        code = "```print('Hello, World!')```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_quote(self):
        quote = ">This is a Quote\n>Quiiioootteee"
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)
    
    def test_unordered_list(self):
        unordered_list = "* List one\n* List two"
        self.assertEqual(block_to_block_type(unordered_list), BlockType.U_LIST)

    def test_ordered_list(self):
        ordered_list = "1. List one\n2. List two"
        self.assertEqual(block_to_block_type(ordered_list), BlockType.LIST)

    # Add more tests for other block types like quote, unordered list, ordered list, etc.

if __name__ == "__main__":
    unittest.main()
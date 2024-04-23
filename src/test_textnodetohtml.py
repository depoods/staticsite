import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, TextNodeType, text_node_to_html_node, split_nodes_delimiter
from textnode import TextNode

#from enum import Enum

class TestTextNodeToHtmlNode(unittest.TestCase):
    
    def test_splits_simple_string(self):
        # Testing a simple string split with no initial delimiter
        old_node = [TextNode("This is text with `code` inside", TextNodeType.TEXT)]
        expected_result = [
            TextNode("This is text with ", TextNodeType.TEXT),
            TextNode("code", TextNodeType.CODE),  # Assuming your "code" text_type is just "code"
            TextNode(" inside", TextNodeType.TEXT)
        ]
        result = split_nodes_delimiter(old_node, "`", TextNodeType.CODE)
        self.assertEqual(result, expected_result)
    
    def test_handles_beginning_delimiter(self):
        # Testing string that starts with a delimiter
        old_node = [TextNode("`code` at the start", TextNodeType.TEXT)]
        expected_result = [
            TextNode("code", TextNodeType.CODE),
            TextNode(" at the start", TextNodeType.TEXT)
        ]
        result = split_nodes_delimiter(old_node, "`", TextNodeType.CODE)
        #print(f"RESULT: {result}")
        self.assertEqual(result, expected_result)

    def test_odd_number_of_delimiters_raises_exception(self):
        # Testing to ensure the function raises an exception for an odd number of delimiters
        old_node = [TextNode("This is `incorrect syntax", TextNodeType.TEXT)]
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(old_node, "`", "code")
        self.assertTrue('invalid Markdown Syntax found' in str(context.exception))
            

if __name__ == "__main__":
    unittest.main()
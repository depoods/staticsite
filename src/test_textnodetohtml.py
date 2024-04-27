import unittest

from htmlnode import *
from textnode import TextNode

#from enum import Enum

class TestMarkdownConverter(unittest.TestCase):
    
    def test_create_para_html_block_simple(self):
        self.assertEqual(create_para_html_block("Hello, world!"), "<p>Hello, world!</p>")

    def test_create_para_html_block_with_html_chars(self):
        # You might consider this test if you decide to handle HTML escaping in the future.
        self.assertEqual(create_para_html_block("Use <code> to embed code."), 
                         "<p>Use <code> to embed code.</p>")

    def test_create_unordered_list_html_block(self):
        markdown = "- Item 1\n- Item 2\n- Item 3"
        expected_html = "<ul>\n<li>Item 1</li>\n<li>Item 2</li>\n<li>Item 3</li>\n</ul>"
        self.assertEqual(create_unordered_list_html_block(markdown), expected_html)

    def test_create_ordered_list_html_block(self):
        markdown = "1. Item A\n2. Item B\n3. Item C"
        expected_html = "<ol>\n<li>Item A</li>\n<li>Item B</li>\n<li>Item C</li>\n</ol>"
        self.assertEqual(create_ordered_list_html_block(markdown), expected_html)
    
    def test_create_head_html_block(self):
        markdown = "## Head"
        expected_html = "<h2>Head</h2>"
        self.assertEqual(create_head_html_block(markdown), expected_html)

    def test_create_head_html_block(self):
        markdown = "## Head"
        expected_html = "<h2>Head</h2>"
        self.assertEqual(create_head_html_block(markdown), expected_html)
    
    def test_create_code_html_block(self):
        markdown = "```this is a code```"
        expected_html ="<pre><code>this is a code</code></pre>"
        self.assertEqual(create_code_html_block(markdown), expected_html)



if __name__ == "__main__":
    unittest.main()
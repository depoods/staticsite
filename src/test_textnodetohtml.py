import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, TextNodeType, text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image
from textnode import TextNode

#from enum import Enum

class TestSplitNodesImage(unittest.TestCase):
    
    def test_no_images(self):
        input_nodes = [TextNode("Just some text.", TextNodeType.TEXT)]
        expected_output = [TextNode("Just some text.", TextNodeType.TEXT)]
        self.assertEqual(split_nodes_image(input_nodes), expected_output)

    def test_image_in_the_middle(self):
        input_nodes = [TextNode("That's all for now, folks! ![Final Image](http://example.com/final.png)", TextNodeType.TEXT)]
        expected_output = [
            TextNode("That's all for now, folks! ", TextNodeType.TEXT),
            TextNode("Final Image", TextNodeType.IMAGE, "http://example.com/final.png")
        ]
        self.assertEqual(split_nodes_image(input_nodes), expected_output)

    def test_multiple_images(self):
        input_nodes = [TextNode("![Image A](http://example.com/imageA.png) Between two images ![Image B](http://example.com/imageB.png) isn't that cool?", TextNodeType.TEXT)]
        expected_output = [
            TextNode("Image A", TextNodeType.IMAGE, "http://example.com/imageA.png"),
            TextNode(" Between two images ", TextNodeType.TEXT),
            TextNode("Image B", TextNodeType.IMAGE, "http://example.com/imageB.png"),
            TextNode(" isn't that cool?", TextNodeType.TEXT)
        ]
        self.assertEqual(split_nodes_image(input_nodes), expected_output)

    def test_only_images(self):
        input_nodes = [TextNode("![Solo Image](http://example.com/solo.png)", TextNodeType.TEXT)]
        expected_output = [TextNode("Solo Image", TextNodeType.IMAGE, "http://example.com/solo.png")]
        self.assertEqual(split_nodes_image(input_nodes), expected_output)

    def test_surrounded_by_images(self):
        input_nodes = [TextNode("![Start](http://example.com/start.png) Welcome to the middle! ![End](http://example.com/end.png)", TextNodeType.TEXT)]
        expected_output = [
                TextNode("Start", TextNodeType.IMAGE, "http://example.com/start.png"),
                TextNode(" Welcome to the middle! ", TextNodeType.TEXT),
                TextNode("End", TextNodeType.IMAGE, "http://example.com/end.png")
        ]
        self.assertEqual(split_nodes_image(input_nodes), expected_output)
    
    # Add more tests here following the template...
if __name__ == "__main__":
    unittest.main()
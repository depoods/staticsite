import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "http://www.URL.com")
        node2 = TextNode("This is a text node", "bold", "http://www.URL.com")
        node3 = TextNode("This is a text", "bolt", 12)
        node4 = TextNode(None, "italian", "www")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
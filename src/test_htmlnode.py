import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_probs(self):
        node = HTMLNode()
        node_child_1 = HTMLNode()
        node1 = HTMLNode("p", "Hello World in HTML", [node, node_child_1], "<a>")
        node2 = HTMLNode("a", "Hello World in HTML :)", [node, node_child_1], '{"href": "https://www.google.com"}')

        print(node)
        print(node_child_1)
        print(node1)
        print(node2)

        print(node2.props_to_html())

if __name__ == "__main__":
    unittest.main()

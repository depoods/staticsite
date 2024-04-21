import unittest
from htmlnode import ParentNode, HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

class TestParentNode(unittest.TestCase):
    def test_single_child(self):
        # Test a ParentNode with a single child.
        # Setup a ParentNode instance with a LeafNode as a child.
        # Use self.assertEqual() to check the output of your to_html() method against the expected HTML string.
        node = ParentNode("p",LeafNode("p", "Hello, world!"), None)
        self.assertEqual(node.to_html(), "<p><p>Hello, world!</p></p>")
        
    def test_multiple_children(self):
        # Test a ParentNode with multiple children.
        # Similarly, setup your ParentNode with multiple children and compare the output.
        # Test for creating a section with a heading, a paragraph, and an ordered list with items
        node = ParentNode("section", [
            LeafNode("h2", "Heading Title"),
            LeafNode("p", "This is a paragraph describing the list below."),
            ParentNode("ol", [
                LeafNode("li", "First item"),
                LeafNode("li", "Second item"),
                LeafNode("li", "Third item")
            ])
        ])

        expected_html = ('<section>'
                        '<h2>Heading Title</h2>'
                        '<p>This is a paragraph describing the list below.</p>'
                        '<ol>'
                        '<li>First item</li>'
                        '<li>Second item</li>'
                        '<li>Third item</li>'
                        '</ol>'
                        '</section>')

        self.assertEqual(node.to_html(), expected_html)

    def test_nested_structure(self):
        # Test for creating a paragraph that includes a link
        node = ParentNode("p", [
            LeafNode(None, "Visit "),
            ParentNode("a", [LeafNode(None, "our website")], props={"href": "https://example.com"}),
            LeafNode(None, " for more information.")
        ])

        # Note on props_to_html(): This part assumes that your method for converting
        # the props dictionary to a string properly formats it for HTML output.
        expected_html = '<p>Visit <a href="https://example.com">our website</a> for more information.</p>'

        self.assertEqual(node.to_html(), expected_html)
        
    def test_no_tag_error(self):
        # Test that a ValueError is raised if no tag is provided.
        # Use self.assertRaises(ValueError) in a with context to check if the error is raised correctly.
        pass
        
    def test_no_children_error(self):
        # Test that a ValueError is raised if no children are provided.
        # Similar to test_no_tag_error, but check for children.
        pass

    def test_unordered_list(self):
        # Test for creating an unordered list with three items
        node = ParentNode("ul", [
            LeafNode("li", "Item 1"),
            LeafNode("li", "Item 2"),
            LeafNode("li", "Item 3"),
        ])
        self.assertEqual(node.to_html(), "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>")


if __name__ == "__main__":
    unittest.main()
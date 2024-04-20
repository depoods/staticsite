from textnode import TextNode

def main():
    new_text = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(new_text)

    node1 = TextNode("Sample text", "bold", "https://www.example.com")
    node2 = TextNode("Sample text", "bold", "https://www.example.com")

    print(node1 == node2)  # This should output: True

    # Different text
    node3 = TextNode("Different text", "bold", "https://www.example.com")
    print(node1 == node3)  # This should output: False

    # Different text_type
    node4 = TextNode("Sample text", "italic", "https://www.example.com")
    print(node1 == node4)  # This should output: False

    # Different URL
    node5 = TextNode("Sample text", "bold", "https://www.different.com")
    print(node1 == node5)  # This should output: False

main()
from enum import Enum

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textnode_obj):
        return (self.text == textnode_obj.text) and (self.text_type == textnode_obj.text_type) and (self.url == textnode_obj.url)

    def __repr__(self):
        return f"TextNode({self.text}, {type(self.text_type)}, {self.url})"


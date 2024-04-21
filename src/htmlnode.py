from enum import Enum

class HTMLNode:
    def __init__(self, tag=None , value=None, children=None, props=None):   
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""

        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'

        return props_html

    def __repr__(self):
        return f"HTMLNode: tag:{self.tag} value:{self.value}, children:{self.children}, props:{self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("HTML: invalid - no value for a leafnode")

        if self.tag is None:
            return self.value

        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        
        attributes_list = [f'{key}="{value}"' for key, value in self.props.items()]
        attributes_string =  " ".join(attributes_list)

        return f"<{self.tag} {attributes_string}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

        if not isinstance(children, list):
            children = [children]  # Encapsulate non-list children in a list
            self.children = children

    def to_html(self):
        if self.tag is None:
            raise ValueError("HTML: invalid, no tag")
        if self.children is None:
            raise ValueError("HTML: invalid, no children")

        html_opening_string = f"<{self.tag}{self.props_to_html()}>"
        html_strings = ""

        for child in self.children:
            html_strings += child.to_html()
        
        html_end_string = f"</{self.tag}>"
    
        return html_opening_string + html_strings + html_end_string

class TextNodeType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextNodeType._value2member_map_:
        raise Exception("Invalid text node type")

    if text_node.text_type == TextNodeType.TEXT.value:
        if text_node.url is None:
            return LeafNode(value=text_node.text)
    

    



        
        

        

        



        



"""
An HTMLNode without a tag will just render as raw text
An HTMLNode without a value will be assumed to have children
An HTMLNode without children will be assumed to have a value
An HTMLNode without props simply won't have any attributes
""" 

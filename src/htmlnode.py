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

        return f"<{self.tag} {attributes_string}>{self.value}</{self.tag}"



        



"""
An HTMLNode without a tag will just render as raw text
An HTMLNode without a value will be assumed to have children
An HTMLNode without children will be assumed to have a value
An HTMLNode without props simply won't have any attributes
""" 

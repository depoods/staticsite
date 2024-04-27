from enum import Enum
from textnode import TextNode
import re 

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
    def __init__(self, tag=None, value=None, props=None):
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

    if not isinstance(text_node.text_type, TextNodeType):
        raise Exception(f"Invalid text node type: {text_node.text_type}")

    if text_node.text_type == TextNodeType.TEXT:
        return LeafNode(value=text_node.text)
    
    if text_node.text_type == TextNodeType.BOLD:
        return LeafNode(tag="b", value=text_node.text)

    if text_node.text_type == TextNodeType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)

    if text_node.text_type == TextNodeType.CODE:
        return LeafNode(tag="code", value=text_node.text)   

    if text_node.text_type == TextNodeType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    
    if text_node.text_type == TextNodeType.IMAGE:
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text })

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return_list = []
    for old_node in old_nodes:
        if old_node.text_type is not TextNodeType.TEXT:
            return_list.append(old_node)
            continue
        
        if old_node.text.count(delimiter) % 2 == 0:
            tmp_str = old_node.text.split(delimiter)
            #print(f"TMP STR: {tmp_str}")
            if tmp_str[0] == "":
                #first char was a delimiter
                #Remove empty string
                tmp_str = tmp_str[1:]
                for index, segment in enumerate(tmp_str):
                    if index % 2 == 0: 
                        print(f'Segment: "{segment}" "{text_type}"')
                        return_list.append(TextNode(segment, text_type))
                        print(f"list: {return_list}")
                    else:
                        print(f'Segment: "{segment}" "{text_type}"')
                        return_list.append(TextNode(segment, old_node.text_type))
            else:
                #first char was not a delimiter
                for index, segment in enumerate(tmp_str):
                    if index % 2 == 0: 
                        return_list.append(TextNode(segment, old_node.text_type))
                    else:
                        return_list.append(TextNode(segment, text_type))

        else:
            raise Exception("invalid Markdown Syntax found")
    #print(return_list)
    return return_list

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    return_list = []
    text_parts = []

    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        remaining_text = old_node.text

        if(len(images)) == 0:
            return_list.append(old_node)
        else:
            for image in images:
                split_result = remaining_text.split(f"![{image[0]}]({image[1]})", 1)
                if len(split_result) > 1:
                    # There was at least one image, so updating the remaining_text to the part after the first image found.
                    before_image_text = split_result[0]
                    remaining_text = split_result[1]             
                    if before_image_text.strip():  # Checks if the text is not just whitespace
                        return_list.append(TextNode(before_image_text, TextNodeType.TEXT))

                    return_list.append(TextNode(image[0], TextNodeType.IMAGE,image[1]))
            # After processing all images in the loop:
            if remaining_text.strip():  # This checks if there's any text left.
                # You could add further checks here (like checking for not only whitespace)
                return_list.append(TextNode(remaining_text, TextNodeType.TEXT))


    return return_list

def split_nodes_links(old_nodes):
    return_list = []
    text_parts = []

    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        remaining_text = old_node.text

        if(len(links)) == 0:
            return_list.append(old_node)
        else:
            for link in links:
                split_result = remaining_text.split(f"[{link[0]}]({link[1]})", 1)
                if len(split_result) > 1:
                    # There was at least one link, so updating the remaining_text to the part after the first link found.
                    before_link_text = split_result[0]
                    remaining_text = split_result[1]             
                    if before_link_text.strip():  # Checks if the text is not just whitespace
                        return_list.append(TextNode(before_link_text, TextNodeType.TEXT))

                    return_list.append(TextNode(link[0], TextNodeType.LINK,link[1]))
            # After processing all link in the loop:
            if remaining_text.strip():  # This checks if there's any text left.
                # You could add further checks here (like checking for not only whitespace)
                return_list.append(TextNode(remaining_text, TextNodeType.TEXT))


    return return_list

def text_to_textnodes(text):
    nodes = [TextNode(text, TextNodeType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextNodeType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextNodeType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextNodeType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)

    return nodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return_list = []
    for block in blocks:
        return_list.append(block.strip())

    return return_list

class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered_list"
    LIST = "ordered_list"

def block_to_block_type(block):
    # Check if the block is a heading
    heading_result = check_for_headings(block)
    if heading_result:
        return heading_result
    
    # Check if the block is code
    code_result = check_for_code(block)
    if code_result:
        return code_result

    quote_result = check_for_quote(block)
    if quote_result:
        return quote_result
    
    unordered_list_result = check_for_unordered_list(block)
    if unordered_list_result:
        return unordered_list_result
    
    ordered_list_result = check_for_ordered_list(block)
    if ordered_list_result:
        return ordered_list_result
    
    return BlockType.PARA

    


def check_for_headings(text):
    if re.match(r"#{1,6}\s", text):
        return BlockType.HEAD

def check_for_code(text):
    if text.startswith("```") and text.endswith("```"):
        return BlockType.CODE

def check_for_quote(text):
    lines = text.split("\n")
    for line in lines:
        if not re.match(r"^>", line):
            return False
    return BlockType.QUOTE

def check_for_unordered_list(text):
    lines = text.split("\n")
    for line in lines:
        if not re.match(r"^(\*\s|\-\s)", line):
            return False
    return BlockType.U_LIST

def check_for_ordered_list(text):
    lines = text.split("\n")
    for line in lines:
        if not re.match(r"^\d+\.\s", line):
            return False
    return BlockType.LIST

def create_quote_html_block(block):
    return f"<blockquote>{block}</blockquote>"

def create_unordered_list_html_block(block):
    lines = block.split("\n")
    html_block = []
    html_block.append("<ul>")

    for line in lines:
        html_block.append(f"<li>{line[2:]}</li>")
    
    html_block.append("</ul>")
    return "\n".join(html_block)

def create_ordered_list_html_block(block):
    lines = block.split("\n")
    html_block = []
    html_block.append("<ol>")

    for line in lines:
        html_block.append(f"<li>{line[3:]}</li>")
    
    html_block.append("</ol>")
    return "\n".join(html_block)

def create_code_html_block(block):
    return f"<pre><code>{block[3:-3]}</code></pre>"

def create_head_html_block(block):
    match = re.match(r"(#{1,6})\s", block)
    hash_count = "1"
    if match:
        hash_count = len(match.group(1))
    return f"<h{hash_count}>{block.lstrip("# ")}</h{hash_count}>"

def create_para_html_block(block):
    return f"<p>{block}</p>"




    

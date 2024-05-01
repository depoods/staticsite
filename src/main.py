from textnode import TextNode
from copystatic import empty_public, copy_to_public
from generate import extract_title, generate_page

def main():

    generate_page("/home/depood/workspace/github.com/depoods/staticsite/content/index.md", "/home/depood/workspace/github.com/depoods/staticsite/template.html", "/home/depood/workspace/github.com/depoods/staticsite/static/index.html")
    empty_public()
    copy_to_public()


main()
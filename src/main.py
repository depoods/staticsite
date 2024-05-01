from textnode import TextNode
from copystatic import empty_public, copy_to_public
from generate import *

def main():

    #generate_page("/home/depood/workspace/github.com/depoods/staticsite/content/index.md", "/home/depood/workspace/github.com/depoods/staticsite/template.html", "/home/depood/workspace/github.com/depoods/staticsite/static/index.html")
    generate_pages_recursive("/home/depood/workspace/github.com/depoods/staticsite/content/","/home/depood/workspace/github.com/depoods/staticsite/template.html","/home/depood/workspace/github.com/depoods/staticsite/static/" )
    empty_public()
    copy_to_public()


main()
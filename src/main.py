from textnode import TextNode
import os
import shutil

def main():
    file_copy("/home/depood/workspace/github.com/depoods/staticsite/static/index.css", "/home/depood/workspace/github.com/depoods/staticsite/public/index.css")
    file_delete("/home/depood/workspace/github.com/depoods/staticsite/public/delete_me")

def file_copy(file_src, file_target):
    shutil.copy(file_src, file_target)
    print(f"copy attempt: {file_src}, {file_target}")

def file_delete(file_target):
    shutil.rmtree(file_target)
    print(f"deleting {file_target}")



    


main()
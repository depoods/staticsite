from markdown_blocks import *
from copystatic import *

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)    

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type is block_type_heading:
            if block.startswith("# "):
                return block[2:]
            else:
                raise Exception("No Header found")

def generate_page(from_path, template_path, dest_path):
    print("Step 0: warmup..")

     # Step 1: Read the markdown file
    print(f"Opening MarkDown File from {from_path}")
    with open(from_path, 'r') as markdown_object:
        markdown_text = markdown_object.read()

    # Step 2: Read the template file
    print(f"Opening Template file from {template_path}")
    with open(template_path, 'r') as template_object:
        template_text = template_object.read()

    # Step 3: Generate HTML Code from Markdown_text
    print("Generating HTML Code from Markdown text")
    markdown_html_code = markdown_to_html_node(markdown_text).to_html()

    # Step 4: Extract Title from the markdown text
    print("Extracting Title from the markdown text")
    title = extract_title(markdown_text)

    # Step 5: Generate the final HTML by replacing placeholders in template text
    print("Generating a HTML page from Template and Markdown")
    final_html_content = template_text.replace("{{ Title }}", title).replace("{{ Content }}", markdown_html_code)

    # Step 6: Generate a HTML file for output
    print(f"Writing final HTML to {dest_path}")
    with open(dest_path, 'w') as file:
        file.write(final_html_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    #scan dirpath

    if not dir_path_content.endswith(os.sep):
        dir_path_content += os.sep

    if not dest_dir_path.endswith(os.sep):
        dest_dir_path += os.sep



    files = []
    folders = []
    html_path = ""
    scan_directory(dir_path_content, files, folders)


    for file in files:
        if file[-3:] == ".md":
            relative_path = file[len(dir_path_content):]  # Extract the relative path
            html_relative_path = relative_path[:-3] + ".html"  # Replace .md with .html
            full_html_path = os.path.join(dest_dir_path, html_relative_path)

            html_dir = os.path.dirname(full_html_path)
            os.makedirs(html_dir, exist_ok=True)

            print(f"generating recursive HTML files in {full_html_path}")
            generate_page(file, template_path, full_html_path)
    



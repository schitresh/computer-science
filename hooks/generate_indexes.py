import os

docs_dir = "docs"

# Traverse through all directories inside your docs folder
for root, dirs, files in os.walk(docs_dir):
    # Skip the absolute root docs directory itself
    if root == docs_dir:
        continue

    folder_name = os.path.basename(root)

    # Safe title formatting: removes "01_" and fixes the list-split bug
    if "_" in folder_name and folder_name[:2].isdigit():
        clean_title = folder_name.split("_", 1)[1].replace("_", " ").title()
    else:
        clean_title = folder_name.replace("_", " ").title()

    # Build out dynamic markdown list items for files inside this folder
    links_markdown = ""

    # Sort files to respect numeric sorting prefixes on the page
    for filename in sorted(files):
        # Only list actual documentation files, skipping the index itself
        if filename.endswith(".md") and filename.lower() != "index.md":
            if "_" in filename and filename[:2].isdigit():
                file_title = (
                    filename.split("_", 1)[1]
                    .replace(".md", "")
                    .replace("_", " ")
                    .title()
                )
            else:
                file_title = filename.replace(".md", "").replace("_", " ").title()

            # Append a functional relative markdown link
            links_markdown += f"* [{file_title}]({filename})\n"

    # Also list out child subfolders if they exist
    for sub_dir in sorted(dirs):
        if "_" in sub_dir and sub_dir[:2].isdigit():
            sub_title = sub_dir.split("_", 1)[1].replace("_", " ").title()
        else:
            sub_title = sub_dir.replace("_", " ").title()
        links_markdown += f"* [{sub_title}]({sub_dir}/index.md)\n"

    # Construct the final markdown index document path
    index_path = os.path.join(root, "index.md")

    # Template: Title followed immediately by your bullet links
    markdown_content = f"# {clean_title}\n\n{links_markdown}"

    # REMOVED SAFETY CHECK: This now overwrites and refreshes files every time!
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"[UPDATED] {index_path} layout refreshed.")

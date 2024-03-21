import os
import argparse

def gather_files_and_dirs(root_dir, extensions):
    """
    Create a nested dictionary that represents the folder structure of root_dir,
    including files that match the given extensions but excluding directories and
    files that start with '.' or are in the 'venv' directory.
    """
    tree = {}
    for root, dirs, files in os.walk(root_dir, topdown=True):
        # Skip the 'venv' directory and its contents
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'venv']
        if 'venv' in root:
            continue
        files = [f for f in files if not f.startswith('.') and f.endswith(extensions)]

        # Construct the tree structure
        parts = os.path.relpath(root, start=root_dir).split(os.sep)
        subtree = tree
        for part in parts:
            if part != '.':
                subtree = subtree.setdefault(part, {})

        for file in files:
            subtree[file] = None  # Represent files as None

    return tree


def print_tree(node, prefix='', output_file=None):
    """
    Recursively prints the tree structure (both directories and files)
    to the given output file. The 'node' parameter should be a dictionary
    representing the tree.
    """
    children = list(node.keys())
    for i, child in enumerate(children):
        connector = "└── " if i == len(children) - 1 else "├── "
        if isinstance(node[child], dict):  # If the child is a directory
            output_file.write(f"{prefix}{connector}{child}/\n")
            new_prefix = "    " if i == len(children) - 1 else "│   "
            print_tree(node[child], prefix + new_prefix, output_file)
        else:  # The child is a file
            output_file.write(f"{prefix}{connector}{child}\n")


def gather_file_paths(root_dir, extensions):
    """
    Generator to yield paths of files matching the given extensions, excluding
    those starting with '.' and within the 'venv' directory.
    """
    for root, dirs, files in os.walk(root_dir, topdown=True):
        # Exclude 'venv' directory
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'venv']
        if 'venv' in root:
            continue
        for file in files:
            if file.startswith('.') or not file.endswith(extensions):
                continue
            yield os.path.join(root, file)


def write_file_contents(file_paths, output_file):
    """
    Writes the content of files to the output_file.
    """
    for idx, file_path in enumerate(file_paths, start=1):
        rel_path = os.path.relpath(file_path, start=os.path.dirname(output_file.name))
        output_file.write(f"\n{idx}. '{rel_path}':\n```\n")
        with open(file_path, "r", encoding="utf-8") as file:
            contents = file.read()
            output_file.write(contents)
            output_file.write("\n```\n")


def main(project_dir, output_file_path, extensions=('.py', '.js', '.css', '.html')):
    tree = gather_files_and_dirs(project_dir, extensions)
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        print_tree(tree, output_file=output_file)
        file_paths = gather_file_paths(project_dir, extensions)
        write_file_contents(file_paths, output_file)
    print(f"Project structure and contents written to {output_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate project documentation for GitHub publishing.")
    parser.add_argument("project_dir", help="Path to the project directory")
    parser.add_argument("output_file_path", help="Path where the output file will be saved")
    args = parser.parse_args()
    main(args.project_dir, args.output_file_path)

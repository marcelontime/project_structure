
# Project Documentation Tool

This tool generates a comprehensive documentation of your project structure and detailed contents of specified file types (`.py`, `.js`, `.css`, `.html`). It's designed to help you create a clear overview of your project for GitHub or other platforms where your code will be published.

## Features

- **Project Structure Overview**: Generates a tree representation of your project directory, excluding directories and files starting with a dot (e.g., `.git`) and the `venv` directory.
- **File Contents Inclusion**: Appends the contents of `.py`, `.js`, `.css`, and `.html` files to the documentation, providing a detailed look into your project's codebase.

## Usage

To use this tool, you'll need Python installed on your system. Download the script from the URL and run it from the command line, providing the path to your project directory and the desired output file path for the documentation.

### Downloading the Script

```bash
curl -o project_doc_tool.py <URL_TO_DOWNLOAD_SCRIPT>
```

Replace `<URL_TO_DOWNLOAD_SCRIPT>` with the actual URL where the script is hosted.

### Running the Tool

```bash
python project_doc_tool.py <path_to_project_directory> <path_to_output_file>
```

Replace `<path_to_project_directory>` with the path to your project directory and `<path_to_output_file>` with the path where you want the output documentation file to be saved.

## Example

```bash
python project_doc_tool.py my_project/ project_overview.md
```

This command will generate a file named `project_overview.md` in the current directory, containing the structure and contents of the `my_project` directory.

## License

MIT License

Copyright (c) 20024 Marcelo Sales

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contributions

Contributions are welcome! Please feel free to submit a pull request.

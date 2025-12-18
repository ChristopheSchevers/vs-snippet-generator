# Snippet Generator

This project is a Python application designed to generate Visual Studio Code snippets from text copied to the clipboard. It features a graphical user interface (GUI) built with Tkinter, allowing users to easily input snippet details and generate a JSON representation of the snippet.

## Features

- **Clipboard Integration**: Automatically reads code from the clipboard.
- **Customizable Snippets**: Users can specify the title, prefix, and description for each snippet.
- **Cross-Platform**: Supports building for both Windows and Unix-like systems.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

1. Copy the code you want to turn into a snippet to your clipboard.
2. Run the application by executing `src/main.py`.
3. Fill in the snippet title, prefix, and description in the GUI.
4. Click "Generate & Copy" to copy the JSON snippet to your clipboard.

## Building the Application

### For Windows

To build the application for Windows, run the following command in the terminal:

```
scripts/build_windows.bat
```

### For Unix-like Systems

To build the application for Unix-like systems, use:

```
scripts/build_unix.sh
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
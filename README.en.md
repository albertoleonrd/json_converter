# JSON Converter

Command-line tool to efficiently convert between JSON Lines (JSONL) and standard JSON formats.

## Features

- JSONL to JSON conversion: Transforms files where each line is a JSON object into a single JSON file with an array of objects.
- JSON to JSONL conversion: Converts a JSON file with an array of objects to a text file where each line is a JSON object.
- Efficient handling of large files through streaming processing.
- Robust validation and clear error messages.

## Requirements

- Python 3.8 or higher

## Installation

### 1. Verify Python Installation

Before starting, make sure you have Python 3.8 or higher correctly installed:

1. Open a terminal (PowerShell or Command Prompt) and verify if Python is installed:

```bash
python --version
```

If you see a message like "Python 3.x.x", Python is correctly installed. If you receive an error, follow these steps:

#### If Python is not installed:

1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, **MAKE SURE TO CHECK THE OPTION "Add Python to PATH"**
3. Restart your terminal after installation

#### If Python is installed but the command is not recognized:

Python might be installed but not in your PATH. You can:

- Use the full path to the Python executable. Look for where it's installed (typically in `C:\Python3x\` or `C:\Users\[user]\AppData\Local\Programs\Python\Python3x\`)
- Add Python to PATH manually:
  1. Search for "Environment Variables" in the start menu
  2. Click on "Environment Variables..."
  3. In the "System Variables" section, select "Path" and click "Edit"
  4. Click "New" and add the path to the Python folder and also to the Scripts subfolder
  5. Click "OK" in all windows
  6. Restart your terminal

### 2. Clone or download this repository:

```bash
git clone https://github.com/albertoleonrd/json_converter.git
cd json_converter
```

### 3. Install the package in development mode:

```bash
# Install using pip
pip install -e .
```

**Note**: If the pip command doesn't work, make sure Python is correctly installed and added to the system PATH.

## Basic Usage

### Automatic Mode (Recommended)

The tool automatically detects the format of the input file and performs the appropriate conversion:

```bash
json_converter --input file.jsonl --output file.json
```

or

```bash
json_converter --input file.json --output file.jsonl
```

### View help

```bash
json_converter --help
```

## Examples

In the `examples/` directory you will find example files in both formats:

- `ejemplo.jsonl`: File in JSONL format (each line is a JSON object)
- `ejemplo.json`: File in JSON format (array of objects)

You can test the tool with these files:

```bash
# Using automatic mode
json_converter --input examples/ejemplo.jsonl --output result.json
json_converter --input examples/ejemplo.json --output result.jsonl
```

### Example of JSONL content (ejemplo.jsonl)

```
{"id": 1, "nombre": "Juan", "edad": 30}
{"id": 2, "nombre": "María", "edad": 25}
{"id": 3, "nombre": "Pedro", "edad": 35}
```

### Example of JSON content (ejemplo.json)

```json
[
  {"id": 1, "nombre": "Juan", "edad": 30},
  {"id": 2, "nombre": "María", "edad": 25},
  {"id": 3, "nombre": "Pedro", "edad": 35}
]
```

## Running Tests

To run the unit tests:

```bash
python -m unittest discover tests
```

## Error Handling

The tool provides clear error messages for common situations:

- Input file not found
- Insufficient permissions
- Invalid JSON
- Incorrect format (for example, if the JSON file does not contain an array as the main element)

If you encounter any problems, make sure to check:

1. That the files exist and have the correct permissions
2. That the file format is as expected
3. That you have enough disk space for the operation

## Contributions

Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a branch for your feature (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a new Pull Request
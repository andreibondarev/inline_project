# Inline Project

A command-line tool to inline the content of a project (code) into a single file.

## Installation

```
pip install git+https://github.com/andreibondarev/inline_project.git
```

## Usage

```
inline-project /path/to/your/project output.txt --exclude-dirs .git node_modules --exclude-files .DS_Store
```

This will create a file named `output.txt` containing the inlined content of your project, excluding the `.git` and `node_modules` directories and the `.DS_Store` file.

## Options

- `project_dir`: Path to the project directory (required)
- `output_file`: Path to the output file (required)
- `--exclude-dirs`: Directories to exclude (optional, can specify multiple)
- `--exclude-files`: Files to exclude (optional, can specify multiple)


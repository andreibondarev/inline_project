import os
import argparse

def inline_project(project_dir, output_file, exclude_dirs=None, exclude_files=None):
    if exclude_dirs is None:
        exclude_dirs = set()
    if exclude_files is None:
        exclude_files = set()

    exclude_dirs = {os.path.relpath(os.path.join(project_dir, d), project_dir) for d in exclude_dirs}

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(project_dir):
            rel_root = os.path.relpath(root, project_dir)
            if rel_root in exclude_dirs:
                continue

            dirs[:] = [d for d in dirs if os.path.relpath(os.path.join(root, d), project_dir) not in exclude_dirs]
            
            for file in files:
                if file in exclude_files:
                    continue
                
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, project_dir)
                
                outfile.write(f"\n\n# File: {rel_path}\n")
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                except UnicodeDecodeError:
                    outfile.write(f"# Unable to read file: {rel_path} (possibly binary)\n")

def main():
    parser = argparse.ArgumentParser(description="Inline project content into a single file")
    parser.add_argument("project_dir", help="Path to the project directory")
    parser.add_argument("output_file", help="Path to the output file")
    parser.add_argument("--exclude-dirs", nargs="*", default=[], help="Directories to exclude")
    parser.add_argument("--exclude-files", nargs="*", default=[], help="Files to exclude")
    
    args = parser.parse_args()
    
    inline_project(args.project_dir, args.output_file, set(args.exclude_dirs), set(args.exclude_files))
    print(f"Project content has been inlined into {args.output_file}")

if __name__ == "__main__":
    main()


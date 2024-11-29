import os
from collections import defaultdict

def count_lines_of_code(directory):
    total_lines = 0
    file_count = 0
    line_counts_by_type = defaultdict(int)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.java', '.c', '.cpp', '.h', '.hpp', '.js', '.html', '.css', '.json')):
                file_path = os.path.join(root, file)
                file_count += 1
                file_extension = os.path.splitext(file)[1]
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        line_count = len(lines)
                        total_lines += line_count
                        line_counts_by_type[file_extension] += line_count
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    
    return total_lines, file_count, line_counts_by_type

def main():
    current_directory = os.getcwd()
    total_lines, file_count, line_counts_by_type = count_lines_of_code(current_directory)
    
    print(f"Total number of code files: {file_count}")
    print(f"Total number of lines of code: {total_lines}")
    
    print("\nLines of code by file type:")
    for file_type, count in line_counts_by_type.items():
        print(f"{file_type}: {count} lines")

if __name__ == "__main__":
    main()
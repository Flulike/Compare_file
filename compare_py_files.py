import difflib
import sys

def read_file(file_path):
    """Read file and return a list of lines, normalizing spaces and ignoring empty lines."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.rstrip() for line in f.readlines() if line.strip()]

def compare_files(file1, file2):
    """Compare two Python files while ignoring whitespace differences and formatting a colored HTML report."""
    lines1 = read_file(file1)
    lines2 = read_file(file2)
    
    diff = difflib.unified_diff(lines1, lines2, fromfile=file1, tofile=file2, lineterm='')
    html_diff = difflib.HtmlDiff().make_file(lines1, lines2, file1, file2)
    
    return '\n'.join(diff), html_diff

def save_html_report(html_diff, output_file="diff_report.html"):
    """Save the HTML diff report to a file."""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_diff)
    print(f"HTML report saved to {output_file}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python compare.py <file1.py> <file2.py>")
        sys.exit(1)
    
    file1, file2 = sys.argv[1], sys.argv[2]
    result, html_diff = compare_files(file1, file2)
    
    if result:
        print(result)
    else:
        print("No differences found.")
    
    save_html_report(html_diff)

if __name__ == "__main__":
    main()

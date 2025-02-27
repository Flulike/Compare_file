from flask import Flask, render_template, request
import difflib

app = Flask(__name__)

def compare_code(code1, code2):
    """Compares two pieces of Python code and returns an HTML diff."""
    lines1 = code1.strip().split('\n')
    lines2 = code2.strip().split('\n')
    return difflib.HtmlDiff().make_file(lines1, lines2, "Original", "Modified")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code1 = request.files['file1'].read().decode('utf-8')
        code2 = request.files['file2'].read().decode('utf-8')
        diff_html = compare_code(code1, code2)
        return render_template('result.html', diff=diff_html)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
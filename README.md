# 🐍Code Comparison Tool

## 🚀 Overview
It's just that when I want to Reproduction Code about some paper on the baseline, I need to find the code difference between the paper and baseline. I believe there must be other repositories which are strong enough for code comparison. I just write this code with GPT and DeepSeek, and hope it will be useful for you.  

## 🔥 Features
- **Ignores whitespace changes & empty lines** because who cares about extra spaces?
- **Displays a handy diff output** in the terminal for quick inspection.
- **Generates an awesome HTML report** so you can view differences in full color!

## 🛠 Requirements
- Python 3.x (no extra dependencies, just good ol' Python)

## 📦 Installation
No installation needed! Just run the script and you're good to go.

## 🚀 Usage
Fire up your terminal and run:
```sh
python compare.py <file1.py> <file2.py>
```
Example:
```sh
python compare.py original.py modified.py
```

### 🖥 Output
1. **Terminal Output:** Shows a clean diff highlighting changes.
2. **HTML Report:** Creates `diff_report.html`, open it in any browser and enjoy the colorful diff magic! ✨

## 🚧 Recent plans
### Graphical User Interface

## 📜 Example Diff Output
Sample terminal output:
```diff
--- original.py
+++ modified.py
@@ -2,7 +2,7 @@
def example():
-    print("Hello World")
+    print("Hello Hell")
```

## 📜 License
This script is free to use, modify, and share! No strings attached. 🎉


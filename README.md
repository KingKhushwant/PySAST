PySAST (Python Static Application Security Testing Tool)
---

```markdown

**PySAST** is a beginner-friendly Static Analysis tool written in pure Python. It scans Python source code for insecure coding patterns and bad practices — without running the code.

Built for learning, lightweight projects, and early-stage secure coding.

---

## 🔍 What PySAST Detects

✅ Hardcoded password variables  
✅ Usage of dangerous functions (`eval`, `exec`)  
✅ Dangerous OS calls like `os.system("...")`  

---

## 📂 Example

```python
password = "12345"
eval("print('This is bad')")
os.system("rm -rf /")
```

Running PySAST:

```bash
python main.py target.py
```

Output:

```
 Line 1: Hardcoded password
 Line 2: Dangerous function used: eval
 Line 3: Dangerous os.system call
```

---

## 🛠️ How to Use

1. Clone this repo
2. Put your Python code in a file like `target.py`
3. Run:

```bash
python main.py target.py
```

No dependencies. Just plain old Python.

---

## 🧠 How It Works

- Uses Python’s built-in `ast` (Abstract Syntax Tree) module
- Walks through your code safely (no execution)
- Flags risky patterns by inspecting assignments and function calls

---

## 🗂️ Project Structure

```
PySAST/
├── main.py        # Core scanner
├── target.py      # Sample vulnerable code
└── README.md      # This file
```

---










import ast
import sys
import re

class SAST(ast.NodeVisitor):
    def __init__(self):
        self.issues = []

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                if re.search(r'pass(word|wd)?', target.id, re.IGNORECASE):
                    self.issues.append((node.lineno, "Hardcoded password"))
        self.generic_visit(node)

    def visit_Call(self, node):
        # Check for eval and exec
        if isinstance(node.func, ast.Name) and node.func.id in ["eval", "exec"]:
            self.issues.append((node.lineno, f"Dangerous function used: {node.func.id}"))

        # Check for os.system and other dangerous calls
        elif isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "os":
                if node.func.attr == "system":
                    self.issues.append((node.lineno, "Dangerous os.system call"))

        self.generic_visit(node)

    def report(self):
        if not self.issues:
            print(" No issues found!")
        for lineno, message in self.issues:
            print(f" Line {lineno}: {message}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sast.py target.py")
        sys.exit(1)

    with open(sys.argv[1], "r") as file:
        code = file.read()

    tree = ast.parse(code)
    scanner = SAST()
    scanner.visit(tree)
    scanner.report()

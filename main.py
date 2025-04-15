import argparse
import ast
import re
import sys
import os


class SimpleSAST(ast.NodeVisitor):
    def __init__(self):
        self.issues = []

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                if re.search(r'pass(word|wd)?', target.id, re.IGNORECASE):
                    self.issues.append((node.lineno, "Hardcoded password"))
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in ["eval", "exec"]:
            self.issues.append((node.lineno, f"Dangerous function used: {node.func.id}"))

        elif isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "os":
                if node.func.attr == "system":
                    self.issues.append((node.lineno, "Dangerous os.system call"))

        self.generic_visit(node)

    def report(self, filename):
        if not self.issues:
            print(f" {filename}: No issues found.")
        else:
            print(f" Issues in {filename}:")
            for lineno, message in self.issues:
                print(f" Line {lineno}: {message}")


def scan_file(path):
    try:
        with open(path, "r") as f:
            code = f.read()
        tree = ast.parse(code)
        scanner = SimpleSAST()
        scanner.visit(tree)
        scanner.report(path)
    except Exception as e:
        print(f" Error scanning {path}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description=" PySAST - A simple static analysis tool for Python"
    )
    parser.add_argument("file", help="Python file to scan")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f" File not found: {args.file}")
        sys.exit(1)

    scan_file(args.file)


if __name__ == "__main__":
    main()

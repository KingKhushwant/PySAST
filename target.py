import os

password = "secret123"

def run_command(cmd):
    os.system(cmd)

def main():
    query = "SELECT * FROM users WHERE name = 'admin'"
    eval("print('This is unsafe')")
    run_command("ls -la")

main()

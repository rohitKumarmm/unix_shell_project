import os
import shutil
import socket
import datetime

def list_files():
    for f in os.listdir('.'):
        if os.path.isfile(f):
            print(f)

def list_dirs():
    for f in os.listdir('.'):
        if os.path.isdir(f):
            print(f)

def show_date():
    print(datetime.datetime.now().strftime("%d-%b-%Y"))

def show_time(option=None):
    now = datetime.datetime.now()
    if option == "hours":
        print(now.hour)
    elif option == "mins":
        print(now.minute)
    elif option == "secs":
        print(now.second)
    else:
        print(now.strftime("%H:%M:%S"))

def cat_file(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")

def head_file(filename):
    try:
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                if i == 5:
                    break
                print(line, end="")
    except FileNotFoundError:
        print("File not found.")

def tail_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines[-5:]:
                print(line, end="")
    except FileNotFoundError:
        print("File not found.")

def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print("File copied.")
    except FileNotFoundError:
        print("File not found.")

def remove_file(filename):
    try:
        os.remove(filename)
        print("File deleted.")
    except FileNotFoundError:
        print("File not found.")

def empty_file(filename):
    open(filename, 'w').close()
    print("File emptied.")

def ipconfig():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("IP Address:", ip_address)

def pwd():
    print(os.getcwd())

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def main():
    while True:
        cmd = input("myshell> ").strip().split()

        if not cmd:
            continue

        command = cmd[0]

        if command == "list":
            list_files()
        elif command == "dirs":
            list_dirs()
        elif command == "date":
            show_date()
        elif command == "time":
            if len(cmd) > 1:
                show_time(cmd[1])
            else:
                show_time()
        elif command == "cat":
            if len(cmd) > 1:
                cat_file(cmd[1])
            else:
                print("Usage: cat <filename>")
        elif command == "head":
            if len(cmd) > 2 and cmd[1] == "-5":
                head_file(cmd[2])
            else:
                print("Usage: head -5 <filename>")
        elif command == "tail":
            if len(cmd) > 2 and cmd[1] == "-5":
                tail_file(cmd[2])
            else:
                print("Usage: tail -5 <filename>")
        elif command == "copy_file":
            if len(cmd) > 2:
                copy_file(cmd[1], cmd[2])
            else:
                print("Usage: copy_file <src> <dest>")
        elif command == "remove_file":
            if len(cmd) > 1:
                remove_file(cmd[1])
            else:
                print("Usage: remove_file <filename>")
        elif command == "empty_file":
            if len(cmd) > 1:
                empty_file(cmd[1])
            else:
                print("Usage: empty_file <filename>")
        elif command == "ipconfig":
            ipconfig()
        elif command == "pwd":
            pwd()
        elif command == "clear":
            clear_screen()
        elif command == "exit":
            break
        else:
            print("Unknown command:", command)

if __name__ == "__main__":
    main()

#!/usr/bin/env python
import os
import sys
from colorama import Fore, Back, Style

def error(message):
    return f'{Back.RED}{Fore.WHITE}{message}{Style.RESET_ALL}'

def detect_file(file):
    if '.' in file:
        return True
    else:
        return False

argvs = sys.argv
argvs.pop(0)

if len(argvs) == 0 or len(argvs) > 2:
    if len(argvs) == 0:
        print(error('ERROR: No arguments given.'))
    else:
        print(error('ERROR: Too many arguments given.'))
    print(error('Usage: pfm <path> <start-directory(OPTIONAL)>'))
    print('Use "pfm --help" for more information.')
    sys.exit(1)
if argvs[0] == '-h' or argvs[0] == '--help':
    print('USAGE: pfm [path] [start-folder (if you want to start from a specific folder)]')
    print('Example One: pfm /folder1/folder2/folder3/file.txt\nExample Two: python3 pfm /folder1/folder2/folder3/file.txt /folder1/folder2/folder3\n')
    sys.exit(0)

path = argvs[0].split('/')
if len(argvs) == 2:
    if os.path.exists(argvs[1]):
        start_folder = argvs[1]
        os.chdir(start_folder)
        print(f"Start folder: {start_folder}")
    else:
        print('error: start folder does not exist')
        sys.exit(1)
else:
    start_folder = os.getcwd()
    os.chdir(start_folder)
    print(f"start_folder: {start_folder}")

if len(path) == 1:
    if not os.path.exists(path[0]):
        if detect_file(path[0]):
            with open(path[0], 'w') as f:
                f.write('')
        else:
            os.mkdir(path[0])
    else:
        print(f'"{path[0]}" already exists')
else:
    for i in range(len(path) - 1):
        if os.path.exists(path[i]):
            print(f'{path[i]} already exists')
            os.chdir(path[i])
        else:
            print(f'Creating {path[i]}...')
            os.mkdir(path[i])
            os.chdir(path[i])

    print(f'Creating {path[-1]}...')

    if detect_file(path[-1]):
        print(f'{path[-1]} is a file')
        with open(path[-1], 'w') as f:
            f.write('')
    else:
        print(f'{path[-1]} is a folder')
        os.mkdir(path[-1])


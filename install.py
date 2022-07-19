#!/usr/bin/env python
import os
import shutil

repo_files = os.listdir(".")
os.system("pip install -r requirements.txt")
os.system("pyinstaller --onefile --name=pfm path-maker.py")

shutil.move('dist/pfm', '/usr/local/bin/pfm')
for i in os.listdir("."):
      if i not in repo_files:
         if os.path.isdir(i):
            shutil.rmtree(i)
         else:
            os.remove(i)
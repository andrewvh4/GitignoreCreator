'''
To Compile to exe:
pip install pyinstaller
pyinstaller gitignoreCreator.py --onefile
'''
import os

for file in os.listdir():
	if ".gitignore" in file:
		print(file)
		os.rename(file, ".gitignore")
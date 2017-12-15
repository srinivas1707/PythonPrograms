import os
name = "sri.txt"
if os.path.isfile(name):
    print("file does exist at this time")
else:
    print("no such file")

import os
fpath = ""
for dirpath, dirnames, filenames in os.walk(fpath):
    print("directory:", dirpath)
    print("subdirectories:", dirnames)
    print("files:", filenames)
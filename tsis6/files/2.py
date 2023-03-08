import os
fpath = ""
if not os.path.exists(fpath):
    print ("path do not exist")
else:
    print(os.access(fpath, os.R_OK))
    print(os.access(fpath, os.W_OK))
    print(os.access(fpath, os.X_OK))
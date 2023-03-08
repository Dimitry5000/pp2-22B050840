import os
fname = ""
fpath = ""
dname = ""
if not os.path.exists(fpath):
    print ("path do not exist")
else:
    print(os.path.isfile(os.path.join(fpath, fname)))
    print(os.path.isdir(os.path.join(fpath, dname)))
    

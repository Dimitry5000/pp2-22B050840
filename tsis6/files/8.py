import os
fname = "anyfile.txt"
if os.access(os.getcwd(), os.W_OK):
    os.remove(fname)
import os

path = r"C:/Users/Sanya/Desktop/PP2/PP2.2024/lab6/dirandfiles"

exists = os.path.exists(path)
readable = os.access(path, os.R_OK)
writable = os.access(path, os.W_OK)
executable = os.access(path, os.X_OK)

print("Path exists:", exists)
if exists:
    print("Readable:", readable)
    print("Writable:", writable)
    print("Executable:", executable)
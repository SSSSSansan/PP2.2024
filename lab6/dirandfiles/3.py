import os

path = "C:/Users/Sanya/Desktop/PP2/PP2.2024/lab6/dirandfiles/la.txt"

exists = os.path.exists(path)

if exists:
    print("Path exists.")
    directory, filename = os.path.split(path)
    print("Directory:", directory)
    print("Filename:", filename)
else:
    print("Path does not exist.")
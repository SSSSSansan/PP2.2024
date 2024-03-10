import os
file_path = "C:/Users/Sanya/Desktop/PP2/PP2.2024/lab6/dirandfiles/del.txt"

if not os.path.exists(file_path):
        print("File does not exist.")
else:
        os.remove(file_path)
        print("File deleted successfully.")

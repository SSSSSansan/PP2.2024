import os
path = "C:/Users/Sanya/Desktop/PP2/PP2.2024/lab6/dirandfiles/words.txt"
with open(path, 'r') as file:
            line_count = len(file.readlines())

print("Number of lines in the file:",line_count)



path = "C:/Users/Sanya/Desktop/PP2/PP2.2024/lab6/dirandfiles/copy.txt"
path1 ="C:/Users/Sanya/Desktop/PP2/PP2.2024/lab6/dirandfiles/copy2.txt"
with open(path, 'r') as source_file:
        content = source_file.read()
with open(path1, 'w') as destination_file:
        destination_file.write(content)
print("File content copied successfully.")
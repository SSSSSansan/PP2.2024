list = ['apple', 'banana', 'orange']

path = "C:/Users/Sanya/Desktop/PP2/PP2.2024/lab6/dirandfiles/list.txt"
with open(path, 'w') as file:
        for item in list:
            file.write(str(item) + '\n')
print("List has been successfully written to the file.")
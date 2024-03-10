import string, os

folder_path = "C:/Users/Sanya/Desktop/PP2/PP2.2024/lab6/dirandfiles"

for letter in string.ascii_uppercase:
    file_name = letter + ".txt"
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as file:
            file.write("This is the content of " + file_name)
            print(f"File '{file_name}' has been created successfully.")
  
with open("sample.txt", "w") as file:
    file.write("This is a sample text file.\n")
    file.write("It contains same text for demonstration purposes. \n")
    file.write("You can add more lines as needed.\n")
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content: ")
    print(content)
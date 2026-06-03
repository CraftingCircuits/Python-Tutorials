# Closing file
file = open("one.txt", "r")
print(file.read())
file.close()

# renaming and deleting files
# rename() method to rename a file in python - it is required to import module os
import os

# os.rename("file2.txt", "file1.txt")
# print("File is renamed")


# removing the file using remove() method
import os

os.rename("myfile.txt")
print("File is removed")

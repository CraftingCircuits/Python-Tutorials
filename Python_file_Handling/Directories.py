# finding file position
input_file = open("fileDemo1.txt")
print(input_file.read())
print("The current position is ...")
print(input_file.tell())
input_file.seek(0)
print("The current position is ...")
print(input_file.tell())


# understanding directories
# import os

# getting working directory
# print(os.getcwd())
# create a new directory
# os.mkdir("New_folder")
# list file and folders
# print(os.listdir("ToDoApp"))
# going back to previous directory
# os.chdir("..")
# remove a directory
# os.rmdir("New_folder")

# Binary files
# file = open("myfile.bin", "rb")
# data = list(file.read())
# print(data)
# file.close()

# writing data in binary file using write() function
# bytearray() - returns byte representation of the object
# write() - used to write the byte array to a binary file
file1 = open("myfile.bin", "wb")
data1 = [10, 20, 30, 40, 50]
array = bytearray(data1)
file1.write(array)
file1.close()

file1 = open("myfile.bin", "rb")
data = file1.read()
print(list(data))
file1.close()

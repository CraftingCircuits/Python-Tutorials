# write a python program to write the contents in 'one.txt' file. read these contents and write them to another file named 'two.txt'.
print("\n")
n = int(input("Enter number of lines to write to the file 'one.txt': "))
outfile = open("one.txt", "w")
for i in range(n):
    line = input("Enter line: ")
    outfile.write(line + "\n")
outfile.close()
infile = open("one.txt", "r")
outfile2 = open("two.txt", "w")
i = 0
for i in range(n + 1):
    line = infile.readline()
    outfile2.write(line + "\n")
infile.close()
outfile2.close()
print("\n")
print("Contents of the file 'two.txt' are: ")
infile2 = open("two.txt", "r")
content2 = infile2.read()
print(content2)
infile2.close()

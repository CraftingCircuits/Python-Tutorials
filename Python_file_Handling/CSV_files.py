# CSV files - comma separated value.
# import csv

# file = open("student.csv", "r")
# # print(file.read())
# reader = csv.reader(file, delimiter="#")
# for row in reader:
#     print(row)
# file.close()
# it can also be done using with statement
# import csv
# with open("student.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# reading file with different delimiter
# import csv

# with open("student.csv", "r") as file:
#     reader = csv.reader(file, delimiter="#")
#     for row in reader:
#         print(row)

# writing csv file
import csv

with open("student.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow("5. Rajesh Patel")
    writer.writerow("6. Dharmesh lokhande")

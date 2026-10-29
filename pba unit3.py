import csv

total = 0
count = 0

with open("/Users/harshbhagat/students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += float(row["Marks"])
        count += 1

if count > 0:
    average = total / count
    print("Average Marks:", average)
else:
    print("No student records found.")
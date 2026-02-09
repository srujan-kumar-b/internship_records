import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    print("Students who Passed:")
    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])

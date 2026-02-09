import csv  
import openpyxl

file = open("sample.txt", "w")
file.write("Hello, this is a file handling example. srujan")
file.close()

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")

with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], row[1], row[2])

workbook = openpyxl.load_workbook("data.xlsx")
sheet = workbook.active
for row in sheet.iter_rows(values_only=True):
    print(row)
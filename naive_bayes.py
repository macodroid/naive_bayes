import csv

csv_name = 'exams.csv'
header = []
data = []
table = []
with open(csv_name, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        data.append(row)

for row in data:
    table_row = {}
    for r in range(len(row)):
        table_row[header[r]] = row[r]
    table.append(table_row)


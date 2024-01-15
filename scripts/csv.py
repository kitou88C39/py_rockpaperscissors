import csv

with open('sample.csv', mode='f') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

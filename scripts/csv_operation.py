#sample1
import csv

with open('sample.csv', mode='r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#sample2
import csv

data = '''11 12 13 14
21 22 23 24
31 32 33 34
'''

with open('sample.csv', mode='r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        print(row)

##CSVのライブラリを使った書き込み
#sample1
import csv

data = [41,42,43,44]

with open('sample.csv', mode='a+', newline='') as f:
    write = csv.write(f)
    write.writerow(data)

    f.seek(0)
    print(f.read())

# DICTReaderを使ったコード
import csv

num_rows = [
    [11, 12, 13, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34]
]

with open('sample.csv', mode='w+') as f:
    writer = csv.writer(f)
    for row in num_rows:
    f.seek(0)
    reader = csv.DictReader(f,fieldnames=["ONE", "TWO", "THREE", "FOUR"])
    for row in reader:
        print(row)

# DICTWriterを使ったコード
import csv

num_rows = [
    [11, 12, 13, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34]
]

with open('sample.csv', 'a+' newline='') as f:
    writer = csv.DictWriter(f,fieldnames=["ONE", "TWO", "THREE", "FOUR"])
    writer.writerow({"ONE:41", "TWO:42", "THREE:43", "FOUR:44"})
    f.seek(0)
    reader = csv.DictReader(f,fieldnames=["ONE", "TWO", "THREE", "FOUR"])
    for row in reader:
        print(row)

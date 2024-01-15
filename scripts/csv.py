import csv

data = '''
11,12,13,14
21,22,23,24
'''

with open("sample.csv",mode="w") as f:
    f.write(data)
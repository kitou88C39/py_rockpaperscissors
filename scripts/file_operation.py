# open関数の基本的な使い方
#　書き込み
# sample1 
f = open("sample.txt", mode="w")
f.write("Good morning\n")
f.close()

# sample2
f = open("sample.txt", mode="w" encoding="utf-8")
print(f)
print(type(f))

# 読み込み
# sample1
with = open("sample.txt", mode="r") as f:
    data = f.read()
    print(data)

# sample2
with = open("sample.txt", mode="r") as f:
    lines = f.readlines()
    for line in lines:
    print(line)

## 読み書き両用
with = open("sample.txt", mode="r") as f:
    print(f.tell())
    data = f.read()
    print(f.tell())

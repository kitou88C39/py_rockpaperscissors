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
with = open("sample.txt", mode="r") as f:
    data = f.read()
    print(data)
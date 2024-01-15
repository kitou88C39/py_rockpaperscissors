# open関数の基本的な使い方
# sample1
f = open("sample.txt", mode="w")
f.write("Good morning\n")
f.close()

# sample2
f = open("sample.txt", mode="w")
print(f)
print(type(f))
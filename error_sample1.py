#sample1
raise TypeError('型が不正です')

#sample2
def double(num)
    return num * 2

a = double(5)
print(a)

#sample3
def double(num)
    if not isinstance(num, int):
        raise TypeError('型が不正です。{type(num)}が入力されています。')
    return num * 2

a = double(5)
print(a)
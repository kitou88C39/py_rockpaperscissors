# sample1
num = [0, 1, 2]

try:
    print(nume[3])
except IndexError:
    print('要素が3つ以下です')

print('Finish')

# sample2
num = [0, 1, 2]

try:
    print(nume[3])
except IndexError as e:
    print(e)
    print(type(e))
    print('要素が3つ以下です')

print('Finish')

# sample3
um = [0, 1, 2]

try:
    a = 1 / 0
    print(a)
    print(nume[3])
except IndexError as e:
    print(e)
    print(type(e))
    print('要素が3つ以下です')

print('Finish')

# sample4
um = [0, 1, 2]

try:
    a = 1 / 0
    print(a)
    print(nume[3])
except ZeroDivisionError as e:
    print(e)
    print(type(e))

print('Finish')

# sample5
um = [0, 1, 2]

try:
    a = 1 / 0
    print(a)
    print(nume[3])
except (ZeroDivisionError, IndexError) as e:
    print(e)
    print(type(e))
    print('要素が3つ以下です')

print('Finish')

# sample6
um = [0, 1, 2]

try:
    a = 1 / 0
    print(a)
    print(nume[3])
except ZeroDivisionError as e:
    print(e)
    print(type(e))
    print('0で割れない')
except IndexError as e:
    print(e)
    print(type(e))
    print('要素が3つ以下です')

print('Finish')
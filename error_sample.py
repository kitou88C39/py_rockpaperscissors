num = [0, 1, 2]

try:
    print(nume[3])
except IndexError:
    print('要素が3つ以下です')

print('Finish')
def degree(A, B):
    if (B == 1):
        return (A)
    else:
        return (A*degree(A, B - 1))


try:
    A = int(input('Введите число А '))
    B = int(input('Введите число B '))
    if (A < 0 or B < 0):
        raise
    elif (B == 0):
        print('1')
    else:
        print(degree(A, B))
except:
    print("Неккорекный ввод")

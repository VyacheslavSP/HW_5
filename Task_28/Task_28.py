def summ(a, b):
    if b == 0:
        return a
    else:
        b -= 1
        a += 1
        return summ(a, b)


try:
    a = int(input('Введите число a '))
    b = int(input('Введите число b '))
    if (a < 0 or b < 0):
        raise
    print(summ(a, b))
except:
    print("Неккорекный ввод")

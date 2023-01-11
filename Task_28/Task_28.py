def summ(a, b):
    if b == 0:
        return a
    else:
        b -= 1
        a += 1
        return summ(a, b)


print(summ(10, 100))

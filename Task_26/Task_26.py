
A = 2
B = 10


def degree(A, B):
    if (B == 1):
        return (A)
    else:
        return (A*degree(A, B - 1))


print(degree(A, B))

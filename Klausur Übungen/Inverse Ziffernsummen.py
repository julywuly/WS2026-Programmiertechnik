def ziffernsumme(zahl):
    s = 0
    for z in str(zahl):
        s += int(z)
    return s


def f(n, m):
    gefunden = []
    i = 1

    while len(gefunden) < m:
        if ziffernsumme(i) == n:
            gefunden.append(i)
        i += 1

    return gefunden[-1]


def s(k):
    result = 0

    for i in range(1, k + 1):
        result += f(i, i ** 2)

    return result

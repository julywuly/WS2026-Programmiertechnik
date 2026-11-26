def isPrim(zahl):
    if zahl < 2:
        return False
    for i in range(2, zahl//2+1):
        if zahl % i == 0:
            return False
    return True

def primfaktorenzerlegung(schranke, zahl):
    faktoren = 1
    loopzahl = zahl
    for i in range(2, schranke + 1):
        if isPrim(i):
            while loopzahl % i == 0:
                faktoren = faktoren * i
                loopzahl = loopzahl // i
                if faktoren == zahl:
                    return True
    return False

def ziffernsummeIsEven(zahl):
    sum = 0
    for i in str(zahl):
        sum = sum + int(i)
    if sum % 2 == 0:
        return True
    return False


def G(S, m, n):
    summe = 0
    for i in range(m, n + 1):
        if primfaktorenzerlegung(S, i) and ziffernsummeIsEven(i):
            summe = summe + i
    return summe

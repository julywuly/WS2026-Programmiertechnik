
def isPrim(zahl):
    for i in range(2, zahl):
        if zahl % i == 0:
            return False
    return True


def findNeighbourPrimeNumber(zahl):
    smaller = zahl
    larger = zahl
    isNeighbourSmall = 0
    isNeighbourLarge = 0

    while isNeighbourLarge == 0:
        larger = larger + 1
        if isPrim(larger):
            isNeighbourLarge += larger

    while isNeighbourSmall == 0:
        smaller = smaller - 1
        if isPrim(smaller):
            isNeighbourSmall += smaller

    if(zahl - smaller) == (larger - zahl) and (zahl == (smaller + larger) / 2):
        return True
    return False

def containsNo6(zahl):
    if str(zahl).__contains__("6"):
        return False
    return True


def A(n,m):
    sum = 0
    for i in range(n,m+1):
        if findNeighbourPrimeNumber(i) and isPrim(i) and containsNo6(i):
            sum += i
    return sum

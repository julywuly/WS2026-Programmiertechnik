def geradeZiffernsumme(zahl):
    sum = None
    for num in str(zahl):
        sum += int(num)

    if sum % 2:
        return True
    else:
        return False


def isPrim(zahl):
    for num in range(2, zahl):
        if zahl % num == 0:
            return False
    return True

def isStrongPrimeNumber(zahl, upper):
    for num in range(2, zahl - 1):
        if zahl % num != 0:
            smaller = num

    for num in range(zahl + 1, upper):
        if zahl % num != 0:
            larger = num

    mittel = arithmetischesMittel(smaller, larger)
    if mittel < zahl:
        return True
    else:
        return False


def countStronPrimeNumbers(lower, upper):
    strongandgeradePrimeNumbers = 0
    for num in range(lower, upper+1):
        if isPrim(num) and isStrongPrimeNumber(num, upper) and geradeZiffernsumme(num):
            strongandgeradePrimeNumbers += num

def arithmetischesMittel(num1, num2):
    return (num1 + num2) /2

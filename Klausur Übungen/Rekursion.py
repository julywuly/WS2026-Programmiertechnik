def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)

def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def ggt(a, b):
    if b == 0:
        return a
    return ggt(b, a % b)

def kgv(a, b):
    return (a * b) // ggt(a, b)

def nested_sum(array):
    summe = 0

    for element in array:
        if type(element) == int:
            summe += element
        elif type(element) == list:
            summe += nested_sum(element)

    return summe
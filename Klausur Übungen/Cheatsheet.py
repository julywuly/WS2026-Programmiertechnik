# =========================
# ARRAY / LIST FUNKTIONEN
# =========================

def search(array, x):
    """Sucht x im Array und gibt den Index zurück."""
    for i in range(len(array)):
        if array[i] == x:
            return i
    return None


def contains(array, x):
    """Prüft, ob x im Array vorkommt."""
    for element in array:
        if element == x:
            return True
    return False


def maximum(array):
    """Liefert das größte Element."""
    max_wert = array[0]

    for i in range(1, len(array)):
        if array[i] > max_wert:
            max_wert = array[i]

    return max_wert


def minimum(array):
    """Liefert das kleinste Element."""
    min_wert = array[0]

    for i in range(1, len(array)):
        if array[i] < min_wert:
            min_wert = array[i]

    return min_wert


def summe(array):
    """Berechnet die Summe aller Zahlen."""
    s = 0

    for zahl in array:
        s += zahl

    return s


def reverse(array):
    """Gibt eine umgedrehte Liste zurück."""
    neu = []

    for i in range(len(array) - 1, -1, -1):
        neu.append(array[i])

    return neu


def count(array, x):
    """Zählt wie oft x vorkommt."""
    anzahl = 0

    for element in array:
        if element == x:
            anzahl += 1

    return anzahl


# =========================
# STACK
# =========================

def push(stack, x):
    stack.append(x)


def pop(stack):
    if len(stack) == 0:
        return None

    return stack.pop()


def top(stack):
    if len(stack) == 0:
        return None

    return stack[-1]


def is_empty(stack):
    return len(stack) == 0


# =========================
# SORTIEREN
# =========================

def selection_sort(array, asc=True):
    U = array.copy()
    S = []

    while len(U) > 0:
        extrem = 0

        for i in range(1, len(U)):
            if asc:
                if U[i] < U[extrem]:
                    extrem = i
            else:
                if U[i] > U[extrem]:
                    extrem = i

        S.append(U.pop(extrem))

    return S


# =========================
# PRIMZAHLEN
# =========================

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def next_prime(n):
    kandidat = n + 1

    while not is_prime(kandidat):
        kandidat += 1

    return kandidat


# =========================
# REKURSION
# =========================

def rec_sum(array):
    if len(array) == 0:
        return 0

    return array[0] + rec_sum(array[1:])


def ggt(a, b):
    """Größter gemeinsamer Teiler."""
    if b == 0:
        return a

    return ggt(b, a % b)


def kgv(a, b):
    """Kleinstes gemeinsames Vielfaches."""
    return (a * b) // ggt(a, b)


# =========================
# GERADE / UNGERADE
# =========================

def is_even(n):
    if n == 0:
        return True

    return is_odd(n - 1)


def is_odd(n):
    if n == 0:
        return False

    return is_even(n - 1)


# =========================
# VERSCHACHTELTE LISTEN
# =========================

def sum_integers(array):
    """
    Addiert rekursiv alle Integer
    in verschachtelten Listen.
    """

    summe = 0

    for element in array:
        if type(element) == int:
            summe += element

        elif type(element) == list:
            summe += sum_integers(element)

    return summe


def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def fib_sum(n):
    summe = 0

    for i in range(n + 1):
        summe += fib(i)

    return summe

#Primfaktorenzerlegung
def prime_factors(n):
    faktor = 2

    while faktor <= n:
        while n % faktor == 0:
            print(faktor)
            n //= faktor

        faktor += 1

#Perfekte Zahl
def is_perfect(n):
    summe = 0

    for i in range(1, n):
        if n % i == 0:
            summe += i

    return summe == n

#Armstrong Zahlen
def is_armstrong(n):
    s = str(n)
    k = len(s)

    summe = 0

    for z in s:
        summe += int(z) ** k

    return summe == n

# =========================
# TESTS
# =========================

if __name__ == "__main__":

    print(search([3, 7, 5], 7))
    print(maximum([2, 8, 4]))
    print(reverse([1, 2, 3, 4]))

    stack = []
    push(stack, 10)
    push(stack, 20)

    print(top(stack))
    print(pop(stack))
    print(is_empty(stack))

    print(selection_sort([5, 2, 8, 1]))
    print(is_prime(13))
    print(next_prime(13))

    print(ggt(48, 18))
    print(kgv(12, 18))

    print(is_odd(7))
    print(is_even(8))

    print(sum_integers([1, [2, [3]], 4.44, [5, ["Hallo", 6]]]))
# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Die Zahl die untersucht werden soll wird an die untenstehende Funktion als Variable "x" übergeben.
# Die Variable "result" soll die Lösung als booleschen Wert enthalten.

def is_odd(x):
    result = None
    if x % 2 == 0:
        result = False
    else:
        result = True

    return result


def my_sum(x):
    sum = 0
    y = 3
    while y < x:
        sum += y
        y += 5
    print(sum)
    return sum


def get_min_max(a, b, c, d, e, f):
    _max_ = None
    _min_ = None

    zahlen = [a, b, c, d, e, f]

    for zahl in zahlen:
        if _max_ is None or zahl > _max_:
            _max_ = zahl
        if _min_ is None or zahl < _min_:
            _min_ = zahl

    return _min_, _max_


def count_loop(x):
    count = 0;

    if not is_odd(x):
        while x > 0:
            x = x // 2
            count += 1

    return count


def division_mit_rest(x, y):
    result = 0
    remainder = 0

    while x >= y:
        x = x - y
        result += 1

    remainder = x

    return result, remainder


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def is_triangular(x):
    sum = 0
    for i in range(1, x):
        sum += i
        if sum == x:
            return True
    return False


if __name__ == '__main__':
    is_triangular(7)

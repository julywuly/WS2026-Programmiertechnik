def get_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    return digits
#wenn man append(n) machen würde dann wäre die liste 145,45,5
def sum_of_square(n):
    digits = get_digits(n)
    sumDigits = 0

    for digit in digits:
        sumDigits = sumDigits + (digit * digit)

    return sumDigits

def is_square_number(l, n):
    sumSquareNumbers = 0

    for i in range(l, n + 1):
        num = sum_of_square(i)
        if num % len(get_digits(i)) == 0:
            sumSquareNumbers = sumSquareNumbers + i

    return sumSquareNumbers

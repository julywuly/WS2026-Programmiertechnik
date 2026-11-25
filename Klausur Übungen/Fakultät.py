# Berechnet die Fakultät einer Zahl.
# Beispiel:
# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
def factorial(n):
    result = 1

    # Multipliziere alle Zahlen von 1 bis n
    for i in range(1, n + 1):
        result = result * i

    return result


# Zerlegt eine Zahl in ihre einzelnen Ziffern.
# Beispiel:
# get_digits(145) -> [5, 4, 1]
def get_digits(n):
    digits = []

    # Solange noch Ziffern vorhanden sind
    while n > 0:

        # Letzte Ziffer anhängen
        digits.append(n % 10)

        # Letzte Ziffer entfernen
        n = n // 10

    return digits


# Findet alle Zahlen bis n, bei denen die Summe
# der Fakultäten ihrer Ziffern wieder die Zahl ergibt.
# Die Funktion gibt die Summe aller gefundenen Zahlen zurück.
def digits_factorial(n):

    # Hier wird die Summe aller gültigen Zahlen gesammelt.
    total_sum = 0

    # Beginne bei 10, da 1! = 1 und 2! = 2
    # laut Angabe nicht berücksichtigt werden sollen.
    for number in range(10, n + 1):

        # Zerlege die aktuelle Zahl in ihre Ziffern.
        # Beispiel:
        # 145 -> [5, 4, 1]
        digits = get_digits(number)

        # Hier speichern wir die Summe der Ziffernfakultäten.
        factorial_sum = 0

        # Gehe alle Ziffern der Zahl durch.
        for digit in digits:

            # Berechne die Fakultät der Ziffer
            # und addiere sie zur laufenden Summe.
            factorial_sum = factorial_sum + factorial(digit)

        # Prüfe, ob die Summe der Ziffernfakultäten
        # gleich der ursprünglichen Zahl ist.
        #
        # Beispiel für 145:
        # 1! + 4! + 5! = 145
        #
        # factorial_sum = 145
        # number = 145
        if factorial_sum == number:

            # Falls die Bedingung erfüllt ist,
            # addiere die Zahl zur Gesamtsumme.
            total_sum = total_sum + number

    # Gib die Summe aller gefundenen Zahlen zurück.
    return total_sum
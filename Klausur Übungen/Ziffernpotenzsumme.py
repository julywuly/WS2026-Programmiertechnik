# Importiert die bereits fertige Fakultätsfunktion aus dem Modul math.
# Beispiel:
# factorial(5) -> 120
from math import factorial


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


# Addiert zunächst alle Ziffern in der Liste
# und erhebt die Summe anschließend zur Potenz "power".
#
# Beispiel:
# digits = [5, 4, 1]
# power = 2
#
# (5 + 4 + 1)^2 = 10^2 = 100
def digit_power_sum(digits, power):
    digit_sum = 0

    # Addiere alle Ziffern
    for d in digits:
        digit_sum = digit_sum + d

    # Potenz berechnen und zurückgeben
    return digit_sum ** power


# Prüft, ob eine Zahl "interessant" ist.
#
# Die Idee:
# 1. Ziffern der Zahl bestimmen.
# 2. Summe der Ziffern berechnen.
# 3. Diese Summe mit verschiedenen Potenzen
#    (1, 2, 3, 4, ...) potenzieren.
# 4. Falls irgendwann wieder die ursprüngliche Zahl entsteht,
#    ist die Zahl interessant.
def is_interesting_number(n):

    # Ziffern der Zahl holen
    digits = get_digits(n)

    # Beginne mit Potenz 1
    power = 1

    # Ersten Wert berechnen
    value = digit_power_sum(digits, power)

    # Solange der Wert größer als 1 und
    # nicht größer als n ist
    while 1 < value <= n:

        # Wenn der berechnete Wert gleich der
        # ursprünglichen Zahl ist,
        # ist die Zahl interessant.
        if value == n:
            return True

        # Nächste Potenz ausprobieren
        power = power + 1

        # Neuen Wert berechnen
        value = digit_power_sum(digits, power)

    # Keine passende Potenz gefunden
    return False


# Soll alle interessanten Zahlen
# zwischen l und u zurückgeben.
def get_interesting_numbers(l, u):
    interesting_numbers = []

    # Gehe alle Zahlen im Bereich durch
    for n in range(l, u + 1):

        # HIER IST WAHRSCHEINLICH EIN FEHLER!
        # Momentan wird jede Zahl hinzugefügt,
        # egal ob sie interessant ist oder nicht.
        interesting_numbers.append(n)

        # Durch die Einrückung endet die Funktion
        # außerdem bereits nach dem ersten Schleifendurchlauf.
        return interesting_numbers
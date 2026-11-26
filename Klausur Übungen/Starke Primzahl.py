# ---------------------------------------------------------
# Funktion: geradeZiffernsumme
# Zweck:
# Berechnet die Summe aller Ziffern einer Zahl und prüft,
# ob diese Summe gerade ist.
#
# Beispiel:
# Zahl = 123
# Ziffernsumme = 1 + 2 + 3 = 6
# 6 ist gerade -> True
# ---------------------------------------------------------
def geradeZiffernsumme(zahl):

    # Variable für die Ziffernsumme
    # ACHTUNG:
    # Im Originalcode steht hier "None".
    # Das würde beim ersten "+=" einen Fehler erzeugen.
    # Deshalb wird die Summe mit 0 gestartet.
    sum = 0

    # Die Zahl wird in einen String umgewandelt.
    # Beispiel:
    # 123 -> "123"
    #
    # Dadurch kann über jede einzelne Ziffer iteriert werden.
    for num in str(zahl):

        # Die Ziffer liegt aktuell als Zeichen vor.
        # Beispiel:
        # '1', '2', '3'
        #
        # int() wandelt das Zeichen in eine Zahl um,
        # die anschließend zur Summe addiert wird.
        sum += int(num)

    # Prüfen, ob die Summe durch 2 teilbar ist.
    #
    # sum % 2 liefert:
    # 0 -> gerade
    # 1 -> ungerade
    if sum % 2 == 0:
        return True
    else:
        return False


# ---------------------------------------------------------
# Funktion: isPrim
# Zweck:
# Prüft, ob eine Zahl eine Primzahl ist.
#
# Primzahl:
# Eine natürliche Zahl > 1,
# die nur durch 1 und sich selbst teilbar ist.
#
# Beispiele:
# 2, 3, 5, 7, 11, 13 ...
# ---------------------------------------------------------
def isPrim(zahl):

    # Zahlen kleiner als 2 sind keine Primzahlen.
    if zahl < 2:
        return False

    # Alle Zahlen von 2 bis zahl-1 testen.
    for num in range(2, zahl):

        # Falls ein Teiler gefunden wird,
        # ist die Zahl keine Primzahl.
        if zahl % num == 0:
            return False

    # Wurde kein Teiler gefunden,
    # handelt es sich um eine Primzahl.
    return True


# ---------------------------------------------------------
# Funktion: isStrongPrimeNumber
# Zweck:
# Prüft, ob eine Primzahl eine starke Primzahl ist.
#
# Definition:
# Eine Primzahl p ist stark, wenn sie größer ist als
# das arithmetische Mittel ihrer benachbarten Primzahlen.
#
# Beispiel:
# Primzahlen:
# 11, 13, 17
#
# Mittelwert:
# (11 + 17) / 2 = 14
#
# 13 > 14 ?
# Nein -> keine starke Primzahl
# ---------------------------------------------------------
def isStrongPrimeNumber(zahl, upper):

    # Hier wird die vorherige Primzahl gesucht.
    smaller = None

    # Von 2 bis kurz vor zahl laufen
    for num in range(2, zahl):

        # Nur Primzahlen betrachten
        if isPrim(num):

            # Die zuletzt gefundene Primzahl speichern.
            # Dadurch steht am Ende die größte Primzahl
            # unterhalb von zahl in smaller.
            smaller = num

    # Hier wird die nächste größere Primzahl gesucht.
    larger = None

    # Von zahl+1 bis upper laufen
    for num in range(zahl + 1, upper):

        # Sobald die erste Primzahl gefunden wird,
        # handelt es sich um die nächste Nachbarprimzahl.
        if isPrim(num):
            larger = num
            break

    # Falls keine Nachbarprimzahlen gefunden wurden,
    # kann keine Aussage getroffen werden.
    if smaller is None or larger is None:
        return False

    # Arithmetisches Mittel berechnen
    mittel = arithmetischesMittel(smaller, larger)

    # Ist die aktuelle Primzahl größer als das Mittel,
    # handelt es sich um eine starke Primzahl.
    if zahl > mittel:
        return True
    else:
        return False


# ---------------------------------------------------------
# Funktion: countStronPrimeNumbers
# Zweck:
# Zählt alle Zahlen im Bereich [lower, upper],
# die gleichzeitig
#
# 1. Primzahlen sind
# 2. starke Primzahlen sind
# 3. eine gerade Ziffernsumme besitzen
# ---------------------------------------------------------
def countStronPrimeNumbers(lower, upper):

    # Zähler für passende Zahlen
    strongandgeradePrimeNumbers = 0

    # Alle Zahlen des Intervalls durchlaufen
    for num in range(lower, upper + 1):

        # Es müssen alle drei Bedingungen erfüllt sein.
        if (
            isPrim(num)
            and isStrongPrimeNumber(num, upper)
            and geradeZiffernsumme(num)
        ):

            # Zähler um 1 erhöhen
            strongandgeradePrimeNumbers += 1

    # Ergebnis zurückgeben
    return strongandgeradePrimeNumbers


# ---------------------------------------------------------
# Funktion: arithmetischesMittel
# Zweck:
# Berechnet den Durchschnitt zweier Zahlen.
#
# Formel:
# (a + b) / 2
# ---------------------------------------------------------
def arithmetischesMittel(num1, num2):

    return (num1 + num2) / 2


# ---------------------------------------------------------
# Beispielaufruf
# ---------------------------------------------------------

ergebnis = countStronPrimeNumbers(2, 100)

print(
    "Anzahl starker Primzahlen mit gerader Ziffernsumme:",
    ergebnis
)

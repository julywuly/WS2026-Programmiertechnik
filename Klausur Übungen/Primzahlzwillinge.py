def is_prime(zahl):
    if zahl < 2:
        return False
    for i in range(2, zahl//2+1):
        if zahl % i == 0:
            return False
    return True


def get_prime_list(n):             # Wir möchten unsere Primzahlen in eine Liste speichern. Würden wir hier eine
    j = 2                          # For-Loop verwenden, würden wir von zB 2 bis 10 durchiterieren. In der Angabe
    prime_list = []                # interessiert uns aber nicht das Intervall, in dem Primzahlen vorkommen, sondern
    while len(prime_list) < n:     # wir möchten eine ANZAHL an Primzahlen (im Beispiel wollen wir 6). Daher nehmen
        if is_prime(j):            # wir eine While-Loop, die solange die Iteration laufen lässt, bis in unserer leeren
            prime_list.append(j)   # Liste genug Werte (n-Werte) sind.
        j += 1
    return prime_list


def get_twin_pairs(prime_list):      # Nun wollen wir Paare bilden. Diese Paare haben aber die Bedingung, dass zwischen
    current_prime = prime_list[0]    # ihnen ein Abstand von 2 sein muss! Eine solche Bedingung können wir überprüfen,
    pairs = []                       # indem wir die Differenz berechnen = Subtraktion. 3-2 = 1 --> kein Abstand von 2!
    for next_prime in prime_list[1:]:      # Um eine Überprüfung machen zu können, speichern wir den ersten Wert an
        if next_prime - current_prime == 2:  # Index 0 in eine Variable.  In der For-Loop beginnen wir mit der Iteration
            pairs.append((current_prime, next_prime)) # bei Index 1. So können wir 3 - 2, 5 - 3, usw rechnen.
        current_prime = next_prime           # Ergibt sich ein Abstand von zwei, speichern wir in eine neue leere Liste
                                             # die Werte "(current_prime, next_prime)" ab.
    return pairs                             # Die extra Klammern nicht vergessen!



def sum_of_pairs(pairs):            # Die Paare sollen nun wieder in eine einzige Liste gespeichert werden.
    flattened_list = []             # Wir iterieren wieder mit einer For-Loop über "(x, y)" und führen zwei Mal
    for (x, y) in pairs:            # die append.-Funktion aus.
        flattened_list.append(x)
        flattened_list.append(y)

    return sum(set(flattened_list))   # Um uns mehr Schreibarbeit zu sparen, kicken wir mit dem set()-Konstruktor
                                      # (Set = mathematische Menge) jegliche Duplikate raus,
                                      # und summieren die verbleibende Werte in der Liste mit sum() auf.
                                      # Das return-Statement gibt dann die Summe zurück.

def twinPrimeSum(n):
    return sum_of_pairs(get_twin_pairs(get_prime_list(n)))
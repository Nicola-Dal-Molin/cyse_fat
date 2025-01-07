""" Esercizio per esercitarsi usando i comandi di Git
Tale esercizio permette di calcolare il fattoriale da una variabile """
def calcolo_fattoriale_ricorsivo(fattore, ini=1):
    # Caso base: se il fattore è 0 o 1, ritorna il risultato accumulato
    if fattore == 0 or fattore == 1:
        return ini
    # Chiamata ricorsiva con fattore decrementato e risultato aggiornato
    return calcolo_fattoriale_ricorsivo(fattore - 1, ini * fattore)

fattore = 4
start = 1
print(calcolo_fattoriale_ricorsivo(fattore, start))

    
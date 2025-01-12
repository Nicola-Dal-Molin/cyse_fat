"""
Esercizio per impratichirsi nel uso di git,
in tale esercizio si farà uso di python per calcolare il fattoriale in modo ricorsivo
"""

def fattoriale_ricorsivo(value):
    """Calcola il fattoriale di un numero in modo ricorsivo.

    Args:
        value: Il numero di cui calcolare il fattoriale.

    Returns:
        Il fattoriale del numero.
    """

    if value == 0:
        return 1  # Caso base: 0! = 1
    else:
        return value * fattoriale_ricorsivo(value - 1)
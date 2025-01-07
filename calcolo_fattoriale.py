""" Esercizio per esercitarsi usando i comandi di Git
Tale esercizio permette di calcolare il fattoriale da una variabile """

def calcolo_fattoriale(fattore=0): #di default è 1 se non gli viene passato niente
    if(fattore == 0):
        return 1
    result = 1
    for i in range(1, fattore+1): #attenzione che il range eslude l'estremo "destro"
        result = result * i
    return result

fattore = 4
print(calcolo_fattoriale(fattore))
    
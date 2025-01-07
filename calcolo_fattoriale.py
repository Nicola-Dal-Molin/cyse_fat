""" Esercizio per esercitarsi usando i comandi di Git
Tale esercizio permette di calcolare il fattoriale da una variabile """

fattore = 1

def calcolo_fattoriale(fattore=0): #di default è 1 se non gli viene passato niente
    if(fattore == 0):
        return 1
    result = 0
    for i in range(1, fattore):
        
    
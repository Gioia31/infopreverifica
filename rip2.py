  
nparole = input("Scrivere una lista di parole separate da virgole (es. parola1, parola2,..).\n") 
listap = nparole.split(", ") #ad ogni , e spazio divide la lista per poi contare le lettere di ogni singola parola IMPORTANTE
listalungp = []
for parola in listap:
    lunp = len(parola)
    listalungp.append(lunp)

print("La lunghezza delle parole è di ", listalungp)



  
print("Il seguente programma riconosce se la parola fornita è un pallindromo.")

pfornita = input("Inserire la parola: ")
pgirata = pfornita[::-1] #gira la stringa

if pfornita == pgirata:
    print(pfornita," è un pallindromo.")
else:
    print(pfornita," non è un pallindromo.")



  
V = "aeiou"
plingua = ""

while True:# x frase
    p = input("Inserire la prima parola della frase da trasformare: ")
    for lettera in p:
        if lettera in V:
            plingua = plingua + lettera
        else:
            plingua = plingua + lettera + "o" + lettera
    print("La paola ", p, " diventa: ", plingua)

    continuo = input("Vuoi continuare con un altra parola? si o no ? ")
    if continuo == "no":
        break



npart = int(input("Inserisci il totale dei partecipanti "))

while npart != 0:
    npart = npart-1
    nome = input("Inserisci il nome del partecipante ")
    listapart = []
    listapart.append(nome)

    vallancio = float(input("Inserisci il valore del lancio "))

vallanci = []
vallanci.append(vallancio)
massimo = max(vallanci)
print("Il valore massimo ottenuto nella gara è ", massimo, " complimenti !!")



  
lun = int(input("Da quante cifre è composto il numero binario? "))
espo = 0
ncifre = 0 #numero cifre passate dal while
nbinario = ""
ndecimale = 0

while ncifre != lun :
    ncifre = ncifre + 1
    cifra = input("Inserisci il valore della cifra a destra ")
    c = int(cifra)
    nbinario = nbinario + cifra
    ndecimale = ndecimale + (c*(2**espo))
    espo = espo + 1

print("Il numero binario fornito, con il sistema decimale, corrisponde a ",ndecimale )
print("Secondo le funzioni di Python il numero binario è uguale a", int(nbinario[::-1], base = 2))
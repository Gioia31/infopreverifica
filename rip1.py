'''def ---> serve per definire una funzione quindi creare un comando partendo da comandi che abbiamo già.
Una FUNZIONE è una raccolta di comandi; è molto versatile poichè rende il codice riutilizzabile '''

def print_n: 
    for i in range(3):
        print("ciao")

''' scrivendo solo      print_n()   richiamo la appena creata, e posso scriverslo ingiro per il codice'''

def print_n(n,t):
    for i in range(n):
        print(t)

print_n(3,"ciao")
''' si passano e inseriscono nella funzione sempre prima gli argomenti obbligatori poi quelli opzionali x una questione di SIGNATURE, in questo caso erano tutti obbligatori
Con argomenti opzionali:'''

# si chiama SIGNATURE 
def print_n(t, n = 1, U = False):   #n e U sono argom opzionali di DEFAULT n = 1 e U = False 
    if U == True:
        t = t.upper()
    for i i ìn range(n):
        print(t)

''' ma per passare l'argomento opzionale U, devo passare anche n?? NO. Per richiamare la funzione posso scrivere:'''
print_n("ciao", U = True)  '''passo il valore del determinato argomento '''

def differenza(a,b):
    return a - b

c = differenza(4,2)
#oppure
c = differenza(b = 4, a = 2)
''' l'istruzione return provoca il ritorno del controllo al programma principale o, in generale, alla funzione chiamante.




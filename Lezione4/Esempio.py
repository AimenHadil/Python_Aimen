# Esempio di dichiarazione e uso variabili
print("Scrivi il tuo nome, caro utente!")
# Per poter acquisire qualcosa che digita l'utente utilizzo la funzione imput()
# nome user = "Dario"
nomeUser = input() # Argomento mancante

print("Benvenuto", nomeUser)

# Faccio la stessa cosa in modo più veloce passando come arogmento all'input una frase  
# Funzione (argomento) --> tutto questo si chiama FIRMA DEL METODO 
cognomeUser = input ("Scrivi il tuo cognome..")
print("Il tuo cognome è", cognomeUser)

print("------NUMERI------")
# ATT: Tutto ciò che recupero da un utente è considerato una stringa, un testo. Per poter fare un calcolo devo fare il TYPE CASTING, ovvero forzare quella variabile ad essere un numero e non una stringa
Num1 = int( input("Scrivi un numero"))
Num2 = int( input("Scrivi un'altro numero"))
Somma = num1 + num2 
print("La somma vale: ", somma) 

# Esempio con int
Num3 = int("3") # Qui stiamo facendo il TYPE CASTING 
Num4 = 6
Somma2 = num3 + num4
print(somma2)
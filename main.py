import random

domande = open("domande.txt", "r")
punti = open("punti.txt", "r")
livelloMax = 0
#classe domanda con il testo, la difficoltà e le 4 possibili risposte, compresa quella corretta
class domanda:
    def __init__(self, testo, difficolta, risposta, rispostaS1, rispostaS2, rispostaS3):
        self.testo = testo
        self.difficolta = difficolta
        self.risposta = risposta
        self.rispostaS1 = rispostaS1
        self.rispostaS2 = rispostaS2
        self.rispostaS3 = rispostaS3

    def __str__(self):
        print(f" {self.testo} , {self.difficolta} , {self.risposta} , {self.rispostaS1} , {self.rispostaS2} , {self.rispostaS3}")

listaDomande = []
stringa = ""
#riscrivo tutto il file su una singola riga in modo da poter fare una split in base a dove si trova il simbolo di a capo
for line in domande:
    stringa += line

l = stringa.split("\n")

i=0
#array che conterrà tutti i valori necessari per creare un oggetto della classe domanda
b = ['','','','','','']

#scorro la stringa splittata elemento per elemento
for x in l:
    #se l'elemento è una riga vuota allora vuol dire che ho già analizzato le righe prima che contenevano le informazioni che mi servono e posso creare l'oggetto domanda e aggiungerlo alla lista delle domande
    #posso anche andare a controllare se il livello in esame è il piu alto o meno e in caso aggiornare la variabile livelloMax
    #azzero il contatore i in modo da poter ricominciare da capo nell'array
    if x == '':
        d = domanda(b[0], b[1], b[2], b[3], b[4], b[5])
        if int(b[1]) > int(livelloMax):
            livelloMax = int(b[1])
        listaDomande.append(d)
        i=0
        b = ['','','','','','']
    else:
        #se l'elemento non è una riga vuota allora posso inserirlo nel suo posto dell'array, indicato dal contatore i, che verrà poi aggiornato 
        b[i] = x
        i = i+1

#creo una lista vuota ma lunga tanto quanto è il livello massimo raggiungibile
lista = [None] * (livelloMax+1)

i=0

#riempo la lista creata prima di 0
for k in range(livelloMax+1):
    lista[i] = 0
    i = i + 1

i=0
#conto quante domande di ogni livello ci sono
while i < int(livelloMax+1):
    for d in listaDomande:
        if int(d.difficolta) == int(i):
            lista[i] = int(lista[i]) + 1
    i = i+1

errore = 0
print("Difficoltà massima raggiungibile: ", livelloMax)

punteggio = 0
diff = 0
c = 1

#qua faccio partire il ciclo che effettivamente farà funzionare il gioco
while errore == 0 and diff <= int(livelloMax):
    #indico la dofficioltà della domanda che verrà proposta
    print("Difficoltà ", diff, ":")
    #genero un numero a caso tra 1 e la quantità di domande di questo livello di difficoltà disponibili
    randomNum = random.randint(1, lista[diff])

    #accedo alla lista di tutte le domande
    for d in listaDomande:
        #controllo se la domanda ha la difficoltà giusta
        if int(d.difficolta) == diff:
            #controllo che la domanda sia quella indicata dal numero casuale generato prima
            if c == randomNum:

                #stampo la domanda e le risposte e chiedo di inserire la risposta 
                print(d.testo)
                print(d.risposta)
                print(d.rispostaS1)
                print(d.rispostaS2)
                print(d.rispostaS3)

                inserimento = input("Inserire la risposta: ")

                c=1
                #controllo la risposta inserita
                if inserimento == d.risposta:
                    diff = diff + 1
                    print("Complimenti, risposta esatta!")
                    punteggio = punteggio + 1
                else:
                    print("Hai sbagliato, fine del gioco!")
                    errore = 1
                break
            else:
                c = c+1


print("Il tuo punteggio finale è: ", punteggio)
nick = input("Inserisci il tuo nickname: ")
temp = open("temporaneo.thx", "w")
trovato = 0

for p in punti:
    p=p.strip("\n")
    riga=p.split(" ")
    nuovaR = ""

    if riga[0] == nick:
        nuovaR = nick + " " + str(punteggio) + "\n"
        temp.write(nuovaR)
        trovato = 1
    else:
        nuovaR = riga[0] + " " + riga[1] + "\n"
        temp.write(nuovaR)

if trovato == 0:
    temp.write(nick + " " + str(punteggio) + "\n")

temp.close()
punti.close()

scrivi = open("punti.txt", "w")
leggi = open("temporaneo.thx", "r")

for l in leggi:
    scrivi.write(l)

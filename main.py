from contextlib import nullcontext

domande = open("domande.txt", "r")
punti = open("punti.txt", "r")
livelloMax = 0
diff = 0

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
for line in domande:
    stringa += line

l = stringa.split("\n")

i=0
b = ['','','','','','']
for x in l:
    if x == '':
        d = domanda(b[0], b[1], b[2], b[3], b[4], b[5])
        if int(b[1]) > int(livelloMax):
            livelloMax = b[1]
        listaDomande.append(d)
        i=0
        b = ['','','','','','']
    else:
        b[i] = x
        i = i+1

errore = 0
print("Difficoltà massima raggiungibile: ", livelloMax)
punteggio = 0

while errore == 0 and diff <= int(livelloMax):
    print("Difficoltà ", diff, ":")
    for d in listaDomande:
        if int(d.difficolta) == diff:
            print(d.testo)
            print(d.risposta)
            print(d.rispostaS1)
            print(d.rispostaS2)
            print(d.rispostaS3)

            inserimento = input("Inserire la risposta: ")
            giusto = d.risposta
            break

    if inserimento == giusto:
        diff = diff + 1
        print("Complimenti, risposta esatta!")
        punteggio = punteggio +1
    else:
        print("Hai sbagliato, fine del gioco!")
        errore = 1

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

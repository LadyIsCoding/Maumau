import random
import time

Anwender = []
PC = []
Kartenfarben = ['Karo','Herz','Pik','Kreuz']
Kartenwerte = ['7','8','9','10','Bube', 'Dame', 'König', 'Ass']
Kartensatz = []
for i in Kartenfarben:
    for j in Kartenwerte:
        Kartensatz +=[[i,j]]

Kartensatz_Kopie = list(Kartensatz)

def Kartenziehen(Anzahl, liste):
    if len(liste) == 0:
        liste = mischen(Kartensatz_Kopie)
        print("Die Karten werden neu gemischt")
        Kartenziehen(Anzahl, liste)
    karten = random.sample(Kartensatz,k=Anzahl)
    for i in karten:
        liste.remove(i)
    return karten

def mischen(liste):
    kartensatz = [i for i in liste if i not in PC]
    kartensatz = [i for i in kartensatz if i not in Anwender]
    return kartensatz

def ziehen(Spieler,Anzahl,liste):
    gezogen = Kartenziehen(Anzahl,liste)
    Spieler.extend(gezogen)
    return gezogen

def wer_ist_dran(counter=2):
    if counter %2 == 0:
        return PC
    else:
        return Anwender

def spielzug_anwender(karte):
    print(f"Deine Karten: {Anwender}")
    eingabe = int(input("--->"))
    if eingabe == 0:
        blob = ziehen(Anwender,1,Kartensatz)
        print("Du hast folgende Karte gezogen: ", blob)
        legen= input("Diese Karte ablegen? Tippe j für ja oder n für no")
        if legen.lower() == "j":
            Anwender.pop()
            print("Du hast", blob, "gelegt.")
            return blob[0]
        else:
            return karte
    else:
        antwort = Anwender[(eingabe-1)]
        if antwort[0] == karte[0] or antwort[1] == karte[1]:
            karte = Anwender[(eingabe-1)]
            print(f"Du hast {karte} gelegt")
            Anwender.remove(antwort)
            return karte
        else:
            print("Ungültige Eingabe!")
            return karte

def spielzug_PC(karte):
    print("Der PC ist dran!")
    time.sleep(3)
    done = 0
    for i in PC:
        if i[0] == karte[0] or i[1] == karte[1]:
            print(f"Der Computer legt {i}")
            PC.remove(i)
            done = 1
            return i
        else:
            pass
    if done == 0:
        ziehen(PC, 1, Kartensatz)
        print("Der PC musste ziehen")
        return karte



#Spielbeginn
#Die Spieler erhalten jeweils 6 Karten:
Anwender = Kartenziehen(6,Kartensatz)
PC = Kartenziehen(6, Kartensatz)
obere_karte = Kartenziehen(1,Kartensatz)
obere_karte = obere_karte[0]
counter = (random.sample(range(2,10),1))[0]
#counter = counter[0]

eingabe0 = input("Bist du bereit? Drücke Enter, um zu beginnen.")
if eingabe0 =="":
    if counter %2 != 0:
        print(f"Du bist Spieler 1, deine Karten: {Anwender}")
    else:
        print(f"Du bist Spieler 2, deine Karten: {Anwender}")

print(f"\nSpieler 1 beginnt! \nWähle die passende Karte! Schreibe die Zahl der Karte oder 0 um zu ziehen! \nDie obere Karte auf dem Ablegestapel: {obere_karte}")


while True:
    print(obere_karte)
    if wer_ist_dran(counter)== PC:
        obere_karte= spielzug_PC(obere_karte)
        counter+=1
        if bool(PC) is False:
            print("Der PC hat gewonnen!")
            break
    else:
        obere_karte= spielzug_anwender(obere_karte)
        counter+=1
        if bool(Anwender) is False:
            print("Juhu, du hast gewonnen!")
            break
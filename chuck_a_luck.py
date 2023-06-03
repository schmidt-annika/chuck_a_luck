#-------------------------------------------------------------------------------
# Name:        Chuck_A_Luck
# Autor:       Annika Schmidt
#-------------------------------------------------------------------------------


from tkinter import *
from random import *
from tkinter.messagebox import showerror, showinfo
from tkinter.simpledialog import askstring

#Funktionen
def font_resize(): #Wenn sich die Fenstergröße ändert, dann muss sich auch die Fontgröße ändern
    if int(konto_label.cget("text")) < 10: #einstelliger Kontoinhalt
        konto_label.config(font = ("Helvetica",
                                   schriftgroeße_konto_setzen))
    elif int(konto_label.cget("text")) > 9 and int(konto_label.cget("text")) < 99: #zweistelliger Kontoinhalt
        konto_label.config(font = ("Helvetica",
                                   round(schriftgroeße_konto_setzen*0.75)))
    elif int(konto_label.cget("text")) > 99: #dreistelliger Kontoinhalt
        konto_label.config(font = ("Helvetica",
                                   round(schriftgroeße_konto_setzen/2)))
        
    if int(gewinn_label.cget("text")) < 10:
        gewinn_label.config(font = ("Helvetica",
                                    schriftgroeße_gewinn))
    elif int(gewinn_label.cget("text")) > 9:
        gewinn_label.config(font = ("Helvetica",
                                    round(schriftgroeße_gewinn*0.75)))
    wuerfel_label1.config(font = ("Helvetica",
                                  schriftgroeße_wuerfel))
    wuerfel_label2.config(font = ("Helvetica",
                                  schriftgroeße_wuerfel))
    wuerfel_label3.config(font = ("Helvetica",
                                  schriftgroeße_wuerfel))
    auszahlen_button.config(font = ("Ariel",
                                    schriftgroeße_ariel,
                                    "bold"))
    wuerfel_button.config(font = ("Ariel",
                                  schriftgroeße_ariel,
                                  "bold"))
    setzen_label1.config(font = ("Helvetica",
                                 schriftgroeße_konto_setzen))
    setzen_label2.config(font = ("Helvetica",
                                 schriftgroeße_konto_setzen))
    setzen_label3.config(font = ("Helvetica",
                                 schriftgroeße_konto_setzen))
    setzen_label4.config(font = ("Helvetica",
                                 schriftgroeße_konto_setzen))
    setzen_label5.config(font = ("Helvetica",
                                 schriftgroeße_konto_setzen))
    setzen_label6.config(font = ("Helvetica",
                                 schriftgroeße_konto_setzen))
    
    weniger_button1.config(font = ("Ariel",
                                   schriftgroeße_ariel,
                                   "bold"))
    weniger_button2.config(font = ("Ariel",
                                   schriftgroeße_ariel,
                                   "bold"))
    weniger_button3.config(font = ("Ariel",
                                   schriftgroeße_ariel,
                                   "bold"))
    weniger_button4.config(font = ("Ariel",
                                   schriftgroeße_ariel,
                                   "bold"))
    weniger_button5.config(font = ("Ariel",
                                   schriftgroeße_ariel,
                                   "bold"))
    weniger_button6.config(font = ("Ariel",
                                   schriftgroeße_ariel,
                                   "bold"))
    mehr_button1.config(font = ("Ariel",
                                   schriftgroeße_ariel,
                                   "bold"))
    mehr_button2.config(font = ("Ariel",
                                   schriftgroeße_ariel,
                                   "bold"))
    mehr_button3.config(font = ("Ariel",
                                   schriftgroeße_ariel,
                                   "bold"))
    mehr_button4.config(font = ("Ariel",
                                   schriftgroeße_ariel,
                                   "bold"))
    mehr_button5.config(font = ("Ariel",
                                   schriftgroeße_ariel,
                                   "bold"))
    mehr_button6.config(font = ("Ariel",
                                   schriftgroeße_ariel,
                                   "bold"))
    setzen_entry1.config(font = ("Ariel",
                                 schriftgroeße_setzen))
    setzen_entry2.config(font = ("Ariel",
                                 schriftgroeße_setzen))
    setzen_entry3.config(font = ("Ariel",
                                 schriftgroeße_setzen))
    setzen_entry4.config(font = ("Ariel",
                                 schriftgroeße_setzen))
    setzen_entry5.config(font = ("Ariel",
                                 schriftgroeße_setzen))
    setzen_entry6.config(font = ("Ariel",
                                 schriftgroeße_setzen))
    

def resize(e):
    global fenster_breite #die Variablen sollen gobalisiert werden
    global fenster_hoehe
    global schriftgroeße_wuerfel
    global schriftgroeße_konto_setzen
    global schriftgroeße_gewinn
    global schriftgroeße_ariel
    global schriftgroeße_setzen
    if int(e.width) > 500: #Schwankungen in den Werten von e, die aussoertiert werden müssen
        fenster_breite = int(e.width)
    if int(e.height) > 500:
        fenster_hoehe = int(e.height)
    #Die Schriftgröße muss relativ zum Fenster sein
    schriftgroeße_wuerfel = int(fenster_breite//6)
    schriftgroeße_konto_setzen = int(fenster_breite//7)
    schriftgroeße_gewinn = int(fenster_breite//15)
    schriftgroeße_ariel = int(fenster_breite//75)
    schriftgroeße_setzen = int(fenster_breite//45)
    if fenster_breite - fenster_hoehe > 200:
        schriftgroeße_wuerfel = int(fenster_hoehe//4)
        schriftgroeße_konto_setzen = int(fenster_hoehe//5)
        schriftgroeße_gewinn = int(fenster_hoehe//10)
        schriftgroeße_ariel = int(fenster_hoehe//50)
        schriftgroeße_setzen = int(fenster_hoehe//30)
    font_resize()    
    

def startbetrag(): #Die Menge an Geld, mit der man das Spiel beginnt
    betrag = askstring(title = "Einzahlen", prompt = "Mit wieviel Geld willst du starten?")
    konto_label.config(text = betrag)
    if int(konto_label.cget("text")) < 10:
        konto_label.config(font = ("Helvetica",
                           schriftgroeße_konto_setzen))
    elif int(konto_label.cget("text")) > 9 and int(konto_label.cget("text")) < 99:
        konto_label.config(font = ("Helvetica",
                round(schriftgroeße_konto_setzen*0.75)))
    elif int(konto_label.cget("text")) > 99:
        konto_label.config(font = ("Helvetica",
                                   round(schriftgroeße_konto_setzen/2)))
    return
    
def auf_null_setzen():
    setzen_entry1.delete(0, "end")
    setzen_entry2.delete(0, "end")
    setzen_entry3.delete(0, "end")
    setzen_entry4.delete(0, "end")
    setzen_entry5.delete(0, "end")
    setzen_entry6.delete(0, "end")
    setzen_entry1.insert(0, "0")
    setzen_entry2.insert(0, "0")
    setzen_entry3.insert(0, "0")
    setzen_entry4.insert(0, "0")
    setzen_entry5.insert(0, "0")
    setzen_entry6.insert(0, "0")
    
def liste_erstellen(): #Liste mit Infos darüber, wie viel der Spieler auf jede der 6 Zahlen gesetzt hat
    liste = [setzen_entry1.get(),
             setzen_entry2.get(),
             setzen_entry3.get(),
             setzen_entry4.get(),
             setzen_entry5.get(),
             setzen_entry6.get()]
    
    for i in range(0, len(liste)):
        if liste[i] == "":
            liste[i] = "0"
        liste[i] = int(liste[i])
    return liste
    
def wuerfel_button_click(wiederholung=0, liste_setzen = []): #Großteil der Spielmechanik folgt nun
    if wiederholung == 0:
        liste_setzen = liste_erstellen()
        if sum(liste_setzen) > int(konto_label.cget("text")): #Falls mehr Geld gesetzt wird, als man geld auf dem Konto hat
            showerror(title = "Fehler!",
                      message = "Du darfst nicht mehr Geld setzen, als auf deinem Konto ist.")
            return
        else:
            konto_zahl = int(konto_label.cget("text"))
            einsaetze_summe = sum(liste_setzen)
            konto_label.config(text = str(konto_zahl - einsaetze_summe))
    wuerfel_label1.config(fg = "grey")
    wuerfel_label2.config(fg = "grey")
    wuerfel_label3.config(fg = "grey")
    if wiederholung < 10: #Der Würfel wird mehrmals geändert und langsamer, bis das tatsächliche Ergebnis erscheint
        wuerfel1 = choice(wuerfel_liste)
        wuerfel2 = choice(wuerfel_liste)
        wuerfel3 = choice(wuerfel_liste)
        wuerfel_label1.config(text = wuerfel1)
        wuerfel_label2.config(text = wuerfel2)
        wuerfel_label3.config(text = wuerfel3)
        fenster.after(wiederholung * 100, wuerfel_button_click, wiederholung+1, liste_setzen) #Rekursion: Nach 0-10 Sekunden wird die Funktion erneut aufgerufen, nur mit wiederhlung +1, dadurch wird automatisch die Frequenz, in der die Bilder geändert werden, kleiner
    else:
        wuerfel_label1.config(fg = "black") #Die Würfel werden schwarz, da Würfelzyklus abgefertigt ist
        wuerfel_label2.config(fg = "black")
        wuerfel_label3.config(fg = "black")
        index1 = wuerfel_liste.index(wuerfel_label1.cget("text"))
        index2 = wuerfel_liste.index(wuerfel_label2.cget("text"))
        index3 = wuerfel_liste.index(wuerfel_label3.cget("text"))
        gewinn_ermitteln(index1 + 1, index2 + 1, index3 + 1, liste_setzen) #Nach dem Würfeln geht es nun darum, den Gewinn des Spielers zu ermitteln

def gewinn_ermitteln(a, b, c, liste_menge): #Hier wird der Gewinn ermittelt
    def okay_button_click():
        konto_plus = int(gewinn_label.cget("text"))
        gewinn_insgesamt = int(gewinn_label6_klein.cget("text"))
        gewinn_label.config(text = ("+" + str(gewinn_insgesamt + konto_plus)))
        if int(gewinn_label.cget("text")) < 10:
            gewinn_label.config(font = ("Helvetica",
                                        schriftgroeße_gewinn))
        elif int(gewinn_label.cget("text")) > 9:
            gewinn_label.config(font = ("Helvetica",
                                        round(schriftgroeße_gewinn*0.75)))
        auf_null_setzen()
        if konto_label.cget("text") == "0" and gewinn_label.cget("text") == "+0":
            showinfo(title = "Verzockt!", message = "Dein Konto ist leer, das Spiel wird neu gestartet.")
            konto_label.config(text = "3")
            rechnung.destroy()
            startbetrag()
        else:
            rechnung.destroy()
    #Hier wird der Gewinn berechnet
    gewinn_einsatz = 0 #Der Einsatz, den man zurückbekommt
    gewinn1 = 0 #Der Gewinn, den man mit dem ersten Würfel macht
    gewinn2 = 0 #Der Gewinn, den man mit dem zweiten Würfel macht
    gewinn3 = 0 #Der Gewinn, den man mit dem dritten Würfel macht
    gewinn_insgesamt = 0
    if a == b: #zwei Würfel sind gleich
        if b == c: #Alle Würfel sind gleich
            gewinn_einsatz += liste_menge[a - 1]
        else:
            gewinn_einsatz += liste_menge[a - 1] + liste_menge[c - 1]
    elif b == c or c == a: #zwei Würfel sind gleich
        gewinn_einsatz += liste_menge[a - 1] + liste_menge[b - 1]
    else: #alle würfel sind verschieden
        gewinn_einsatz += liste_menge[a - 1] + liste_menge[b - 1] + liste_menge[c - 1] #Einsatz zurückbekommen
    if liste_menge[a - 1] != 0: #hat man auf diese Zahl gesetzte?
        gewinn1 = liste_menge[a - 1]
    if liste_menge[b - 1] != 0: #hat man auf diese Zahl gesetzte?
        gewinn2 = liste_menge[b - 1]
    if liste_menge[c - 1] != 0: #hat man auf diese Zahl gesetzte?
        gewinn3 = liste_menge[c - 1]
    gewinn_insgesamt = gewinn_einsatz + gewinn1 + gewinn2 + gewinn3
    
    #Nach der Berechnung folgt nun die graphische Darstellung, damit der Spieler transperent weiß, woher sein Gewinn kommt
    rechnung = Tk() #Fenster erstellen
    rechnung.title("Deinen Gewinn ermitteln!")
    rechnung.iconbitmap("pik_favicon.ico") #das Favicon zu einem Pik ändern
    rechnung.geometry("500x500+50+50") #Größe und Position auf Bildschirm bestimmen
    rechnung.resizable(False, False) #Dieses Fenster hat eine fixe Größe, es kann nicht gößer oder kleiner gezogen werden
    rechnung.attributes("-topmost",True) #Es soll immer als oberstes stehen, damit der Spieler gezwungen ist, es zu beachten, anstatt einfach weiter zu spielen
    
    augenzahl_label_klein = Label(master = rechnung,
                                  text = "Augenzahl",
                                  font = ("Segoe UI", schriftgroeße_segoe_klein))
    gewinn_label_klein = Label(master = rechnung,
                               text = "Gewinn",
                               font = ("Segoe UI", schriftgroeße_segoe_klein))
    einsatz_label_klein = Label(master = rechnung,
                                text = "Einsatz",
                                font = ("Segoe UI", schriftgroeße_segoe_klein))
    
    augenzahl_label1_klein = Label(master = rechnung,
                                   text = wuerfel_label1.cget("text"),
                                   font = ("Ariel", schriftgroeße_wuerfel_klein))
    augenzahl_label2_klein = Label(master = rechnung,
                                   text = wuerfel_label2.cget("text"),
                                   font = ("Ariel", schriftgroeße_wuerfel_klein))
    augenzahl_label3_klein = Label(master = rechnung,
                                   text = wuerfel_label3.cget("text"),
                                   font = ("Ariel", schriftgroeße_wuerfel_klein))
    
    einsatz_label1_klein = Label(master = rechnung,
                                 text = str(liste_menge[a -1]),
                                 font = ("Ariel", schriftgroeße_zahlen_klein))
    einsatz_label2_klein = Label(master = rechnung,
                                 text = str(liste_menge[b -1]),
                                 font = ("Ariel", schriftgroeße_zahlen_klein))
    einsatz_label3_klein = Label(master = rechnung,
                                 text = str(liste_menge[c -1]),
                                 font = ("Ariel", schriftgroeße_zahlen_klein))
    
    gewinn_label1_klein = Label(master = rechnung,
                                text = str(gewinn1),
                                font = ("Ariel", schriftgroeße_zahlen_klein))
    gewinn_label2_klein = Label(master = rechnung,
                                text = str(gewinn2),
                                font = ("Ariel", schriftgroeße_zahlen_klein))
    gewinn_label3_klein = Label(master = rechnung,
                                text = str(gewinn3),
                                font = ("Ariel", schriftgroeße_zahlen_klein))
    gewinn_label4_klein = Label(master = rechnung,
                                text = str(gewinn_einsatz),
                                font = ("Ariel", schriftgroeße_zahlen_klein))
    gewinn_label5_klein = Label(master = rechnung,
                                text = str(gewinn_insgesamt - gewinn_einsatz),
                                font = ("Ariel", schriftgroeße_zahlen_klein))
    gewinn_label6_klein = Label(master = rechnung,
                                text = str(gewinn_insgesamt),
                                font = ("Ariel", schriftgroeße_zahlen_klein))
    addition_label1_klein = Label(master = rechnung,
                                  text = "+",
                                  font = ("Ariel", schriftgroeße_ariel_klein))
    addition_label2_klein = Label(master = rechnung,
                                  text = "+",
                                  font = ("Ariel", schriftgroeße_ariel_klein))
    addition_label3_klein = Label(master = rechnung,
                                  text = "+",
                                  font = ("Ariel", schriftgroeße_ariel_klein))
    addition_label4_klein = Label(master = rechnung,
                                  text = "+",
                                  font = ("Ariel", schriftgroeße_ariel_klein))
    addition_label5_klein = Label(master = rechnung,
                                  text = "\u2193",
                                  font = ("Ariel", schriftgroeße_ariel_klein))
    addition_label6_klein = Label(master = rechnung,
                                  text = "\u2193",
                                  font = ("Ariel", schriftgroeße_ariel_klein))
    addition_label7_klein = Label(master = rechnung,
                                  text = "+",
                                  font = ("Ariel", schriftgroeße_ariel_klein))
    addition_label8_klein = Label(master = rechnung,
                                  text = "\u2192",
                                  font = ("Ariel", schriftgroeße_ariel_klein))
    okay_button_klein = Button(master = rechnung,
                      text = "Okay!",
                      font = ("Ariel",
                              schriftgroeße_ariel_klein),
                      command = okay_button_click)
    
    #Diesmal wird mit dem .grid-Layoutmenager gearbeitet
    augenzahl_label_klein.grid(row = 0, column = 0, padx = str(konstanter_abstand_klein))
    augenzahl_label1_klein.grid(row = 1, column = 0, padx = str(konstanter_abstand_klein))
    augenzahl_label2_klein.grid(row = 3, column = 0, padx = str(konstanter_abstand_klein))
    augenzahl_label3_klein.grid(row = 5, column = 0, padx = str(konstanter_abstand_klein))
    
    if a == b:
        if b == c: #Alle Würfel sind gleich
            addition_label1_klein.config(text = "\u2A09") #Kreuze, statt Plusse, als Zeichen dafür, dass der Einsatz nur einmal "zurückkommt"
            addition_label2_klein.config(text = "\u2A09")
        else:
            addition_label1_klein.config(text = "\u2A09")
    elif b == c or c == a:
        addition_label2_klein.config(text = "\u2A09")        
        
    einsatz_label_klein.grid(row = 0, column = 1, padx = str(konstanter_abstand_klein))
    einsatz_label1_klein.grid(row = 1, column = 1, padx = str(konstanter_abstand_klein))
    addition_label1_klein.grid(row = 2, column = 1, padx = str(konstanter_abstand_klein))
    einsatz_label2_klein.grid(row = 3, column = 1, padx = str(konstanter_abstand_klein))
    addition_label2_klein.grid(row = 4, column = 1, padx = str(konstanter_abstand_klein))
    einsatz_label3_klein.grid(row = 5, column = 1, padx = str(konstanter_abstand_klein))
    addition_label5_klein.grid(row = 6, column = 1, padx = str(konstanter_abstand_klein))
    gewinn_label4_klein.grid(row = 7, column = 1, padx = str(konstanter_abstand_klein))
    
    gewinn_label_klein.grid(row = 0, column = 3, padx = str(konstanter_abstand_klein))
    gewinn_label1_klein.grid(row = 1, column = 3, padx = str(konstanter_abstand_klein))
    addition_label3_klein.grid(row = 2, column = 3, padx = str(konstanter_abstand_klein))
    gewinn_label2_klein.grid(row = 3, column = 3, padx = str(konstanter_abstand_klein))
    addition_label4_klein.grid(row = 4, column = 3, padx = str(konstanter_abstand_klein))
    gewinn_label3_klein.grid(row = 5, column = 3, padx = str(konstanter_abstand_klein))
    addition_label6_klein.grid(row = 6, column = 3, padx = str(konstanter_abstand_klein))
    gewinn_label5_klein.grid(row = 7, column = 3, padx = str(konstanter_abstand_klein))
    
    gewinn_label6_klein.grid(row = 7, column = 5, padx = str(konstanter_abstand_klein))
    addition_label7_klein.grid(row = 7, column = 2, padx = str(konstanter_abstand_klein))
    addition_label8_klein.grid(row = 7, column = 4, padx = str(konstanter_abstand_klein))
    okay_button_klein.grid(row = 8, column = 5, padx = str(konstanter_abstand_klein))
    
    rechnung.mainloop()

def auszahlung_button_click(): #Hier wird das eine Konto auf das andere Konto gebucht (nur Transparenzzwecke, ansonsten nichts)
    konto_label.config(text = str(int(konto_label.cget("text"))+(int(gewinn_label.cget("text")))))
    gewinn_label.config(text = "+0")
    if int(konto_label.cget("text")) < 10:
        konto_label.config(font = ("Helvetica",
                                   schriftgroeße_konto_setzen))
    elif int(konto_label.cget("text")) > 9 and int(konto_label.cget("text")) < 99:
        konto_label.config(font = ("Helvetica",
                                   round(schriftgroeße_konto_setzen*0.75)))
    elif int(konto_label.cget("text")) > 99:
        konto_label.config(font = ("Helvetica",
                                   round(schriftgroeße_konto_setzen/2)))
  
def setzen_button_allgemein(richtung, menge): #Eine Funktion, die von allen Buttons indirekt aufgerufen wird
    if menge != "":
        menge = int(menge)
        if richtung == "mehr":
            menge += 1
        else:
            menge -= 1
        if menge < 1:
            return (0, "0")
        else:
            return (0, str(menge))
    else:
        if richtung == "weniger":
            return (0, "0")
        else:
            return (0, "1")
        

def weniger_button_click1():
    menge = setzen_entry1.get()
    setzen_entry1.delete(0, "end")
    inhalt = setzen_button_allgemein("weniger", menge)
    setzen_entry1.insert(inhalt[0], inhalt[1])

def weniger_button_click2():
    menge = setzen_entry2.get()
    setzen_entry2.delete(0, "end")
    inhalt = setzen_button_allgemein("weniger", menge)
    setzen_entry2.insert(inhalt[0], inhalt[1])

def weniger_button_click3():
    menge = setzen_entry3.get()
    setzen_entry3.delete(0, "end")
    inhalt = setzen_button_allgemein("weniger", menge)
    setzen_entry3.insert(inhalt[0], inhalt[1])

def weniger_button_click4():
    menge = setzen_entry4.get()
    setzen_entry4.delete(0, "end")
    inhalt = setzen_button_allgemein("weniger", menge)
    setzen_entry4.insert(inhalt[0], inhalt[1])

def weniger_button_click5():
    menge = setzen_entry5.get()
    setzen_entry5.delete(0, "end")
    inhalt = setzen_button_allgemein("weniger", menge)
    setzen_entry5.insert(inhalt[0], inhalt[1])

def weniger_button_click6():
    menge = setzen_entry6.get()
    setzen_entry6.delete(0, "end")
    inhalt = setzen_button_allgemein("weniger", menge)
    setzen_entry6.insert(inhalt[0], inhalt[1])

def mehr_button_click1():
    menge = setzen_entry1.get()
    setzen_entry1.delete(0, "end")
    inhalt = setzen_button_allgemein("mehr", menge)
    setzen_entry1.insert(inhalt[0], inhalt[1])

def mehr_button_click2():
    menge = setzen_entry2.get()
    setzen_entry2.delete(0, "end")
    inhalt = setzen_button_allgemein("mehr", menge)
    setzen_entry2.insert(inhalt[0], inhalt[1])

def mehr_button_click3():
    menge = setzen_entry3.get()
    setzen_entry3.delete(0, "end")
    inhalt = setzen_button_allgemein("mehr", menge)
    setzen_entry3.insert(inhalt[0], inhalt[1])

def mehr_button_click4():
    menge = setzen_entry4.get()
    setzen_entry4.delete(0, "end")
    inhalt = setzen_button_allgemein("mehr", menge)
    setzen_entry4.insert(inhalt[0], inhalt[1])

def mehr_button_click5():
    menge = setzen_entry5.get()
    setzen_entry5.delete(0, "end")
    inhalt = setzen_button_allgemein("mehr", menge)
    setzen_entry5.insert(inhalt[0], inhalt[1])

def mehr_button_click6():
    menge = setzen_entry6.get()
    setzen_entry6.delete(0, "end")
    inhalt = setzen_button_allgemein("mehr", menge)
    setzen_entry6.insert(inhalt[0], inhalt[1])

#Hauptprogramm

#Fenster erstellen
fenster = Tk()
fenster.title("Chuck a luck!")
screen_hoehe = fenster.winfo_screenheight()
screen_breite = fenster.winfo_screenwidth()
fenster.geometry("%dx%d" % (screen_breite, screen_hoehe)) #Das Spiel soll beim Startimmer so groß wie der Screen sein
#fenster.geometry("1300x700") #Das Spiel hat beim Start eine festgelegte Größe und kann dann verändert werden
#fenster.attributes("-fullscreen", True) #Das Spiel wird immer Fullscreen gespielt
fenster.iconbitmap("pik_favicon.ico") #ändert das ico von einer Feder zu einem Pik
fenster.minsize(height = 500, width = 900) #Die Größe, bei der das Spiel noch gut zu spielen ist

#------Hier werden Größen ermittelt-------#

#Konstanten definieren
konstanter_abstand_klein = 5 #_klein steht immer für das Fenster der "Gewinnermittlung"
konstanter_abstand = 25 #zwischen zwei Widgets sollen immer 25px Platz sein
menge_wuerfel = 3 #Elemente nebeneinander im Rahmen "Würfel"
menge_zahlen = 6 #Elemente nebeneinander im Rahmen "Zahlen"
menge_konten = 2 #Elemente nebeneinander im Rahemn "Konten"
menge_zeilen_rahmen = 2 #Widgets untereinander in jedem Rahmen
menge_zeilen_fenster = 2 #Es gibt im Fenster zwei Rahmen untereinander
kopfzeile = 15 #Der Platz, an dem der Schließenbutton ist
anteil_konto_breite = (1/3) #14/37 #So viel der gesamten Fensterbreite wird die Breite des Kontorahmens
anteil_wuerfel_breite = (2/3) #23/37 #So viel der gesamten Fensterbreite wird die Breite des Wuerfelrahmens
anteil_label_hoehe = (2/3) #Wie bei menge_zeilen zu sehen, gibt es pro Rahmen 2 Zeilen. Hier wird bestimmt, welchen Anteil der Rahmenhöhe die obere Zeile einnimt

#Fenster
fenster_breite = fenster.winfo_width() #Um Widgets relativ zur Fenstergröße anordnen zu können
fenster_hoehe = fenster.winfo_height()

#Rahmengrößen ermitteln
setzen_hoehe = (fenster_hoehe - (konstanter_abstand *(menge_zeilen_fenster +1) + kopfzeile)) / 2
setzen_breite = fenster_breite - konstanter_abstand *2

konto_hoehe = (fenster_hoehe - (konstanter_abstand *(menge_zeilen_fenster +1) + kopfzeile)) / 2
konto_breite = (fenster_breite - konstanter_abstand *3) *anteil_konto_breite

wuerfel_hoehe = (fenster_hoehe - (konstanter_abstand *(menge_zeilen_fenster +1) + kopfzeile)) / 2
wuerfel_breite = (fenster_breite - konstanter_abstand *3) *anteil_wuerfel_breite

#Schriftgrößen ermitteln
schriftgroeße_wuerfel = int(fenster_breite//6) #Die Schriftgröße muss relativ zum Fenster sein
schriftgroeße_konto_setzen = int(fenster_breite//7)
schriftgroeße_gewinn = int(fenster_breite//15)
schriftgroeße_ariel = int(fenster_breite//75)
schriftgroeße_setzen = int(fenster_breite//45)


if fenster_breite - fenster_hoehe > 200: #Fall das Höhen-Seiten-Verhältnis zugusten der Höhe ausfällt, wird die Schriftgröße daran abgemessen
    schriftgroeße_wuerfel = int(fenster_hoehe//4) #Die Schriftgröße muss relativ zum Fenster sein
    schriftgroeße_konto_setzen = int(fenster_hoehe//5)
    schriftgroeße_gewinn = int(fenster_hoehe//10)
    schriftgroeße_ariel = int(fenster_hoehe//50)
    schriftgroeße_setzen = int(fenster_hoehe//30)

schriftgroeße_segoe_klein = 15 #_klein steht immer für das Fenster der "Gewinnermittlung"
schriftgroeße_ariel_klein = 15
schriftgroeße_wuerfel_klein = 50
schriftgroeße_zahlen_klein = 20

#Größen ermitteln
wuerfel_label_hoehe = (wuerfel_hoehe - konstanter_abstand *(menge_zeilen_rahmen + 1)) *anteil_label_hoehe
wuerfel_label_breite = (wuerfel_breite - konstanter_abstand *(menge_wuerfel + 1)) /menge_wuerfel #Es gibt insgesamt 3 Würfel, also 2 Ränder und zwei Zwischenräume à 25px und dann den Rest durch 3

konto_label_hoehe = (konto_hoehe - konstanter_abstand *(menge_zeilen_rahmen + 1)) *anteil_label_hoehe
konto_label_breite = (konto_breite - konstanter_abstand *(menge_konten + 1)) /menge_konten

setzen_label_hoehe = (setzen_hoehe - konstanter_abstand *(menge_zeilen_rahmen + 1)) *anteil_label_hoehe
setzen_label_breite = (setzen_breite - konstanter_abstand *(menge_zahlen + 1)) /menge_zahlen

richtung_button_hoehe = setzen_label_hoehe /3
richtung_button_breite = setzen_label_breite /3

setzen_entry_hoehe = richtung_button_hoehe
setzen_entry_breite = richtung_button_breite

button_hoehe = fenster_hoehe/20
button_breite = fenster_breite/10

#-------------Ende der Größenermittlung--------------#

#Button zum Spielschließen, nur notwendig bei fest definiertem Fullscreen. Im jetzigen Fall einfach nur eine Spaßfunktion
schließen_button = Button(master = fenster,
                          text = "Spiel schließen",
                          command = fenster.destroy)
schließen_button.place(relx=0.5, y = kopfzeile, anchor=CENTER)

#Rahmen fürs Setzen
setzen_rahmen = Frame(master = fenster,
                      highlightbackground = "black",
                      highlightthickness = 1)
setzen_rahmen.place(relx = konstanter_abstand / fenster_breite,
                    rely = (konstanter_abstand + kopfzeile) / fenster_hoehe,
                    relwidth = setzen_breite / fenster_breite,
                    relheight = setzen_hoehe / fenster_hoehe) #Größen relativ zur Bildschirmgröße



#Rahmen für Konto
konto_rahmen = Frame(master = fenster,
                     highlightbackground = "black",
                     highlightthickness = 1)
konto_rahmen.place(relx = konstanter_abstand / fenster_breite,
                   rely = (konstanter_abstand *2 + kopfzeile + setzen_hoehe) / fenster_hoehe,
                   relwidth = konto_breite / fenster_breite, 
                   relheight = konto_hoehe / fenster_hoehe) #Größen relativ zur Bildschirmgröße


#Rahmen für Würfel
wuerfel_rahmen = Frame(master = fenster,
                       highlightbackground = "black",
                       highlightthickness = 1)
wuerfel_rahmen.place(relx = (konstanter_abstand *2 + konto_breite) / fenster_breite,
                     rely = (konstanter_abstand *2 + kopfzeile + setzen_hoehe) / fenster_hoehe,
                     relwidth = wuerfel_breite / fenster_breite, 
                     relheight = wuerfel_hoehe / fenster_hoehe) #Größen relativ zur Bildschirmgröße


#Würfelliste in Unicode, also keine Bilder, sondern Schriftzeichen
wuerfel_liste = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]


#Label für Würfel
wuerfel_name_label = Label(master = wuerfel_rahmen,
                           text = "Würfel")
wuerfel_name_label.place(x = 0,
                         y = 0)

wuerfel_label1 = Label(master = wuerfel_rahmen,
                       text = "",
                       font = ("Helvetica",
                               schriftgroeße_wuerfel))
wuerfel_label1.place(relx = konstanter_abstand / wuerfel_breite,
                     rely = konstanter_abstand / wuerfel_hoehe,
                     relwidth = wuerfel_label_breite / wuerfel_breite,
                     relheight = wuerfel_label_hoehe / wuerfel_hoehe)

wuerfel_label2 = Label(master = wuerfel_rahmen,
                       text = "",
                       font = ("Helvetica",
                               schriftgroeße_wuerfel))
wuerfel_label2.place(relx = (konstanter_abstand *(menge_wuerfel - 1) + wuerfel_label_breite) / wuerfel_breite,
                     rely = konstanter_abstand / wuerfel_hoehe,
                     relwidth = wuerfel_label_breite / wuerfel_breite,
                     relheight = wuerfel_label_hoehe / wuerfel_hoehe)

wuerfel_label3 = Label(master = wuerfel_rahmen,
                       text = "",
                       font = ("Helvetica",
                               schriftgroeße_wuerfel))
wuerfel_label3.place(relx = (konstanter_abstand *(menge_wuerfel) + wuerfel_label_breite *(menge_wuerfel - 1)) / wuerfel_breite,
                     rely = konstanter_abstand / wuerfel_hoehe,
                     relwidth = wuerfel_label_breite / wuerfel_breite,
                     relheight = wuerfel_label_hoehe / wuerfel_hoehe)

#Button zum Würfelrollen
wuerfel_button = Button(master = wuerfel_rahmen,
                        text = "Würfeln",
                        font = ("Ariel",
                                schriftgroeße_ariel,
                                "bold"),
                        command = wuerfel_button_click)
wuerfel_button.place(relx = ((wuerfel_breite - button_breite) / 2) / wuerfel_breite,
                     rely = (wuerfel_hoehe - (wuerfel_hoehe/5)) / wuerfel_hoehe, #Die y-Position wird von unten berechnet
                     relwidth = button_breite / wuerfel_breite, 
                     relheight = button_hoehe / wuerfel_hoehe)



#Label für Konto
konto_name_label = Label(master = konto_rahmen,
                         text = "Konto")
konto_name_label.place(x = 0,
                       y = 0)

konto_label = Label(master = konto_rahmen, 
                    text = "3",
                    font = ("Helvetica",
                            schriftgroeße_konto_setzen))
konto_label.place(relx = konstanter_abstand / konto_breite,
                  rely = konstanter_abstand / konto_hoehe,
                  relwidth = konto_label_breite / konto_breite,
                  relheight = konto_label_hoehe / konto_hoehe)

gewinn_label = Label(master = konto_rahmen,
                     text = "+0",
                     anchor = "nw", 
                     font = ("Helvetica",
                            schriftgroeße_gewinn))
gewinn_label.place(relx = (konstanter_abstand *(menge_konten) + konto_label_breite) / konto_breite,
                   rely = konstanter_abstand / konto_hoehe,
                   relwidth = konto_label_breite / konto_breite,
                   relheight = konto_label_hoehe / konto_hoehe)

#Button zum Auszahlen
auszahlen_button = Button(master = konto_rahmen,
                          text = "Auszahlen",
                          font = ("Ariel",
                                  schriftgroeße_ariel,
                                  "bold"),
                          command = auszahlung_button_click)
auszahlen_button.place(relx = ((konto_breite - button_breite) /2) / konto_breite, 
                       rely = (konto_hoehe - (konto_hoehe/5)) / konto_hoehe, #Die y-Position wird von unten berechnet
                       relwidth = button_breite / konto_breite,
                       relheight = button_hoehe / konto_hoehe)

#Label fürs Setzen
setzen_name_label = Label(master = setzen_rahmen,
                          text = "Setzen")
setzen_name_label.place(x = 0,
                        y = 0)

setzen_label1 = Label(master = setzen_rahmen,
                      text = "1",
                      font = ("Helvetica",
                              schriftgroeße_konto_setzen))
setzen_label1.place(relx = konstanter_abstand / setzen_breite,
                    rely = konstanter_abstand / setzen_hoehe,
                    relwidth = setzen_label_breite / setzen_breite,
                    relheight = setzen_label_hoehe / setzen_hoehe)

setzen_label2 = Label(master = setzen_rahmen,
                      text = "2",
                      font = ("Helvetica",
                              schriftgroeße_konto_setzen))
setzen_label2.place(relx = (konstanter_abstand *(menge_zahlen - 4) + setzen_label_breite) / setzen_breite,
                    rely = konstanter_abstand / setzen_hoehe,
                    relwidth = setzen_label_breite / setzen_breite,
                    relheight = setzen_label_hoehe / setzen_hoehe)

setzen_label3 = Label(master = setzen_rahmen,
                      text = "3",
                      font = ("Helvetica",
                              schriftgroeße_konto_setzen))
setzen_label3.place(relx = (konstanter_abstand *(menge_zahlen - 3) + setzen_label_breite *(menge_zahlen - 4)) / setzen_breite,
                    rely = konstanter_abstand / setzen_hoehe,
                    relwidth = setzen_label_breite / setzen_breite,
                    relheight = setzen_label_hoehe / setzen_hoehe)

setzen_label4 = Label(master = setzen_rahmen,
                      text = "4",
                      font = ("Helvetica",
                              schriftgroeße_konto_setzen))
setzen_label4.place(relx = (konstanter_abstand *(menge_zahlen - 2) + setzen_label_breite *(menge_zahlen - 3)) / setzen_breite,
                    rely = konstanter_abstand / setzen_hoehe,
                    relwidth = setzen_label_breite / setzen_breite,
                    relheight = setzen_label_hoehe / setzen_hoehe)

setzen_label5 = Label(master = setzen_rahmen,
                      text = "5",
                      font = ("Helvetica",
                              schriftgroeße_konto_setzen))
setzen_label5.place(relx = (konstanter_abstand *(menge_zahlen - 1) + setzen_label_breite *(menge_zahlen - 2)) / setzen_breite,
                    rely = konstanter_abstand / setzen_hoehe,
                    relwidth = setzen_label_breite / setzen_breite,
                    relheight = setzen_label_hoehe / setzen_hoehe)

setzen_label6 = Label(master = setzen_rahmen,
                      text = "6",
                      font = ("Helvetica",
                              schriftgroeße_konto_setzen))
setzen_label6.place(relx = (konstanter_abstand *menge_zahlen + setzen_label_breite *(menge_zahlen - 1)) / setzen_breite,
                    rely = konstanter_abstand / setzen_hoehe,
                    relwidth = setzen_label_breite / setzen_breite,
                    relheight = setzen_label_hoehe / setzen_hoehe)

#Entry fürs Setzen

setzen_entry1 = Entry(master = setzen_rahmen,
                      font = ("Ariel",
                              schriftgroeße_setzen),
                      justify = "center",
                      bg = "white")

setzen_entry2 = Entry(master = setzen_rahmen,
                      font = ("Ariel",
                              schriftgroeße_setzen),
                      justify = "center",
                      bg = "white")

setzen_entry3 = Entry(master = setzen_rahmen,
                      font = ("Ariel",
                              schriftgroeße_setzen),
                      justify = "center",
                      bg = "white")

setzen_entry4 = Entry(master = setzen_rahmen,
                      font = ("Ariel",
                              schriftgroeße_setzen),
                      justify = "center",
                      bg = "white")

setzen_entry5 = Entry(master = setzen_rahmen,
                      font = ("Ariel",
                              schriftgroeße_setzen),
                      justify = "center",
                      bg = "white")

setzen_entry6 = Entry(master = setzen_rahmen,
                      font = ("Ariel",
                              schriftgroeße_setzen),
                      justify = "center",
                      bg = "white")

setzen_entry1.place(relx = (konstanter_abstand + richtung_button_breite) / setzen_breite,
                    rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                    relwidth = setzen_entry_breite / setzen_breite,
                    relheight = setzen_entry_hoehe / setzen_hoehe)

setzen_entry2.place(relx = (konstanter_abstand *(menge_zahlen - 4) + setzen_label_breite + richtung_button_breite) / setzen_breite,
                    rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                    relwidth = setzen_entry_breite / setzen_breite,
                    relheight = setzen_entry_hoehe / setzen_hoehe)

setzen_entry3.place(relx = (konstanter_abstand *(menge_zahlen - 3) + setzen_label_breite *(menge_zahlen - 4) + richtung_button_breite) / setzen_breite,
                    rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                    relwidth = setzen_entry_breite / setzen_breite,
                    relheight = setzen_entry_hoehe / setzen_hoehe)

setzen_entry4.place(relx = (konstanter_abstand *(menge_zahlen - 2) + setzen_label_breite *(menge_zahlen - 3) + richtung_button_breite) / setzen_breite,
                    rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                    relwidth = setzen_entry_breite / setzen_breite,
                    relheight = setzen_entry_hoehe / setzen_hoehe)

setzen_entry5.place(relx = (konstanter_abstand *(menge_zahlen - 1) + setzen_label_breite *(menge_zahlen - 2) + richtung_button_breite) / setzen_breite,
                    rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                    relwidth = setzen_entry_breite / setzen_breite,
                    relheight = setzen_entry_hoehe / setzen_hoehe)

setzen_entry6.place(relx = (konstanter_abstand *menge_zahlen + setzen_label_breite *(menge_zahlen - 1) + richtung_button_breite) / setzen_breite,
                    rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                    relwidth = setzen_entry_breite / setzen_breite,
                    relheight = setzen_entry_hoehe / setzen_hoehe)

#Button fürs Setzen
mehr_button1 = Button(master = setzen_rahmen,
                      text = ">",
                      font = ("Ariel",
                              schriftgroeße_ariel,
                              "bold"),
                      command = mehr_button_click1)

mehr_button2 = Button(master = setzen_rahmen,
                      text = ">",
                      font = ("Ariel",
                              schriftgroeße_ariel,
                              "bold"),
                      command = mehr_button_click2)

mehr_button3 = Button(master = setzen_rahmen,
                      text = ">",
                      font = ("Ariel",
                              schriftgroeße_ariel, 
                              "bold"),
                      command = mehr_button_click3)

mehr_button4 = Button(master = setzen_rahmen,
                      text = ">",
                      font = ("Ariel",
                              schriftgroeße_ariel,
                              "bold"),
                      command = mehr_button_click4)

mehr_button5 = Button(master = setzen_rahmen,
                      text = ">",
                      font = ("Ariel",
                              schriftgroeße_ariel,
                              "bold"),
                      command = mehr_button_click5)

mehr_button6 = Button(master = setzen_rahmen,
                      text = ">",
                      font = ("Ariel",
                              schriftgroeße_ariel,
                              "bold"),
                      command = mehr_button_click6)

weniger_button1 = Button(master = setzen_rahmen,
                         text = "<",
                         font = ("Ariel",
                                 schriftgroeße_ariel,
                                 "bold"),
                         command = weniger_button_click1)

weniger_button2 = Button(master = setzen_rahmen,
                         text = "<",
                         font = ("Ariel",
                                 schriftgroeße_ariel,
                                 "bold"),
                         command = weniger_button_click2)

weniger_button3 = Button(master = setzen_rahmen,
                         text = "<",
                         font = ("Ariel",
                                 schriftgroeße_ariel,
                                 "bold"),
                         command = weniger_button_click3)

weniger_button4 = Button(master = setzen_rahmen,
                         text = "<",
                         font = ("Ariel",
                                 schriftgroeße_ariel,
                                 "bold"),
                         command = weniger_button_click4)

weniger_button5 = Button(master = setzen_rahmen,
                         text = "<",
                         font = ("Ariel",
                                 schriftgroeße_ariel,
                                 "bold"),
                         command = weniger_button_click5)

weniger_button6 = Button(master = setzen_rahmen,
                         text = "<",
                         font = ("Ariel",
                                 schriftgroeße_ariel,
                                 "bold"),
                         command = weniger_button_click6)

mehr_button1.place(relx = (konstanter_abstand + richtung_button_breite + setzen_entry_breite) / setzen_breite,
                   rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                   relwidth = richtung_button_breite / setzen_breite,
                   relheight = richtung_button_hoehe / setzen_hoehe)

mehr_button2.place(relx = (konstanter_abstand *(menge_zahlen - 4) + setzen_label_breite + richtung_button_breite + setzen_entry_breite) / setzen_breite,
                   rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                   relwidth = richtung_button_breite / setzen_breite,
                   relheight = richtung_button_hoehe / setzen_hoehe)

mehr_button3.place(relx = (konstanter_abstand *(menge_zahlen - 3) + setzen_label_breite *(menge_zahlen - 4) + richtung_button_breite + setzen_entry_breite) / setzen_breite,
                   rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                   relwidth = richtung_button_breite / setzen_breite,
                   relheight = richtung_button_hoehe / setzen_hoehe)

mehr_button4.place(relx = (konstanter_abstand *(menge_zahlen - 2) + setzen_label_breite *(menge_zahlen - 3) + richtung_button_breite + setzen_entry_breite) / setzen_breite,
                   rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                   relwidth = richtung_button_breite / setzen_breite,
                   relheight = richtung_button_hoehe / setzen_hoehe)

mehr_button5.place(relx = (konstanter_abstand *(menge_zahlen - 1) + setzen_label_breite *(menge_zahlen - 2) + richtung_button_breite + setzen_entry_breite) / setzen_breite,
                   rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                   relwidth = richtung_button_breite / setzen_breite,
                   relheight = richtung_button_hoehe / setzen_hoehe)

mehr_button6.place(relx = (konstanter_abstand *menge_zahlen + setzen_label_breite *(menge_zahlen - 1) + richtung_button_breite + setzen_entry_breite) / setzen_breite,
                   rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                   relwidth = richtung_button_breite / setzen_breite,
                   relheight = richtung_button_hoehe / setzen_hoehe)

weniger_button1.place(relx = konstanter_abstand / setzen_breite,
                      rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                      relwidth = richtung_button_breite / setzen_breite,
                      relheight = richtung_button_hoehe / setzen_hoehe)

weniger_button2.place(relx = (konstanter_abstand *(menge_zahlen - 4) + setzen_label_breite) / setzen_breite,
                      rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                      relwidth = richtung_button_breite / setzen_breite,
                      relheight = richtung_button_hoehe / setzen_hoehe)

weniger_button3.place(relx = (konstanter_abstand *(menge_zahlen - 3) + setzen_label_breite *(menge_zahlen - 4)) / setzen_breite,
                      rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                      relwidth = richtung_button_breite / setzen_breite,
                      relheight = richtung_button_hoehe / setzen_hoehe)

weniger_button4.place(relx = (konstanter_abstand *(menge_zahlen - 2) + setzen_label_breite *(menge_zahlen - 3)) / setzen_breite,
                      rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                      relwidth = richtung_button_breite / setzen_breite,
                      relheight = richtung_button_hoehe / setzen_hoehe)

weniger_button5.place(relx = (konstanter_abstand *(menge_zahlen - 1) + setzen_label_breite *(menge_zahlen - 2)) / setzen_breite,
                      rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                      relwidth = richtung_button_breite / setzen_breite,
                      relheight = richtung_button_hoehe / setzen_hoehe)

weniger_button6.place(relx = (konstanter_abstand *menge_zahlen + setzen_label_breite *(menge_zahlen - 1)) / setzen_breite,
                      rely = (setzen_hoehe - (setzen_hoehe /4)) / setzen_hoehe,
                      relwidth = richtung_button_breite / setzen_breite,
                      relheight = richtung_button_hoehe / setzen_hoehe)

startbetrag() #Bei Spielbeginn

fenster.bind("<Configure>", resize) #Funktion, die an das Event "Fenstergröße verändert sich" gebunden ist
fenster.mainloop()



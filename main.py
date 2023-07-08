# Import the required libraries
from tkinter import *
from typing import List, Any


class ObjetSac:
    def __init__(self,noms, poids, valeur):
        self.noms = noms
        self.poids = poids
        self.valeur = valeur
        self.rapport = valeur / poids
        # Fonction pour la comparaison entre deux ObjetSac

    # On compare le rapport calculé pour les trier
    def __lt__(self, other):
        return self.rapport < other.rapport



def getMax( tableauTrie,capacite):


    tableauTrie.sort(reverse=True)
    z=0
    compteurValeur = 0
    chaineRes=""
    for objet in tableauTrie:
        poidsCourant = int(objet.poids)
        valeurCourante = float(objet.valeur)
        if capacite - poidsCourant >= 0:
            # on ajoute l'objet dans le sac
            # On soustrait la capacité

            print(objet.noms,objet.poids,objet.valeur)
            chaineRes=chaineRes+"|"+objet.noms
            z=z+1
            capacite -= poidsCourant
            compteurValeur += valeurCourante
    chaineRes = "La liste Des objects :"+chaineRes + "|"
    print(chaineRes)
    res.config(text=chaineRes)


            # On ajoute la valeur dans le sac

    return compteurValeur

############################################

################################################################
# Create an instance of tkinter frame or window
win = Tk()
#Titre de la fenetre
win.title("Sac à Dos")
win.geometry("1960x1080")
#window.iconbitmap("SacàDos.ico")
win.config(background='#FFECEF')
label_title = Label(win, text="Problème Du Sac à Dos " , font=("Pacifico",40) , bg='#FFECEF',fg='#372948' )
label_title.pack()
width = 400
height = 400

image = PhotoImage(file='sac-de-courses.png').zoom(10).subsample(16)
canvas = Canvas(win,width=width, height=height,bg='#FFECEF',bd=0,highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.place(x=600,y=300)

# Create an Entry widget
############
Cap = Label(win,text="Capacité",bg='#FFECEF',font=('Helvetica',20,'bold'),fg='#251B37')
Cap.place(x=780,y=180)
e = Entry(win,width=18,bd=3,relief=GROOVE,font=('Helvetica',20),bg="#FFCACA",fg="#372948")
e.place(x=700,y=260)
##########"
Demande = Label(win,text="Entrer les objets ",font=("Helvetica",20,'bold',) , bg='#FFECEF',fg='#251B37')
Demande.place(x=40,y=180)
Nom = Label(win,text="Le nom de l'objet",bg='#FFECEF',font=('Helvetica',14,'bold'),fg='#251B37')
Nom.place(x=160,y=230)
Poids = Label(win,text="Le poids de l'objet",bg='#FFECEF',font=('Helvetica',14,'bold'),fg='#251B37')
Poids.place(x=160,y=330)
Valeur = Label(win,text="La valeur de l'objet",bg='#FFECEF',font=('Helvetica',14,'bold'),fg='#251B37')
Valeur.place(x=160,y=430)
a = Entry(win,width=30,bd=3,relief=GROOVE,font=('Helvetica',20),bg="#FFCACA",fg="#372948")
a.place(x=50,y=280)
b = Entry(win,width=30,bd=3,relief=GROOVE,font=('Helvetica',20),bg="#FFCACA",fg="#372948")
b.place(x=50,y=380)
c = Entry(win,width=30,bd=3,relief=GROOVE,font=('Helvetica',20),bg="#FFCACA",fg="#372948")
c.place(x=50,y=480)
Envoyer = Button(win,text="Rajouter",bg="#251B37",fg="white",relief=FLAT,font=('Helvetica',18) ,width=10)
Envoyer.place(x=50,y=580)
Terminer = Button(win,text="Terminer",bg="#251B37",fg="white",relief=FLAT,font=('Helvetica',18) ,width=10)
Terminer.place(x=360,y=580)
capacite = 16
tableauTrie= []

def fin():


    capc = int(e.get())
    valeurMax = getMax(tableauTrie, capc)
    labelvaleur.config(text="La valeur max ="+str(valeurMax))

    print("valeur max", valeurMax)


def ajout():

     nom = str(a.get())
     valeur = int(c.get())
     poid = int(b.get())
     tableauTrie.append(ObjetSac(nom, poid, valeur))
     a.delete(0, END)
     b.delete(0, END)
     c.delete(0, END)
     label.config(text=str(len(tableauTrie))+" objet(s) entré(s) ")



Envoyer = Button(win,text="Ajouter",bg="#251B37",fg="white",relief=FLAT,font=('Helvetica',18) ,width=10,command=ajout)
Envoyer.place(x=50,y=580)
Terminer = Button(win,text="Résultat",bg="#251B37",fg="white",relief=FLAT,font=('Helvetica',18) ,width=10, command=fin)
Terminer.place(x=360,y=580)
################################################

label = Label(win, text=" 0 objet entré  ", font=('Helvetica',18,'bold') , bg='#FFECEF',fg="#372948")
label.place(x=320,y=179)
res = Label(win, text=" ", font=('Helvetica',18,'bold') , bg='#FFECEF',fg="#372948")
res.place(x=980,y=600)

labelvaleur=Label(win, text="",font=('Helvetica',18,'bold') , bg='#FFECEF',fg="#372948")
labelvaleur.place(x=980,y=650)

win.mainloop()
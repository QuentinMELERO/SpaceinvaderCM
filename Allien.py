## Importation des bibliothèques nécessaires

from tkinter import Tk, Label, Button, PhotoImage, Menu, Entry, StringVar, Canvas
import math

## Fonction de déplacement pour l'allien

def deplacement():
    """ déplacement de l'allien """
    global X,DX,RAYON,LARGEUR,HAUTEUR
    # Rebond à droite
    if X + RAYON + DX > LARGEUR:
        X = 2*(LARGEUR-RAYON)-X
        DX = -DX
    # Rebond à gauche
    if X - RAYON + DX < 0:
        X = 2*RAYON-X
        DX = -DX

    X = X + DX
    CanvaJeu.coords(allien,X-RAYON, Y-RAYON, X+RAYON, Y+RAYON)
    Mafenetre.after(20,deplacement)

## Fonction de déplacement pour le vaisseau

def Clavier(event):
    """ Gestion de l'évènement Appui sur une touche du clavier"""
    touche = event.keysym
    global PosX,PosY
    # déplacement vers la droite via la flèche de droite
    if touche == 'Right' and PosX < LARGEUR-20 :
        PosX += 30
    # déplacement vers la gauche vie la flèche de gauche
    if touche == 'Left' and PosX > 20:
        PosX -= 30
    # On dessine le vaisseau à sa nouvelle position
    CanvaJeu.coords(vaisseau,PosX-15,PosY-15,PosX+15,PosY+15)
    



## Mise en place de l'interface graphique principale

Mafenetre = Tk()
Mafenetre.title('Space Invaders')
Mafenetre.geometry('1200x700')

# Zone principale du jeu
HAUTEUR = 600
LARGEUR = 1000
CanvaJeu = Canvas(Mafenetre, bg='black')

# Informations pour l'allien
X = 500
Y = 100
vitesse = 10
angle = 5
DX = vitesse*math.cos(angle)
RAYON = 20 # Rayon de l'allien
allien = CanvaJeu.create_oval(X-RAYON, Y-RAYON, X+RAYON, Y+RAYON, width=1, outline='black', fill='red')

# Informations du vaisseau
PosX = 500
PosY = 580

vaisseau = CanvaJeu.create_rectangle(PosX-15, PosY-15, PosX+15, PosY+15, width=1, outline='black', fill='red')
CanvaJeu.focus_set()
CanvaJeu.bind('<Key>',lambda event: Clavier(event))

CanvaJeu.place(x=0, y=100, width=LARGEUR, height=HAUTEUR)
deplacement()

# Création d'un widget Menu
menubar = Menu(Mafenetre)
menuoption = Menu(menubar,tearoff =0)
menuoption.add_command(label="Recommencer une partie", command = Mafenetre.destroy) # Boutton pour recommencer une partie
menuoption.add_command(label="A propos", command = Mafenetre.destroy)
menuoption.add_command(label="Quitter le jeu", command = Mafenetre.destroy) # Boutton pour quitter 
menubar.add_cascade(label="Option", menu = menuoption)

# Affichage du menu
Mafenetre.config(menu = menubar)

# Création d'un widget Button (boutton jouer)
buttonRecommencer = Button (Mafenetre, text="RECOMMENCER", fg ='white', bg='black',relief='groove', command = Mafenetre.destroy)
buttonRecommencer.place(x=1050, y=250, width=100, height=50)

# Création d'un widget Label (pout afficher le score)
Score = Label(Mafenetre, text='Score : Score du joueur', bg='white',fg='black', font=100)
Score.place(x=5, y=5, width=250, height=30)


# Création d'un widget Label (pout afficher le nombre de vie du joueur)
Nbvie = Label(Mafenetre, text='Vie : Nombre de vie du joueur ', bg='white',fg='black', font=100)
Nbvie.place(x=700, y=5, width=300, height=30)

# Fonction pour afficher le nombre de vies du joueur

#def NbVie(donnee):
    #NbVie = Label(donnee.Mafenetre, text='Il vous reste ' + str(donnee.Vie) +  ' vies', bg='white',fg='black', font=100)
    #Nbchance.place(x=700, y=5, width=300, height=30)

# Création d'un widget Button (boutton quitter)
buttonQuitt = Button (Mafenetre, text="QUITTER", fg ='white', bg='black',relief='groove', command = Mafenetre.destroy)
buttonQuitt.place(x=1050, y=450, width=100, height=50)

Mafenetre.mainloop()
## Importation des bibliothèques nécessaires

from tkinter import Tk, Label, Button, PhotoImage, Menu, Entry, StringVar, Canvas


## Fonction pour le vaisseau 

def Clavier(event):
    """ Gestion de l'évènement Appui sur une touche du clavier"""
    global PosX,PosY
    touche = event.keysym
    # déplacement vers la droite via la flèche de droite
    if touche == 'Right':
        PosX += 30
    # déplacement vers la gauche vie la flèche de gauche
    if touche == 'Left':
        PosX -= 30
    # On dessine le pion à sa nouvelle position
    CanvaJeu.coords(vaisseau,PosX-10, PosY-10, PosX+10, PosY+10)

## Mise en place de l'interface graphique principale

Mafenetre = Tk()
Mafenetre.title('Space Invaders')
Mafenetre.geometry('1200x700')

# Zone principale du jeu
CanvaJeu = Canvas(Mafenetre, bg='black')

# Position initiale du vaisseau
PosX = 500
PosY = 580

vaisseau = CanvaJeu.create_rectangle(PosX-10, PosY-10, PosX+10, PosY+10, width=1, outline='black', fill='red')
CanvaJeu.focus_set()
CanvaJeu.bind('<Key>',Clavier)
CanvaJeu.place(x=0, y=100, width=1000, height=600)


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

# Création d'un widget Button (boutton quitter)
buttonQuitt = Button (Mafenetre, text="QUITTER", fg ='white', bg='black',relief='groove', command = Mafenetre.destroy)
buttonQuitt.place(x=1050, y=450, width=100, height=50)



Mafenetre.mainloop()

 
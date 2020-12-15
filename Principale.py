## Importation des bibliothèques nécessaires

from tkinter import Tk, Label, Button, PhotoImage, Menu, Entry, StringVar, Canvas

## Mise en place de l'interface graphique principale

Mafenetre = Tk()
Mafenetre.title('Space Invaders')
Mafenetre.geometry('1200x700')

# Zone principale du jeu
HAUTEUR = 600
LARGEUR = 1000
CanvaJeu = Canvas(Mafenetre, bg='black')
CanvaJeu.place(x=0, y=100, width=LARGEUR, height=HAUTEUR)

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


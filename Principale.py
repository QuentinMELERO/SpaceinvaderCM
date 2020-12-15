# Importation des bibliothèques nécessaires

from tkinter import Tk, Label, Button, PhotoImage, Menu, Entry, StringVar, Canvas

Mafenetre = Tk()
Mafenetre.title('Space Invader')
Mafenetre.geometry('1200x700')

# Fond 
CanvaFond = Canvas(Mafenetre, bg='black')
CanvaFond.place(x=0, y=100, width=1000, height=600)

# Création d'un widget Menu
menubar = Menu(Mafenetre)
menuoption = Menu(menubar,tearoff =0)
menuoption.add_command(label="Recommencer une partie", command = Mafenetre.destroy) # Boutton pour recommencer une partie
menuoption.add_command(label="Quitter le jeu", command = Mafenetre.destroy) # Boutton pour quitter 
menubar.add_cascade(label="Option", menu = menuoption)

# Affichage du menu
Mafenetre.config(menu = menubar)

# Création d'un widget Button (boutton quitter)
buttonQuitt = Button (Mafenetre, text="QUITTER", fg ='white', bg='red',relief='groove', command = Mafenetre.destroy)
buttonQuitt.place(x=20, y=600, width=100, height=50)

# Création d'un widget Button (boutton quitter)
buttonQuitt = Button (Mafenetre, text="QUITTER", fg ='white', bg='black',relief='groove', command = Mafenetre.destroy)
buttonQuitt.place(x=1050, y=400, width=100, height=50)

Mafenetre.mainloop()


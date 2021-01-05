## Importation des bibliothèques nécessaires

from tkinter import Tk, Label, Button, PhotoImage, Menu, Entry, StringVar, Canvas
import math

## Mise en place de l'interface graphique principale

Mafenetre = Tk()
Mafenetre.title('Space Invaders')
Mafenetre.geometry('1200x700')

# Zone principale du jeu
HAUTEUR = 600
LARGEUR = 1000
CanvaJeu = Canvas(Mafenetre, bg='black')

# Informations pour l'allien
Xa = 500
Ya = 100
n = 0
vitesse = 5
angle = 0
DX = vitesse*math.cos(angle)
RAYON_a = 20 # Rayon de l'allien
allien = CanvaJeu.create_oval(Xa-RAYON_a, Ya-RAYON_a, Xa+RAYON_a, Ya+RAYON_a, width=1, outline='black', fill='red')

# Informations pour le vaisseau
PosX = 500
PosY = 580
vaisseau = CanvaJeu.create_rectangle(PosX-15, PosY-15, PosX+15, PosY+15, width=1, outline='black', fill='red')
CanvaJeu.focus_set()
CanvaJeu.bind('<Key>',lambda event: Clavier(event))
CanvaJeu.place(x=0, y=100, width=LARGEUR, height=HAUTEUR)

# Informations pour le missile
Xm = 500
Ym = 580
vitesse_m = 10
angle = 0
DY = vitesse_m*math.cos(angle)
RAYON_m = 10 # Rayon du missile
missile = CanvaJeu.create_oval(Xm-RAYON_m, Ym-RAYON_m, Xm+RAYON_m, Ym+RAYON_m, width=1, outline='black', fill='white')

## Fonction de déplacement pour l'allien
def deplacement_allien():
    """ déplacement de l'allien """
    global Xa,DX,RAYON_a,LARGEUR,HAUTEUR,n,Ya
    # Rebond à droite
    if Xa + RAYON_a + DX > LARGEUR:
        Xa = 2*(LARGEUR-RAYON_a)-Xa
        DX = -DX
        n += 1
    # Rebond à gauche
    if Xa - RAYON_a + DX < 0:
        Xa = 2*RAYON_a-Xa
        DX = -DX
        n += 1
    
    if n == 2:
        Ya += RAYON_a
        n = 0

    Xa = Xa + DX
    CanvaJeu.coords(allien,Xa-RAYON_a, Ya-RAYON_a, Xa+RAYON_a, Ya+RAYON_a)
    Mafenetre.after(20,deplacement_allien)

deplacement_allien()

## Fonction de déplacement pour le missile
def deplacement_missile():
    """ déplacement du missile """
    global Ym,DY,RAYON_m,LARGEUR,HAUTEUR
    # Dispararition du missile si hors de le fenêtre de jeu
    if Ym - RAYON_m + DY < 0:
        CanvaJeu.delete(missile)
    Ym = Ym - DY
    
    CanvaJeu.coords(missile,Xm-RAYON_m, Ym-RAYON_m, Xm+RAYON_m, Ym+RAYON_m)
    Mafenetre.after(20,deplacement_missile)

## Fonction de déplacement pour le vaisseau

def Clavier(event):
    """ Gestion de l'évènement Appui sur une touche du clavier"""
    touche = event.keysym
    global PosX,PosY,Xm,Ym
    # déplacement vers la droite via la flèche de droite
    if touche == 'Right' and PosX < LARGEUR-20 :
        PosX += 30
        Xm += 30
    # déplacement vers la gauche vie la flèche de gauche
    if touche == 'Left' and PosX > 20:
        PosX -= 30
        Xm -= 30
    # lancement d'un missile via l'espace
    if touche == 'space' :
        deplacement_missile()
    # On dessine le vaisseau à sa nouvelle position
    CanvaJeu.coords(vaisseau,PosX-15,PosY-15,PosX+15,PosY+15)
    CanvaJeu.coords(missile,Xm-RAYON_m, Ym-RAYON_m, Xm+RAYON_m, Ym+RAYON_m)

## Fonction qui fait disparaitre l'allien et le missile lors d'une collison
    
def disparition():
    """ disparition de l'allien et du missile lors d'une colllision """
    if Ym >= Ya + RAYON_a and Ym <= Ya - RAYON_a and Xm >= Xa - RAYON_a and Xm <= Xa + RAYON_a : 
        CanvaJeu.delete(missile)
        CanvaJeu.delete(allien)

disparition()
    

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
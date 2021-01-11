## Importation des bibliothèques nécessaires
from tkinter import Tk, Label, Button, PhotoImage, Menu, Entry, StringVar, Canvas
import math
from Class import jeu_Spaceinvaders, info_allien, class_missile, info_vaisseau

## Mise en place de l'interface graphique principale
Mafenetre = Tk()
Mafenetre.title('Space Invaders')
Mafenetre.geometry('1200x700')
donnee_jeu = jeu_Spaceinvaders(Mafenetre)
donnee_allien = info_allien(Mafenetre)
donnee_vaisseau = info_vaisseau(Mafenetre)

# Zone principale du jeu
HAUTEUR = 600
LARGEUR = 1000
CanvaJeu = Canvas(Mafenetre, bg='black')

# Création de l'allien
allien = CanvaJeu.create_oval(donnee_allien.Xa-donnee_allien.RAYON_a, donnee_allien.Ya-donnee_allien.RAYON_a, donnee_allien.Xa+donnee_allien.RAYON_a, donnee_allien.Ya+donnee_allien.RAYON_a, width=1, outline='black', fill='red')

# Création du vaisseau
vaisseau = CanvaJeu.create_rectangle(donnee_vaisseau.Xv-15, donnee_vaisseau.Yv-15, donnee_vaisseau.Xv+15, donnee_vaisseau.Yv+15, width=1, outline='black', fill='red')
CanvaJeu.focus_set()
CanvaJeu.bind('<Key>',lambda event: Clavier(event))
CanvaJeu.place(x=0, y=100, width=LARGEUR, height=HAUTEUR)

# Informations pour le missile
#missile = CanvaJeu.create_oval(missile.Xm-missile.RAYON_m, missile.Ym-missile.RAYON_m, missile.Xm+missile.RAYON_m, missile.Ym+missile.RAYON_m, width=1, outline='black', fill='white')

### Fonctions permettant de faire fonctionner la fonction principale ###

## Fonction de déplacement pour l'allien
def deplacement_allien(donnee_allien):
    """ Fonction qui gère le déplacement de l'allien """
    # Rebond à droite
    if donnee_allien.Xa + donnee_allien.RAYON_a + donnee_allien.DX_a > LARGEUR:
        donnee_allien.DX_a = -donnee_allien.DX_a
        donnee_allien.n += 1
    # Rebond à gauche
    if donnee_allien.Xa - donnee_allien.RAYON_a + donnee_allien.DX_a < 0:
        donnee_allien.Xa = 2*donnee_allien.RAYON_a-donnee_allien.Xa
        donnee_allien.DX_a = -donnee_allien.DX_a
        donnee_allien.n += 1
    if donnee_allien.n == 2:
        donnee_allien.Ya += donnee_allien.RAYON_a
        donnee_allien.n = 0
    donnee_allien.Xa = donnee_allien.Xa + donnee_allien.DX_a
    CanvaJeu.coords(allien,donnee_allien.Xa-donnee_allien.RAYON_a, donnee_allien.Ya-donnee_allien.RAYON_a, donnee_allien.Xa+donnee_allien.RAYON_a, donnee_allien.Ya+donnee_allien.RAYON_a)
    Mafenetre.after(20,lambda x=donnee_allien : deplacement_allien(x))

Mafenetre.after(0,lambda x=donnee_allien : deplacement_allien(x))

## Fonction qui fait disparaitre l'allien et le missile lors d'une collison
def disparition(donnee_allien,missile_balle,missile):
    """ Fonction qui s'occupe de la disparition de l'allien et du missile lors d'une colllision """
    if  missile.Ym >= donnee_allien.Ya - donnee_allien.RAYON_a and missile.Ym <= donnee_allien.Ya + donnee_allien.RAYON_a and missile.Xm >= donnee_allien.Xa - donnee_allien.RAYON_a and missile.Xm <= donnee_allien.Xa + donnee_allien.RAYON_a  : 
        CanvaJeu.delete(missile_balle)
        CanvaJeu.delete(allien)
        return True 
    return False

## Fonction de déplacement pour le missile
def creation_missile():
    """ déplacement du missile """
    missile = class_missile(Mafenetre,donnee_vaisseau.Xv,donnee_vaisseau.Yv)
    missile_balle = CanvaJeu.create_oval(donnee_vaisseau.Xv-missile.RAYON_m, donnee_vaisseau.Yv-missile.RAYON_m, donnee_vaisseau.Xv+missile.RAYON_m, donnee_vaisseau.Yv+missile.RAYON_m, width=1, outline='black', fill='white')
    def deplacement_missile():
        # Dispararition du missile si hors de le fenêtre de jeu
        if missile.Ym - missile.RAYON_m + missile.DY_m < 0:
            CanvaJeu.delete(missile)
        else :
            missile.Ym = missile.Ym - missile.DY_m
            CanvaJeu.coords(missile_balle,missile.Xm-missile.RAYON_m, missile.Ym-missile.RAYON_m, missile.Xm+missile.RAYON_m, missile.Ym+missile.RAYON_m)
            if not disparition(donnee_allien,missile_balle,missile):
                Mafenetre.after(20,deplacement_missile)
    deplacement_missile()

## Fonction de déplacement liée aux touches du clavier
def Clavier(event):
    """ Gestion de l'évènement Appui sur une touche du clavier"""
    touche = event.keysym
    # déplacement vers la droite via la flèche de droite
    if touche == 'Right' and donnee_vaisseau.Xv < LARGEUR-20 :
        donnee_vaisseau.Xv += 30
    # déplacement vers la gauche vie la flèche de gauche
    if touche == 'Left' and donnee_vaisseau.Xv > 20:
        donnee_vaisseau.Xv -= 30
    # lancement d'un missile via l'espace
    if touche == 'space' :
        creation_missile()
    # On dessine le vaisseau à sa nouvelle position
    CanvaJeu.coords(vaisseau,donnee_vaisseau.Xv-15,donnee_vaisseau.Yv-15,donnee_vaisseau.Xv+15,donnee_vaisseau.Yv+15)
    
# Création d'un widget Menu
menubar = Menu(Mafenetre)
menuoption = Menu(menubar,tearoff =0)
menuoption.add_command(label="Recommencer une partie", command = Mafenetre.destroy) # Boutton pour recommencer une partie
menuoption.add_command(label="A propos", command = Mafenetre.destroy)
menuoption.add_command(label="Quitter le jeu", command = Mafenetre.destroy) # Boutton pour quitter 
menubar.add_cascade(label="Option", menu = menuoption)

# Affichage du menu
Mafenetre.config(menu = menubar)

# Création d'un widget Button (Boutton jouer)
buttonRecommencer = Button (Mafenetre, text="RECOMMENCER", fg ='white', bg='black',relief='groove', command = Mafenetre.destroy)
buttonRecommencer.place(x=1050, y=250, width=100, height=50)

# Création d'un widget Label (Pour afficher le score)
Score = Label(Mafenetre, text='Score : Score du joueur', bg='white',fg='black', font=100)
Score.place(x=5, y=5, width=250, height=30)

# Création d'un widget Label (Pour afficher le nombre de vie du joueur)
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
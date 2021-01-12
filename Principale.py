## Importation des bibliothèques nécessaires ##
from tkinter import Tk, Label, Button, PhotoImage, Menu, Entry, StringVar, Canvas
import math
from Class import jeu_Spaceinvaders, class_allien, class_missile, class_vaisseau, class_bloc

## Mise en place de l'interface graphique principale ##
Mafenetre = Tk()
Mafenetre.title('Space Invaders')
Mafenetre.geometry('1200x700')
donnee_jeu = jeu_Spaceinvaders(Mafenetre)
allien1 = class_allien(200)
allien2 = class_allien(420)
allien3 = class_allien(640)
vaisseau = class_vaisseau()

# Zone principale du jeu
HAUTEUR = 600
LARGEUR = 1000
CanvaJeu = Canvas(Mafenetre, bg='black')

# Création des alliens
allien1_obj = CanvaJeu.create_oval(allien1.Xa-allien1.RAYON_a, allien1.Ya-allien1.RAYON_a, allien1.Xa+allien1.RAYON_a, allien1.Ya+allien1.RAYON_a, width=1, outline='black', fill='red')
allien2_obj = CanvaJeu.create_oval(allien2.Xa-allien2.RAYON_a, allien2.Ya-allien2.RAYON_a, allien2.Xa+allien2.RAYON_a, allien2.Ya+allien2.RAYON_a, width=1, outline='black', fill='red')
allien3_obj = CanvaJeu.create_oval(allien3.Xa-allien3.RAYON_a, allien3.Ya-allien3.RAYON_a, allien3.Xa+allien3.RAYON_a, allien3.Ya+allien3.RAYON_a, width=1, outline='black', fill='red')

# Création du vaisseau
vaisseau_obj = CanvaJeu.create_rectangle(vaisseau.Xv-15, vaisseau.Yv-15, vaisseau.Xv+15, vaisseau.Yv+15, width=1, outline='black', fill='red')
CanvaJeu.focus_set()
CanvaJeu.bind('<Key>',lambda event: Clavier(event))
CanvaJeu.place(x=0, y=100, width=LARGEUR, height=HAUTEUR)

### Fonctions permettant de faire fonctionner la fonction principale ###

## Fonction de déplacement pour l'allien
def deplacement_allien(allien1):
    """ Fonction qui gère le déplacement de l'allien """
    # Rebond à droite
    if allien3.Xa + allien3.RAYON_a + allien3.DX_a > LARGEUR:
        allien3.DX_a = -allien3.DX_a
        allien2.DX_a = -allien2.DX_a
        allien1.DX_a = -allien1.DX_a
        allien3.n += 1
    # Rebond à gauche
    if allien1.Xa - allien1.RAYON_a + allien1.DX_a < 0:
        allien1.DX_a = -allien1.DX_a
        allien3.DX_a = -allien3.DX_a
        allien2.DX_a = -allien2.DX_a
        allien3.n += 1
    # Descend d'un demi-rayon apres un aller-retour
    if allien3.n == 2:
        allien1.Ya += allien1.RAYON_a
        allien2.Ya += allien1.RAYON_a
        allien3.Ya += allien1.RAYON_a
        allien3.n = 0
    allien1.Xa = allien1.Xa + allien1.DX_a
    allien2.Xa = allien2.Xa + allien2.DX_a
    allien3.Xa = allien3.Xa + allien3.DX_a
    CanvaJeu.coords(allien1_obj,allien1.Xa-allien1.RAYON_a, allien1.Ya-allien1.RAYON_a, allien1.Xa+allien1.RAYON_a, allien1.Ya+allien1.RAYON_a)
    CanvaJeu.coords(allien2_obj,allien2.Xa-allien2.RAYON_a, allien2.Ya-allien2.RAYON_a, allien2.Xa+allien2.RAYON_a, allien2.Ya+allien2.RAYON_a)
    CanvaJeu.coords(allien3_obj,allien3.Xa-allien3.RAYON_a, allien3.Ya-allien3.RAYON_a, allien3.Xa+allien3.RAYON_a, allien3.Ya+allien3.RAYON_a)
    #CanvaJeu.coords(missile1,Xa1-RAYON_m, Ya-RAYON_m, Xa1+RAYON_m, Ya+RAYON_m)
    #CanvaJeu.coords(missile2,Xa2-RAYON_m, Ya-RAYON_m, Xa2+RAYON_m, Ya+RAYON_m)
    #CanvaJeu.coords(missile3,Xa3-RAYON_m, Ya-RAYON_m, Xa3+RAYON_m, Ya+RAYON_m)
    Mafenetre.after(20,lambda x=allien1 : deplacement_allien(x))
Mafenetre.after(0,lambda x=allien1 : deplacement_allien(x))

## Création des blocks
bloc1 = class_bloc(200,400)
bloc2 = class_bloc(500,400)
bloc3 = class_bloc(800,400)

# Bloc 1
CanvaJeu.create_rectangle(bloc1.Xb-75, bloc1.Yb-50, bloc1.Xb+75, bloc1.Yb+50, width=1, outline='black', fill='red')
# Bloc 2
CanvaJeu.create_rectangle(bloc2.Xb-75, bloc2.Yb-50, bloc2.Xb+75, bloc2.Yb+50, width=1, outline='black', fill='red')
# Bloc 3
CanvaJeu.create_rectangle(bloc3.Xb-75, bloc3.Yb-50, bloc3.Xb+75, bloc3.Yb+50, width=1, outline='black', fill='red')

## Fonction qui fait disparaitre l'allien et le missile lors d'une collison
def disparition(allien1,missile_balle,missile):
    """ Fonction qui s'occupe de la disparition de l'allien et du missile lors d'une colllision """
    if  missile.Ym >= allien1.Ya - allien1.RAYON_a and missile.Ym <= allien1.Ya + allien1.RAYON_a and missile.Xm >= allien1.Xa - allien1.RAYON_a and missile.Xm <= allien1.Xa + allien1.RAYON_a  : 
        CanvaJeu.delete(missile_balle)
        CanvaJeu.delete(allien1_obj)
    if  missile.Ym >= allien2.Ya - allien2.RAYON_a and missile.Ym <= allien2.Ya + allien2.RAYON_a and missile.Xm >= allien2.Xa - allien2.RAYON_a and missile.Xm <= allien2.Xa + allien2.RAYON_a  : 
        CanvaJeu.delete(missile_balle)
        CanvaJeu.delete(allien2_obj)
    if  missile.Ym >= allien3.Ya - allien3.RAYON_a and missile.Ym <= allien3.Ya + allien3.RAYON_a and missile.Xm >= allien3.Xa - allien3.RAYON_a and missile.Xm <= allien3.Xa + allien3.RAYON_a  : 
        CanvaJeu.delete(missile_balle)
        CanvaJeu.delete(allien3_obj)
    if missile.Ym >= bloc1.Yb-50 and missile.Ym <= bloc1.Yb+50 and missile.Xm >= bloc1.Xb-75 and missile.Xm <= bloc1.Xb+75 :
        CanvaJeu.delete(missile_balle)
    if missile.Ym >= bloc2.Yb-50 and missile.Ym <= bloc2.Yb+50 and missile.Xm >= bloc2.Xb-75 and missile.Xm <= bloc2.Xb+75 :
        CanvaJeu.delete(missile_balle)
    if missile.Ym >= bloc3.Yb-50 and missile.Ym <= bloc3.Yb+50 and missile.Xm >= bloc3.Xb-75 and missile.Xm <= bloc3.Xb+75 :
        CanvaJeu.delete(missile_balle)

## Fonction qui fait disparaitre le missile des alliens
def disparition_missille_allien(vaisseau,missile_balle_allien,missile_allien):
    """ Fonction qui s'occupe de la disparition du missile de l'allien et du vaisseau lors d'une collision """
    if  missile_allien.Ym >= vaisseau.Yv - 15 and missile_allien.Ym <= vaisseau.Yv + 15 and missile_allien.Xm >= vaisseau.Xv - 15 and missile_allien.Xm <= vaisseau.Xv + 15 : 
        CanvaJeu.delete(missile_balle_allien)
        # On perd une vie
        donnee_jeu.Vie = donnee_jeu.Vie - 1
    if missile_allien.Ym >= bloc1.Yb-50 and missile_allien.Ym <= bloc1.Yb+50 and missile_allien.Xm >= bloc1.Xb-75 and missile_allien.Xm <= bloc1.Xb+75 :
        CanvaJeu.delete(missile_balle_allien)
    if missile_allien.Ym >= bloc2.Yb-50 and missile_allien.Ym <= bloc2.Yb+50 and missile_allien.Xm >= bloc2.Xb-75 and missile_allien.Xm <= bloc2.Xb+75 :
        CanvaJeu.delete(missile_balle_allien)
    if missile_allien.Ym >= bloc3.Yb-50 and missile_allien.Ym <= bloc3.Yb+50 and missile_allien.Xm >= bloc3.Xb-75 and missile_allien.Xm <= bloc3.Xb+75 :
        CanvaJeu.delete(missile_balle_allien)
 

## Fonction de déplacement pour le missile
def creation_missile():
    """ déplacement du missile """
    missile = class_missile(vaisseau.Xv,vaisseau.Yv)
    missile_balle = CanvaJeu.create_oval(vaisseau.Xv-missile.RAYON_m, vaisseau.Yv-missile.RAYON_m, vaisseau.Xv+missile.RAYON_m, vaisseau.Yv+missile.RAYON_m, width=1, outline='black', fill='white')
    def deplacement_missile():
        # Dispararition du missile si hors de le fenêtre de jeu
        if missile.Ym - missile.RAYON_m + missile.DY_m < 0:
            CanvaJeu.delete(missile)
        else :
            missile.Ym = missile.Ym - missile.DY_m
            CanvaJeu.coords(missile_balle,missile.Xm-missile.RAYON_m, missile.Ym-missile.RAYON_m, missile.Xm+missile.RAYON_m, missile.Ym+missile.RAYON_m)
            if not disparition(allien1,missile_balle,missile):
                Mafenetre.after(20,deplacement_missile)
    deplacement_missile()

## Fonction de déplacement missiles alliens
def creation_missile_allien():
    missile_allien = class_missile(allien1.Xa,allien1.Ya)
    missile_balle_allien = CanvaJeu.create_oval(allien1.Xa-missile_allien.RAYON_m, allien1.Ya-missile_allien.RAYON_m, allien1.Xa+missile_allien.RAYON_m, allien1.Ya+missile_allien.RAYON_m, width=1, outline='black', fill='white')
    def deplacement_missile_allien():
        # Dispararition du missile si hors de le fenêtre de jeu
        if missile_allien.Ym + missile_allien.RAYON_m - missile_allien.DY_m > 600 :
            CanvaJeu.delete(missile_allien)
        else :
            missile_allien.Ym = missile_allien.Ym + missile_allien.DY_m
            CanvaJeu.coords(missile_balle_allien,missile_allien.Xm-missile_allien.RAYON_m, missile_allien.Ym-missile_allien.RAYON_m, missile_allien.Xm+missile_allien.RAYON_m, missile_allien.Ym+missile_allien.RAYON_m)
            if not disparition_missille_allien(vaisseau,missile_balle_allien,missile_allien):
                Mafenetre.after(20,deplacement_missile_allien)
    deplacement_missile_allien()
    Mafenetre.after(900,creation_missile_allien)
creation_missile_allien()

## Fonction de déplacement liée aux touches du clavier
def Clavier(event):
    """ Gestion de l'évènement Appui sur une touche du clavier"""
    touche = event.keysym
    # déplacement vers la droite via la flèche de droite
    if touche == 'Right' and vaisseau.Xv < LARGEUR-20 :
        vaisseau.Xv += 30
    # déplacement vers la gauche vie la flèche de gauche
    if touche == 'Left' and vaisseau.Xv > 20:
        vaisseau.Xv -= 30
    # lancement d'un missile via l'espace
    if touche == 'space' :
        creation_missile()
    # On dessine le vaisseau à sa nouvelle position
    CanvaJeu.coords(vaisseau_obj,vaisseau.Xv-15,vaisseau.Yv-15,vaisseau.Xv+15,vaisseau.Yv+15)


def fin_de_partie():
    """ Fonction qui met fin à la partie """
    if allien1.Ya + allien1.RAYON_a == vaisseau.Xv :
        CanvaJeu.delete(vaisseau_obj)
        CanvaJeu.delete(allien1_obj)
        fin_de_partie()

## Tout ce qui est lié à l'interface graphique ##
    
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
#Nbvie = Label(Mafenetre, text='Vie : Nombre de vie du joueur ', bg='white',fg='black', font=100)
#Nbvie.place(x=700, y=5, width=300, height=30)

# Fonction pour afficher le nombre de vies du joueur

def NbVie(donnee_jeu):
    NbVie = Label(donnee_jeu.Mafenetre, text='Vies restantes : ' + str(donnee_jeu.Vie), bg='white',fg='black', font=100)
    NbVie.place(x=700, y=5, width=300, height=30)
NbVie(donnee_jeu)

# Création d'un widget Button (boutton quitter)
buttonQuitt = Button (Mafenetre, text="QUITTER", fg ='white', bg='black',relief='groove', command = Mafenetre.destroy)
buttonQuitt.place(x=1050, y=450, width=100, height=50)

Mafenetre.mainloop()
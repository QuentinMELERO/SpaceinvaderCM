## Importation des bibliothèques nécessaires ##
from tkinter import Tk, Label, Button, PhotoImage, Menu, Entry, StringVar, Canvas
import math
from Class import jeu_Spaceinvaders, class_allien, class_missile, class_vaisseau, class_bloc

## Mise en place de l'interface graphique principale ##
Mafenetre = Tk()
Mafenetre.title('Space Invaders')
Mafenetre.geometry('1200x700')
donnee_jeu = jeu_Spaceinvaders(Mafenetre)
allien = class_allien(Mafenetre)
vaisseau = class_vaisseau(Mafenetre)

# Zone principale du jeu
HAUTEUR = 600
LARGEUR = 1000
CanvaJeu = Canvas(Mafenetre, bg='black')

# Création des alliens
allien1_obj = CanvaJeu.create_oval(allien.Xa1-allien.RAYON_a, allien.Ya-allien.RAYON_a, allien.Xa1+allien.RAYON_a, allien.Ya+allien.RAYON_a, width=1, outline='black', fill='red')
allien2_obj = CanvaJeu.create_oval(allien.Xa2-allien.RAYON_a, allien.Ya-allien.RAYON_a, allien.Xa2+allien.RAYON_a, allien.Ya+allien.RAYON_a, width=1, outline='black', fill='red')
allien3_obj = CanvaJeu.create_oval(allien.Xa3-allien.RAYON_a, allien.Ya-allien.RAYON_a, allien.Xa3+allien.RAYON_a, allien.Ya+allien.RAYON_a, width=1, outline='black', fill='red')

# Création du vaisseau
vaisseau_obj = CanvaJeu.create_rectangle(vaisseau.Xv-15, vaisseau.Yv-15, vaisseau.Xv+15, vaisseau.Yv+15, width=1, outline='black', fill='red')
CanvaJeu.focus_set()
CanvaJeu.bind('<Key>',lambda event: Clavier(event))
CanvaJeu.place(x=0, y=100, width=LARGEUR, height=HAUTEUR)

### Fonctions permettant de faire fonctionner la fonction principale ###

## Fonction de déplacement pour l'allien
def deplacement_allien(allien):
    """ Fonction qui gère le déplacement de l'allien """
    # Rebond à droite
    if allien.Xa3 + allien.RAYON_a + allien.DX_a > LARGEUR:
        allien.DX_a = -allien.DX_a
        allien.n += 1
    # Rebond à gauche
    if allien.Xa1 - allien.RAYON_a + allien.DX_a < 0:
        allien.DX_a = -allien.DX_a
        allien.n += 1
    # Descend d'un demi-rayon apres un aller-retour
    if allien.n == 2:
        allien.Ya += allien.RAYON_a
        allien.n = 0
    allien.Xa1 = allien.Xa1 + allien.DX_a
    allien.Xa2 = allien.Xa2 + allien.DX_a
    allien.Xa3 = allien.Xa3 + allien.DX_a
    CanvaJeu.coords(allien1_obj,allien.Xa1-allien.RAYON_a, allien.Ya-allien.RAYON_a, allien.Xa1+allien.RAYON_a, allien.Ya+allien.RAYON_a)
    CanvaJeu.coords(allien2_obj,allien.Xa2-allien.RAYON_a, allien.Ya-allien.RAYON_a, allien.Xa2+allien.RAYON_a, allien.Ya+allien.RAYON_a)
    CanvaJeu.coords(allien3_obj,allien.Xa3-allien.RAYON_a, allien.Ya-allien.RAYON_a, allien.Xa3+allien.RAYON_a, allien.Ya+allien.RAYON_a)
    #CanvaJeu.coords(missile1,Xa1-RAYON_m, Ya-RAYON_m, Xa1+RAYON_m, Ya+RAYON_m)
    #CanvaJeu.coords(missile2,Xa2-RAYON_m, Ya-RAYON_m, Xa2+RAYON_m, Ya+RAYON_m)
    #CanvaJeu.coords(missile3,Xa3-RAYON_m, Ya-RAYON_m, Xa3+RAYON_m, Ya+RAYON_m)
    #Mafenetre.after(20,deplacement_allien)
    CanvaJeu.coords(allien1_obj,allien.Xa1-allien.RAYON_a, allien.Ya-allien.RAYON_a, allien.Xa1+allien.RAYON_a, allien.Ya+allien.RAYON_a)
    CanvaJeu.coords(allien2_obj,allien.Xa2-allien.RAYON_a, allien.Ya-allien.RAYON_a, allien.Xa2+allien.RAYON_a, allien.Ya+allien.RAYON_a)
    CanvaJeu.coords(allien3_obj,allien.Xa3-allien.RAYON_a, allien.Ya-allien.RAYON_a, allien.Xa3+allien.RAYON_a, allien.Ya+allien.RAYON_a)
    Mafenetre.after(20,lambda x=allien : deplacement_allien(x))

Mafenetre.after(0,lambda x=allien : deplacement_allien(x))

## Création des blocks
Bloc = class_bloc(Mafenetre)
# Bloc 1
CanvaJeu.create_rectangle(Bloc.X1-75, Bloc.Y1-50, Bloc.X1+75, Bloc.Y1+50, width=1, outline='black', fill='red')
# Bloc 2
CanvaJeu.create_rectangle(Bloc.X2-75, Bloc.Y2-50, Bloc.X2+75, Bloc.Y2+50, width=1, outline='black', fill='red')
# Bloc 3
CanvaJeu.create_rectangle(Bloc.X3-75, Bloc.Y3-50, Bloc.X3+75, Bloc.Y3+50, width=1, outline='black', fill='red')


## Fonction qui fait disparaitre l'allien et le missile lors d'une collison
def disparition(allien,missile_balle,missile):
    """ Fonction qui s'occupe de la disparition de l'allien et du missile lors d'une colllision """
    if  missile.Ym >= allien.Ya - allien.RAYON_a and missile.Ym <= allien.Ya + allien.RAYON_a and missile.Xm >= allien.Xa1 - allien.RAYON_a and missile.Xm <= allien.Xa1 + allien.RAYON_a  : 
        CanvaJeu.delete(missile_balle)
        CanvaJeu.delete(allien1_obj)
    if  missile.Ym >= allien.Ya - allien.RAYON_a and missile.Ym <= allien.Ya + allien.RAYON_a and missile.Xm >= allien.Xa2 - allien.RAYON_a and missile.Xm <= allien.Xa2 + allien.RAYON_a  : 
        CanvaJeu.delete(missile_balle)
        CanvaJeu.delete(allien2_obj)
    if  missile.Ym >= allien.Ya - allien.RAYON_a and missile.Ym <= allien.Ya + allien.RAYON_a and missile.Xm >= allien.Xa3 - allien.RAYON_a and missile.Xm <= allien.Xa3 + allien.RAYON_a  : 
        CanvaJeu.delete(missile_balle)
        CanvaJeu.delete(allien3_obj)
    if missile.Ym >= Bloc.Y1-50 and missile.Ym <= Bloc.Y1+50 and missile.Xm >= Bloc.X1-75 and missile.Xm <= Bloc.X1+75 :
        CanvaJeu.delete(missile_balle)
    if missile.Ym >= Bloc.Y2-50 and missile.Ym <= Bloc.Y2+50 and missile.Xm >= Bloc.X2-75 and missile.Xm <= Bloc.X2+75 :
        CanvaJeu.delete(missile_balle)
    if missile.Ym >= Bloc.Y3-50 and missile.Ym <= Bloc.Y3+50 and missile.Xm >= Bloc.X3-75 and missile.Xm <= Bloc.X3+75 :
        CanvaJeu.delete(missile_balle)

## Fonction qui fait disparaitre le missile des alliens
def disparition_missille_allien(vaisseau,missile_balle_allien,missile_allien):
    """ Fonction qui s'occupe de la disparition du missile de l'allien et du vaisseau lors d'une collision """
    if  missile_allien.Ym >= vaisseau.Yv - 15 and missile_allien.Ym <= vaisseau.Yv + 15 and missile_allien.Xm >= vaisseau.Xv - 15 and missile_allien.Xm <= vaisseau.Xv + 15 : 
        CanvaJeu.delete(missile_balle_allien)
        # On perd une vie
    if missile_allien.Ym >= bloc1.Y-50 and missile_allien.Ym <= bloc1.Y+50 and missile_allien.Xm >= bloc1.X-75 and missile_allien.Xm <= bloc1.X+75 :
        CanvaJeu.delete(missile_balle_allien)
    if missile_allien.Ym >= bloc2.Y-50 and missile_allien.Ym <= bloc2.Y+50 and missile_allien.Xm >= bloc2.X-75 and missile_allien.Xm <= bloc2.X+75 :
        CanvaJeu.delete(missile_balle_allien)
    if missile_allien.Ym >= bloc3.Y-50 and missile_allien.Ym <= bloc3.Y+50 and missile_allien.Xm >= bloc3.X-75 and missile_allien.Xm <= bloc3.X+75 :
        CanvaJeu.delete(missile_balle_allien)
 
## Fonction de déplacement pour le missile
def creation_missile():
    """ déplacement du missile """
    missile = class_missile(Mafenetre,vaisseau.Xv,vaisseau.Yv)
    missile_balle = CanvaJeu.create_oval(vaisseau.Xv-missile.RAYON_m, vaisseau.Yv-missile.RAYON_m, vaisseau.Xv+missile.RAYON_m, vaisseau.Yv+missile.RAYON_m, width=1, outline='black', fill='white')
    def deplacement_missile():
        # Dispararition du missile si hors de le fenêtre de jeu
        if missile.Ym - missile.RAYON_m + missile.DY_m < 0:
            CanvaJeu.delete(missile)
        else :
            missile.Ym = missile.Ym - missile.DY_m
            CanvaJeu.coords(missile_balle,missile.Xm-missile.RAYON_m, missile.Ym-missile.RAYON_m, missile.Xm+missile.RAYON_m, missile.Ym+missile.RAYON_m)
            if not disparition(allien,missile_balle,missile):
                Mafenetre.after(20,deplacement_missile)
    deplacement_missile()

## Fonction de déplacement missiles alliens
def creation_missile_allien():
    missile_allien = class_missile(Mafenetre,allien.Xa1,allien.Ya)
    missile_balle_allien = CanvaJeu.create_oval(allien.Xa1-missile_allien.RAYON_m, allien.Ya-missile_allien.RAYON_m, allien.Xa1+missile_allien.RAYON_m, allien.Ya+missile_allien.RAYON_m, width=1, outline='black', fill='white')
    def deplacement_missile_allien():
        # Dispararition du missile si hors de le fenêtre de jeu
        if missile_allien.Ym + missile_allien.RAYON_m == vaisseau.Yv:
            CanvaJeu.delete(missile_allien)
        else :
            missile_allien.Ym = missile_allien.Ym + missile_allien.DY_m
            CanvaJeu.coords(missile_balle_allien,missile_allien.Xm-missile_allien.RAYON_m, missile_allien.Ym-missile_allien.RAYON_m, missile_allien.Xm+missile_allien.RAYON_m, missile_allien.Ym+missile_allien.RAYON_m)
            #if not disparition(allien,missile_balle,missile):
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
    if allien.Ya + allien.RAYON_a == vaisseau.Xv :
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
## Importation des bibliothèques nécessaires ##

from tkinter import Tk, Label, Button, PhotoImage, Menu, Entry, StringVar, Canvas, messagebox
from Class import jeu_Spaceinvaders, class_alien, class_missile, class_vaisseau, class_bloc

## Fonction qui fait marcher le jeu ##

def Jeu():

# Création de la fenêtre graphique
    Mafenetre = Tk()
    Mafenetre.title('Space Invaders Corsetti-Melero')
    Mafenetre.geometry('1200x700')
    donnee_jeu = jeu_Spaceinvaders(Mafenetre)
    alien1 = class_alien(200)
    alien2 = class_alien(420)
    alien3 = class_alien(640)
    Aliens = [alien1,alien2,alien3]
    vaisseau = class_vaisseau()
    Gagne = False
    Perdu = False

    # Zone principale du jeu
    HAUTEUR = 600
    LARGEUR = 1000
    CanvaJeu = Canvas(Mafenetre, bg='black')

    # Création des aliens
    alien1_obj = CanvaJeu.create_oval(alien1.Xa-alien1.RAYON_a, alien1.Ya-alien1.RAYON_a, alien1.Xa+alien1.RAYON_a, alien1.Ya+alien1.RAYON_a, width=1, outline='black', fill='red')
    alien2_obj = CanvaJeu.create_oval(alien2.Xa-alien2.RAYON_a, alien2.Ya-alien2.RAYON_a, alien2.Xa+alien2.RAYON_a, alien2.Ya+alien2.RAYON_a, width=1, outline='black', fill='red')
    alien3_obj = CanvaJeu.create_oval(alien3.Xa-alien3.RAYON_a, alien3.Ya-alien3.RAYON_a, alien3.Xa+alien3.RAYON_a, alien3.Ya+alien3.RAYON_a, width=1, outline='black', fill='red')
    Aliens_obj = [alien1_obj,alien2_obj,alien3_obj]

    # Création du vaisseau
    vaisseau_obj = CanvaJeu.create_rectangle(vaisseau.Xv-15, vaisseau.Yv-15, vaisseau.Xv+15, vaisseau.Yv+15, width=1, outline='black', fill='red')

    # Zone de jeu
    CanvaJeu.focus_set()
    CanvaJeu.bind('<Key>',lambda event: Clavier(event))
    CanvaJeu.place(x=0, y=100, width=LARGEUR, height=HAUTEUR)

    ### Toutes les fonctions permettant de faire fonctionner la fonction principale ###

    ## Fonction de déplacement pour l'alien
    def deplacement_alien(alien1):
        """ Fonction qui gère le déplacement des aliens """
        # Rebond à droite
        if alien3.Xa + alien3.RAYON_a + alien3.DX_a > LARGEUR:
            alien3.DX_a = -alien3.DX_a
            alien2.DX_a = -alien2.DX_a
            alien1.DX_a = -alien1.DX_a
            alien3.n += 1
        # Rebond à gauche
        if alien1.Xa - alien1.RAYON_a + alien1.DX_a < 0:
            alien1.DX_a = -alien1.DX_a
            alien3.DX_a = -alien3.DX_a
            alien2.DX_a = -alien2.DX_a
            alien3.n += 1
        # Descend d'un demi-rayon apres un aller-retour
        if alien3.n == 2:
            alien1.Ya += alien1.RAYON_a
            alien2.Ya += alien1.RAYON_a
            alien3.Ya += alien1.RAYON_a
            alien3.n = 0
        alien1.Xa = alien1.Xa + alien1.DX_a
        alien2.Xa = alien2.Xa + alien2.DX_a
        alien3.Xa = alien3.Xa + alien3.DX_a
        CanvaJeu.coords(alien1_obj,alien1.Xa-alien1.RAYON_a, alien1.Ya-alien1.RAYON_a, alien1.Xa+alien1.RAYON_a, alien1.Ya+alien1.RAYON_a)
        CanvaJeu.coords(alien2_obj,alien2.Xa-alien2.RAYON_a, alien2.Ya-alien2.RAYON_a, alien2.Xa+alien2.RAYON_a, alien2.Ya+alien2.RAYON_a)
        CanvaJeu.coords(alien3_obj,alien3.Xa-alien3.RAYON_a, alien3.Ya-alien3.RAYON_a, alien3.Xa+alien3.RAYON_a, alien3.Ya+alien3.RAYON_a)
        Mafenetre.after(20,lambda x=alien1 : deplacement_alien(x))
    Mafenetre.after(0,lambda x=alien1 : deplacement_alien(x))

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

    ## Fonction qui fait disparaitre l'alien et le missile lors d'une collison
    def disparition(alien1,missile_balle,missile):
        """ Fonction qui s'occupe de la disparition de l'alien et du missile lors d'une colllision """
        i = 0
        for alien in Aliens : 
            if  missile.Ym >= alien.Ya - alien.RAYON_a and missile.Ym <= alien.Ya + alien.RAYON_a and missile.Xm >= alien.Xa - alien.RAYON_a and missile.Xm <= alien.Xa + alien.RAYON_a: 
                CanvaJeu.delete(missile_balle)
                CanvaJeu.delete(Aliens_obj[i])
                donnee_jeu.Score += 50
                Score(donnee_jeu)
                alien.alive = False
                return True
            i += 1
        if missile.Ym >= bloc1.Yb-50 and missile.Ym <= bloc1.Yb+50 and missile.Xm >= bloc1.Xb-75 and missile.Xm <= bloc1.Xb+75 :
            CanvaJeu.delete(missile_balle)
            return True
        if missile.Ym >= bloc2.Yb-50 and missile.Ym <= bloc2.Yb+50 and missile.Xm >= bloc2.Xb-75 and missile.Xm <= bloc2.Xb+75 :
            CanvaJeu.delete(missile_balle)
            return True
        if missile.Ym >= bloc3.Yb-50 and missile.Ym <= bloc3.Yb+50 and missile.Xm >= bloc3.Xb-75 and missile.Xm <= bloc3.Xb+75 :
            CanvaJeu.delete(missile_balle)
            return True
        return False

    ## Fonction pour afficher le nombre de vies du joueur
    def NbVie(donnee_jeu):
        """ Affiche le nombre de vie du joueur """
        NbVie = Label(donnee_jeu.Mafenetre, text='Vies restantes : ' + str(donnee_jeu.Vie), bg='white',fg='black', font=100)
        NbVie.place(x=700, y=5, width=300, height=30)

    ## Fonction pour afficher le score du joueur
    def Score(donnee_jeu):
        """ Affiche le score du joueur """
        Score = Label(Mafenetre, text='Score : ' + str(donnee_jeu.Score), bg='white',fg='black', font=100)
        Score.place(x=5, y=5, width=250, height=30)
    

    ## Fonction qui fait disparaitre le missile des aliens
    def disparition_missille_alien(vaisseau,missile_balle_alien,missile_alien):
        """ Fonction qui s'occupe de la disparition du missile de l'alien et du vaisseau lors d'une collision """
        if  missile_alien.Ym >= vaisseau.Yv - 15 and missile_alien.Ym <= vaisseau.Yv + 15 and missile_alien.Xm >= vaisseau.Xv - 15 and missile_alien.Xm <= vaisseau.Xv + 15 : 
            CanvaJeu.delete(missile_balle_alien)
            # On perd une vie
            donnee_jeu.Vie = donnee_jeu.Vie - 1
            NbVie(donnee_jeu)
            return True
        if missile_alien.Ym >= bloc1.Yb-50 and missile_alien.Ym <= bloc1.Yb+50 and missile_alien.Xm >= bloc1.Xb-75 and missile_alien.Xm <= bloc1.Xb+75 :
            CanvaJeu.delete(missile_balle_alien)
            return True
        if missile_alien.Ym >= bloc2.Yb-50 and missile_alien.Ym <= bloc2.Yb+50 and missile_alien.Xm >= bloc2.Xb-75 and missile_alien.Xm <= bloc2.Xb+75 :
            CanvaJeu.delete(missile_balle_alien)
            return True
        if missile_alien.Ym >= bloc3.Yb-50 and missile_alien.Ym <= bloc3.Yb+50 and missile_alien.Xm >= bloc3.Xb-75 and missile_alien.Xm <= bloc3.Xb+75 :
            CanvaJeu.delete(missile_balle_alien)
            return True
        return False

    ## Fonction pour le à propos
    def apropos():
        """ Fonction pour la commande apropos"""
        messagebox.showinfo(title='A propos', message='Jeu classique du SpaceInvaders réalisé par Adrien Corsetti et Quentin Melero')

    ## Fonction pour rejouer
    def rejouer():
        """ Fonction pour la commande rejouer """
        Mafenetre.destroy()
        Jeu()

    ## Fonction pour indiquer au joueur qu'il a gagné 
    def gagne():
        Gagne = True
        for alien in Aliens :
            if alien.alive == True :
                Gagne = False
        if Gagne == True :
            buttonRecommencer = Button (Mafenetre, text="RECOMMENCER", fg ='black', bg='white',relief='groove', command = rejouer)
            buttonRecommencer.place(x=200, y=400, width=300, height=100)
            buttonQuitt = Button (Mafenetre, text="QUITTER", fg ='black', bg='white',relief='groove', command = Mafenetre.destroy)
            buttonQuitt.place(x=500, y=400, width=300, height=100)
            Bravo = Label(Mafenetre, text='Bravo, tu as gagné.', bg='white',fg='black', font=100)
            Bravo.place(x=200, y=300, width=600, height=50)
        else :
            Mafenetre.after(1000,gagne)
    gagne()    
    
    ## Fonction de déplacement pour le missile du vaisseau
    def creation_missile():
        """ Fonction qui gères la création du missile du vaisseau """
        missile = class_missile(vaisseau.Xv,vaisseau.Yv)
        missile_balle = CanvaJeu.create_oval(vaisseau.Xv-missile.RAYON_m, vaisseau.Yv-missile.RAYON_m, vaisseau.Xv+missile.RAYON_m, vaisseau.Yv+missile.RAYON_m, width=1, outline='black', fill='white')
        def deplacement_missile():
            """ Fonction qui gères le déplacement du missile du vaisseau """
            # Dispararition du missile si hors de le fenêtre de jeu
            if missile.Ym - missile.RAYON_m + missile.DY_m < 0:
                CanvaJeu.delete(missile)
            else :
                missile.Ym = missile.Ym - missile.DY_m
                CanvaJeu.coords(missile_balle,missile.Xm-missile.RAYON_m, missile.Ym-missile.RAYON_m, missile.Xm+missile.RAYON_m, missile.Ym+missile.RAYON_m)
                if not disparition(alien1,missile_balle,missile):
                    Mafenetre.after(30,deplacement_missile)
        deplacement_missile()

    ## Fonction de déplacement pour le missile des aliens
    def creation_missile_alien():
        """ Fonction qui gères la création du missile des aliens """
        if alien1.alive == True :
            missile_alien1 = class_missile(alien1.Xa,alien1.Ya)
            missile_balle_alien1 = CanvaJeu.create_oval(alien1.Xa-missile_alien1.RAYON_m, alien1.Ya-missile_alien1.RAYON_m, alien1.Xa+missile_alien1.RAYON_m, alien1.Ya+missile_alien1.RAYON_m, width=1, outline='black', fill='white')
        if alien2.alive == True :    
            missile_alien2 = class_missile(alien2.Xa,alien2.Ya)
            missile_balle_alien2 = CanvaJeu.create_oval(alien2.Xa-missile_alien2.RAYON_m, alien2.Ya-missile_alien2.RAYON_m, alien2.Xa+missile_alien2.RAYON_m, alien2.Ya+missile_alien2.RAYON_m, width=1, outline='black', fill='white')
        if alien3.alive == True :    
            missile_alien3 = class_missile(alien3.Xa,alien3.Ya)
            missile_balle_alien3 = CanvaJeu.create_oval(alien3.Xa-missile_alien3.RAYON_m, alien3.Ya-missile_alien3.RAYON_m, alien3.Xa+missile_alien3.RAYON_m, alien3.Ya+missile_alien3.RAYON_m, width=1, outline='black', fill='white')
        def deplacement_missile_alien(missile_alien,missile_balle_alien):
            """ Fonction qui gères le déplacement du missile des alliens """
            # Dispararition du missile si hors de le fenêtre de jeu
            if missile_alien.Ym + missile_alien.RAYON_m - missile_alien.DY_m > 600 :
                CanvaJeu.delete(missile_alien)
            else :
                missile_alien.Ym = missile_alien.Ym + missile_alien.DY_m
                #CanvaJeu.coords(missile_balle_alien,missile_alien.Xm-missile_alien.RAYON_m, missile_alien.Ym-missile_alien.RAYON_m, missile_alien.Xm+missile_alien.RAYON_m, missile_alien.Ym+missile_alien.RAYON_m)
                CanvaJeu.move(missile_balle_alien,0,missile_alien.DY_m)
                if not disparition_missille_alien(vaisseau,missile_balle_alien,missile_alien):
                    Mafenetre.after(50,lambda:deplacement_missile_alien(missile_alien,missile_balle_alien))
        if alien1.alive == True :
            deplacement_missile_alien(missile_alien1,missile_balle_alien1)
        if alien2.alive == True :
            deplacement_missile_alien(missile_alien2,missile_balle_alien2)
        if alien3.alive == True :
            deplacement_missile_alien(missile_alien3,missile_balle_alien3)
        Mafenetre.after(900,creation_missile_alien)
    creation_missile_alien()

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
        """ Fonction qui indique au joueur qu'il a perdu """
        Perdu = False
        if alien1.Ya + alien1.RAYON_a >= vaisseau.Xv or alien2.Ya + alien2.RAYON_a >= vaisseau.Xv or alien3.Ya + alien3.RAYON_a >= vaisseau.Xv  :
            Perdu = True
            CanvaJeu.delete(vaisseau_obj)
            CanvaJeu.delete(alien1_obj)
        if donnee_jeu.Vie <= 0:
            Perdu = True
        if Perdu == True:
            buttonRecommencer = Button (Mafenetre, text="RECOMMENCER", fg ='black', bg='white',relief='groove', command = rejouer)
            buttonRecommencer.place(x=200, y=400, width=300, height=100)
            buttonQuitt = Button (Mafenetre, text="QUITTER", fg ='black', bg='white',relief='groove', command = Mafenetre.destroy)
            buttonQuitt.place(x=500, y=400, width=300, height=100)
            partie_perdu = Label(Mafenetre, text='Dommage, tu as perdu', bg='white',fg='black', font=100)
            partie_perdu.place(x=200, y=300, width=600, height=50)
        else : 
            Mafenetre.after(1000,fin_de_partie)
    fin_de_partie()

    ## Tout ce qui est lié à l'interface graphique ##

   
    # Création d'un widget Menu
    menubar = Menu(Mafenetre)
    menuoption = Menu(menubar,tearoff =0)
    menuoption.add_command(label="Recommencer une partie", command = Mafenetre.destroy) # Boutton pour recommencer une partie
    menuoption.add_command(label="A propos", command = apropos)
    menuoption.add_command(label="Quitter le jeu", command = Mafenetre.destroy) # Boutton pour quitter 
    menubar.add_cascade(label="Option", menu = menuoption)


    # Affichage du menu
    Mafenetre.config(menu = menubar)

    # Création d'un widget Button (Boutton jouer)
    buttonRecommencer = Button (Mafenetre, text="RECOMMENCER", fg ='white', bg='black',relief='groove', command = rejouer)
    buttonRecommencer.place(x=1050, y=250, width=100, height=50)

    # Création d'un widget Label (Pour afficher le score)
    Score(donnee_jeu)

    # Création d'un widget Label (Pour afficher le nombre de vie du joueur)
    NbVie(donnee_jeu)

    # Création d'un widget Button (boutton quitter)
    buttonQuitt = Button (Mafenetre, text="QUITTER", fg ='white', bg='black',relief='groove', command = Mafenetre.destroy)
    buttonQuitt.place(x=1050, y=450, width=100, height=50)

    Mafenetre.mainloop()
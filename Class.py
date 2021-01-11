## Page pour gérer les classes et toutes les variables de mes fonctions du programme Principale.py ##

import math

class jeu_Spaceinvaders:
    def __init__(self, Mafenetre):
        # Stock des données du jeu SpaceInvaders
        self.Mafenetre = Mafenetre
        self.Vie = 3

class class_allien:
    def __init__(self, Mafenetre):
        # Stock des infos sur l'allien
        self.Xa = 500
        self.Ya = 100
        self.vitesse_a = 4
        self.n = 0
        self.DX_a = self.vitesse_a
        self.RAYON_a = 20
        

class class_vaisseau:
    def __init__(self, Mafenetre):
        # Stock des infos sur le vaisseau
        self.Xv = 500
        self.Yv = 580


class class_missile:
    def __init__(self, Mafenetre,X,Y):
        # Stock des infos sur le missile
        self.Xm = X
        self.Ym = Y
        self.vitesse_m = 15
        self.DY_m = self.vitesse_m
        self.RAYON_m = 10

class class_bloc1:
    def __init__(self,Mafenetre):
        # Stock des infos sur le bloc 1
        self.X1 = 200
        self.Y1 = 400

class class_bloc2:
    def __init__(self,Mafenetre):
        # Stock des infos sur le bloc 2
        self.X2 = 500
        self.Y2 = 400

class class_bloc3:
    def __init__(self,Mafenetre):
        # Stock des infos sur le bloc 3
        self.X3 = 800
        self.Y3 = 400

## Page pour gérer les classes et toutes les variables de mes fonctions du programme Principale.py ##

import math


class jeu_Spaceinvaders:
    def __init__(self, Mafenetre):
        # Stock des données du jeu SpaceInvaders
        self.Mafenetre = Mafenetre
        self.Vie = 3

class info_allien:
    def __init__(self, Mafenetre):
        # Stock des infos sur l'allien
        self.Xa = 500
        self.Ya = 100
        self.vitesse_a = 5
        self.n = 0
        self.DX_a = self.vitesse_a
        self.RAYON_a = 20

class info_vaisseau:
    def __init__(self, Mafenetre):
        # Stock des infos sur le vaisseau
        self.Xv = 500
        self.Yv = 580


class class_missile:
    def __init__(self, Mafenetre,X,Y):
        # Stock des infos sur le missile
        self.Xm = X
        self.Ym = Y
        self.vitesse_m = 10
        self.DY_m = self.vitesse_m
        self.RAYON_m = 10

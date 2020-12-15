from tkinter import Tk, Label, Button, PhotoImage, Menu, Entry, StringVar, Canvas
from Vaisseau import PosX, PosY, CanvaJeu, vaisseau

def Clavier(event):
    """ Gestion de l'évènement Appui sur une touche du clavier"""
    
    touche = event.keysym
    print(touche)
    # déplacement vers la droite 
    if touche == '<Right>':
        PosX += 20
    # déplacement vers la gauche
    if touche == '<Left>':
        PosX -= 20
    # On dessine le pion à sa nouvelle position
    CanvaJeu.coords(vaisseau,PosX-10, PosY-10, PosX+10, PosY+10)

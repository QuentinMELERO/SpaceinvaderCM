from tkinter import Tk, Canvas, Button
import math, random

RAYON = 15 # Rayon de l'alien

# Direction
DX = 5

def deplacement(Mafenetre, CanvaFond, Alien):
    global DX,RAYON
    largeur = 1000
    hauteur = 600
    x = largeur/2
    y = hauteur/2
    if Canvas.bbox(Alien)+RAYON+DX > largeur:
        Canvas.bbox(Alien) = 2*(largeur-RAYON)-Canvas.bbox(Alien)
        DX = -DX
    
    if bbox(Alien)-RAYON+DX < 0:
        Canvas.bbox(Alien) = 2*RAYON-Canvas.bbox(Alien)
        DX = -DX

    Canvas.bbox(Alien) = Canvas.bbox(Alien)+DX

    # affichage
    CanvaFond.move(Alien, x-RAYON,y-RAYON,x+RAYON,y+RAYON)

    # Mise à jour toutes les 50ms
    Mafenetre.after(20,deplacement)


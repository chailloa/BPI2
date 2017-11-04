#!/usr/env/bin python3
"""
SVG
"""
from random import randint

def entete(largeur, hauteur):
    """ Affiche la balise entete du fichier svg. """
    print('<svg width="{}" height="{}">'.format(largeur, hauteur))

def couleur_aleatoire():
    """ Renvoie une couleur (en rgb, vecteur de taille 3) aléaleatoirement. """
    return [randint(0, 255) for _ in range(3)]

def affiche_triangle(triangle_tourne, couleur):
    """
    traingle_tourne est un objet de la classe Triangle.
    couleur (en rgb) est un vecteur de taille 3.
    Affiche un polygon svg à 3 points, ie un triangle.
    """
    print('<polygon points="{},{} {},{} {},{}" style="fill:rgb({},{},{});opacity:0.8"/>'
          .format(
              triangle_tourne.pt1.abs,
              triangle_tourne.pt1.ord,
              triangle_tourne.pt2.abs,
              triangle_tourne.pt2.ord,
              triangle_tourne.pt3.abs,
              triangle_tourne.pt3.ord,
              couleur[0],
              couleur[1],
              couleur[2],
              )
         )

def pied():
    """ Affiche la balise fermante du fichier svg. """
    print("</svg>")

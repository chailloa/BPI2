#!/usr/bin/env python3
"""
Point
"""
from random import randrange
from math import cos, sin

class Point:
    """Classe Point avec 2 attributs : abscisse et ordonnée"""
    def __init__(self, coordonnees):
        """Construit un point."""
        self.abs = coordonnees[0]
        self.ord = coordonnees[1]

    def __str__(self):
        """ Affiche le point. """
        return "Point :\n\tabs = " + str(self.abs) + "\n\tord = " + str(self.ord)

    def method(self):
        """DOC"""
        pass
    def method2(self):
        """Doc"""
        pass

def point_aleatoire(intervalle_largeur, intervalle_hauteur):
    """
    Retourne un Point de coordonnees aleatoires.
    """
    abscisse = randrange(intervalle_largeur[0], intervalle_largeur[1])
    ordonnee = randrange(intervalle_hauteur[0], intervalle_hauteur[1])
    return Point([abscisse, ordonnee])

def rotation(point, centre, angle):
    """ Réalise une rotation circulaire selon l'angle donné. """
    diff_abs = (point.abs - centre.abs)
    diff_ord = (point.ord - centre.ord)
    new_abs = (diff_abs * cos(angle)) - (diff_ord * sin(angle)) + centre.abs
    new_ord = (diff_abs * sin(angle)) - (diff_ord * cos(angle)) + centre.ord
    return Point((new_abs, new_ord))

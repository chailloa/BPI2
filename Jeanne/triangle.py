#!/usr/bin/env python3
"""
Triangle
"""
import point

class Triangle:
    """
    Classe Traingle avec 3 attributs :
    Point pt1
    Point pt2
    Point pt3
    """
    def __init__(self, points):
        """
        Crée un triangle.
        points est un vecteur de 3 Point.
        """
        self.pt1 = points[0]
        self.pt2 = points[1]
        self.pt3 = points[2]

    def __str__(self):
        return ("---Triangle---\n" +
                "Point 1 :\n\tabs = " + str(self.pt1.abs)
                + "\n\tord = " + str(self.pt1.ord)
                + "\nPoint 2 :\n\tabs = " + str(self.pt2.abs)
                + "\n\tord = " + str(self.pt2.ord)
                + "\nPoint 3 :\n\tabs = " + str(self.pt3.abs)
                + "\n\tord = " + str(self.pt3.ord))

    def rotation_autour(self, centre, angle):
        """ Réalise une rotation circulaire selon l'angle donné. """
        return Triangle(
            [point.rotation(self.pt1, centre, angle),
             point.rotation(self.pt2, centre, angle),
             point.rotation(self.pt3, centre, angle)])

    def method(self):
        """Doc"""
        pass

def triangle_aleatoire(intervalle_largeur, intervalle_hauteur):
    """
    Renvoie un Triangle qui rentre dans l'intervalle de largeur et hauteur donnés.
    intervalle sont des vecteurs de taille 2.
    """
    return Triangle(
        [point.point_aleatoire(intervalle_largeur, intervalle_hauteur)
         for _ in range(3)])

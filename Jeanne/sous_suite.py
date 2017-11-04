#!/usr/bin/env python3
"""
04/10/2017 @Jeanne Marcade
INP-Ensimag 1A_g3
Basesfiles de la programmation
TP2
Exo2_6 Sous-Suites

On souhaite effectuer une analyse d’un fichier texte contenant une suite de nombres.
"""
import sys


def converti_f_chaine(fichier):
    """
    Ouvre le fichier et concatène les lignes en chaine de caractères.
    """
    chaine = ''
    with open(fichier, "r") as fichier_suite:
        chaine = fichier_suite.read()
    return chaine

def separe_sous_suites(liste):
    """
    Crée un iterator
    Sépare les sous-suites de nombres de la liste donnée en argument.
    """
    sous_suite = [liste[0]]
    num_pre = liste[0]
    liste.pop(0)
    egaux = []
    croissant = True

    for num in liste:
        if num_pre < num:
            if not croissant:
                yield sous_suite
                if len(egaux) != 0:
                    sous_suite = egaux
                    sous_suite.append(num_pre)
                    egaux = []
                else:
                    sous_suite = [num_pre, num]
                croissant = True
            else:
                sous_suite.append(num)

        elif num_pre == num:
            if (len(egaux) != 0) and (num != egaux[0]):
                egaux = []
            egaux.append(num)
            sous_suite.append(num)

        else:
            if croissant:
                yield sous_suite
                if len(egaux) != 0:
                    sous_suite = egaux
                    sous_suite.append(num_pre)
                    egaux = []
                else:
                    sous_suite = [num_pre, num]
                croissant = False
            else:
                sous_suite.append(num)
        num_pre = num

def analyse_suite(suite):
    """
    Analyse la suite
    """
    #suite = suite.split('\n')
    suite = suite.split( )      #splt( ) avec un espace en argument sépare les
                                #lignes et les mots !!!
    #Analyse de la liste
    max_taille = 0
    for ss_suite in separe_sous_suites(suite):
        if max_taille < len(ss_suite):
            max_taille = len(ss_suite)
            max_ss_suite = ss_suite
    return max_ss_suite

def main():
    """
    On genere un svg plateau a partir d'une taille d'image attendue.
    Recupere le 2e argument de la ligne de commande.
    """
    if len(sys.argv) != 2 or sys.argv[0] == "-h" or sys.argv[0] == "--help":
        print("utilisation:", sys.argv[0], " fichier.txt")
        sys.exit(1)
    #On récupère le 2e argument de la ligne de commande.
    #On pourrait utiliser les redirection. Dans ce cas : main(argument)
    suite = converti_f_chaine(sys.argv[1])
    print("la plus grande sous_suite est : ")
    print(analyse_suite(suite))


if __name__ == "__main__":
    main()

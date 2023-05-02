
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 10:20:46 2023

Le jeu de la vie 


 Dans le jeu de la vie, chaque cellule peut avoir deux états :

    vivante .
    morte.

L'état d'une cellule au tour suivant dépend de l'état de ses huit voisins
 directs. Il y a deux règles simples qui s'appliquent :

    une cellule morte possédant exactement trois voisines vivantes devient
    vivante : elle naît ;
    une cellule vivante possédant deux ou trois voisines vivantes le reste, 
    sinon elle meurt.

On va représenter l'état de nos cellules dans un tableau à deux dimansions ,
une cellule étant représentée par un 0 si elle est morte et un 1 sinon.
On importera le module os , pour afficher le tableau, la méthode est donnée .
On importera le module time pour donner un nombre de secondes de pause 
entre deux états du tableau.


@author: Bruno
"""
import os
import time


class JeuDeLaVie:
    def __init__ (self, tableau):
        self.tableau = tableau
        
    def affiche(self):
        #os.system('cls')
        print(self.tableau)

    def affiche_graphique(self):
        graph = self.tableau.copy()
        for ligne in graph:
            for key in ligne:
                print(key,end='\t')
            print()
        
    def run (self, tours,delai):
        for i in range(tours):
            self.tour()
            self.affiche_graphique()
            print('--------------------------------------')
            time.sleep(delai)
                
    def valeur_case(self, i, j):
        """Renvoie la valeur de la case [i][j] ou 0 si la case n’existe pas."""
        # sample: if index >= 0 and index < len(list)
        if i >= 0 and i < len(self.tableau):
            if j >= 0 and j < len(self.tableau[i]):
                return self.tableau[i][j]
        return 0
    
    def total_voisins(self, i, j):
        """Renvoie la somme des valeurs des voisins de la case [i][j]."""
        up = self.valeur_case(i-1, j)
        down = self.valeur_case(i+1, j)
        left = self.valeur_case(i, j-1)
        right = self.valeur_case(i, j+1)

        up_left = self.valeur_case(i-1, j-1)
        up_right = self.valeur_case(i-1, j+1)
        down_left = self.valeur_case(i+1, j-1)
        down_right = self.valeur_case(i+1, j+1)
        return up + down + left + right + up_left + up_right + down_left + down_right
                
    def resultat(self, valeur_case, total_voisins):
        if valeur_case == 0:
            if total_voisins == 3:
                return 1
        if valeur_case == 1:
            if total_voisins == 2 or total_voisins == 3:
                return 1
        return 0
        
    def tour(self):
        new_table = self.tableau
        for i in range(len(self.tableau)):
            for j in range(len(self.tableau[i])):
                new_table[i][j] = self.resultat(self.valeur_case(i, j), self.total_voisins(i, j))
        self.tableau = new_table



l=[[1,1,0,1,0],
   [0,1,1,1,0],
   [0,0,0,1,0]]       

a = JeuDeLaVie(l)

a.run(8, 0.2)


"""
OUTPUT:
[[1, 1, 0, 1, 0], 
[1, 0, 0, 1, 1], 
[0, 0, 0, 1, 1]]

[[1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0], 
[0, 0, 0, 0, 0]]

[[1, 1, 1, 1, 0], 
[1, 0, 1, 1, 0], 
[0, 0, 0, 0, 0]]

[[1, 0, 1, 1, 0], 
[0, 1, 0, 1, 0], 
[0, 0, 0, 0, 0]]

[[0, 0, 1, 1, 0], 
[0, 0, 1, 1, 0], 
[0, 0, 0, 0, 0]]

[[0, 0, 1, 1, 0], 
[0, 0, 1, 1, 0], 
[0, 0, 0, 0, 0]]

[[0, 0, 1, 1, 0],
[0, 0, 1, 1, 0], 
[0, 0, 0, 0, 0]]

[[0, 0, 1, 1, 0], 
[0, 0, 1, 1, 0], 
[0, 0, 0, 0, 0]]
"""
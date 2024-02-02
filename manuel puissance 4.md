1:Installation

Posseder un IDE de votre choix
Installer les dependence requis pygame,nympy a l'aide des commande python sur votre IDE
Ouvrir le fichier main.py et executer le si tous ce passe bien vous devrier avoir une fenetre qui ces ouvert avec le menu principal

2 comment jouer
une fois le programme ouvert vous arriver sur le menu de selection d'un niveau
selectionner un niveau et commencer a afronter votre advesaire
si gagner ou perder vous retourner au menue de selection du niveau
voila a vous de jouer

3 technologie utiliser

language : Python 3.11
bibliotheque utiliser : Pygame-ce , nympy

4 Regle du jeux

Le but du jeu est d'aligner une suite de 4 pions de même couleur sur une grille comptant 6 rangées et 7 colonnes. Chaque joueur dispose de 21 pions d'une couleur (par convention, en général jaune ou rouge). Tour à tour, les deux joueurs placent un pion dans la colonne de leur choix, le pion coulisse alors jusqu'à la position la plus basse possible dans ladite colonne à la suite de quoi c'est à l'adversaire de jouer. Le vainqueur est le joueur qui réalise le premier un alignement (horizontal, vertical ou diagonal) consécutif d'au moins quatre pions de sa couleur. Si, alors que toutes les cases de la grille de jeu sont remplies, aucun des deux joueurs n'a réalisé un tel alignement, la partie est déclarée nulle.
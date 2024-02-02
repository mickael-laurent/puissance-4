import numpy as np
import math
import pygame
import random
import sys

# les constantes
LARGEUR_CASE = 100
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)
JAUNE = (255, 255, 0)
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
VERT = (0, 255, 0)
ROUGE_CLAIR = (254, 180, 180)
VERT_CLAIR = (33, 255, 33)
BLEU_CLAIR = (0, 176, 240)
VIOLET = (153, 0, 204)
VIOLET_CLAIR = (232, 167, 255)
RAYON = int(LARGEUR_CASE / 2) - 4
NB_LIGNE = 6
NB_COLONNE = 7
ORDINATEUR = 1
HUMAIN = 2
CASE_VIDE = 0
GAGNANT_ORDI = 3
GAGNANT_HUMAIN = 4
COULEUR_ORDI = ROUGE
COULEUR_HUMAIN = JAUNE
COULEUR_GAGNANT = VERT


# =============================================================================
#     -------------------------Pygame-----------------------------------
# =============================================================================

# dessiner le plateau de jeu
# Dessine la structure du jeu et les jetons de différentes couleurs
# Si les valeurs du plateau sont 3 ou 4 alors il faut dessiner un jeton gagnant
# c'est à dire un jeton vert posé sur le jeton de la couleur du gagnant.
# Cela permet de repérer l'alignement gagnant.
def dessiner_plateau(plateau):
    pygame.draw.rect(ecran, BLEU, (0, LARGEUR_CASE, NB_COLONNE * LARGEUR_CASE, (NB_LIGNE + 1) * LARGEUR_CASE))
    for c in range(NB_COLONNE):
        for r in range(NB_LIGNE):
            # pygame.draw.rect(ecran,BLEU,(c*LARGEUR_CASE,r*LARGEUR_CASE+LARGEUR_CASE,LARGEUR_CASE,LARGEUR_CASE))
            pygame.draw.circle(ecran, NOIR, (
                int(c * LARGEUR_CASE + LARGEUR_CASE / 2), int(r * LARGEUR_CASE + LARGEUR_CASE / 2 + LARGEUR_CASE)),
                               RAYON)
    for c in range(NB_COLONNE):
        for r in range(NB_LIGNE):
            if plateau[r][c] == ORDINATEUR:
                pygame.draw.circle(ecran, COULEUR_ORDI, (
                    int(c * LARGEUR_CASE + LARGEUR_CASE / 2), hauteur - int(r * LARGEUR_CASE + LARGEUR_CASE / 2)),
                                   RAYON)
            if plateau[r][c] == HUMAIN:
                pygame.draw.circle(ecran, COULEUR_HUMAIN, (
                    int(c * LARGEUR_CASE + LARGEUR_CASE / 2), hauteur - int(r * LARGEUR_CASE + LARGEUR_CASE / 2)),
                                   RAYON)
            if plateau[r][c] == GAGNANT_ORDI:
                pygame.draw.circle(ecran, COULEUR_ORDI, (
                    int(c * LARGEUR_CASE + LARGEUR_CASE / 2), hauteur - int(r * LARGEUR_CASE + LARGEUR_CASE / 2)),
                                   RAYON)
                pygame.draw.circle(ecran, COULEUR_GAGNANT, (
                    int(c * LARGEUR_CASE + LARGEUR_CASE / 2), hauteur - int(r * LARGEUR_CASE + LARGEUR_CASE / 2)),
                                   RAYON - 15)
            if plateau[r][c] == GAGNANT_HUMAIN:
                pygame.draw.circle(ecran, COULEUR_HUMAIN, (
                    int(c * LARGEUR_CASE + LARGEUR_CASE / 2), hauteur - int(r * LARGEUR_CASE + LARGEUR_CASE / 2)),
                                   RAYON)
                pygame.draw.circle(ecran, COULEUR_GAGNANT, (
                    int(c * LARGEUR_CASE + LARGEUR_CASE / 2), hauteur - int(r * LARGEUR_CASE + LARGEUR_CASE / 2)),
                                   RAYON - 15)

            pygame.display.update()


# -------------------------------------------------------------------------

# La page d'introduction avec ses boutons de niveaux
def intro_jeu(ecran):
    largeur_ecran = NB_COLONNE * LARGEUR_CASE
    hauteur_ecran = (NB_LIGNE + 1) * LARGEUR_CASE
    intro = True
    ecran.fill(NOIR)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # On a cliqué sur un bouton: si on a cliqué en dehors
                # d'un bouton, c'est le niveau 1 qui est lancé
                intro = False
        # affichage du texte
        pygame.font.init()
        font = pygame.font.SysFont("comicsansms", 40)
        texteSurface = font.render("Selectionner un niveau", True, BLANC)
        texteRectangle = texteSurface.get_rect()
        texteRectangle.center = ((largeur_ecran / 2), (hauteur_ecran / 2) - 150)
        ecran.blit(texteSurface, texteRectangle)
        # création des boutons
        button(ecran, "Niveau 1", 150, (hauteur_ecran / 2), 100, 50, VERT, VERT_CLAIR, jouer_niveau1)
        button(ecran, "Niveau 2", 280, (hauteur_ecran / 2), 100, 50, ROUGE, ROUGE_CLAIR, jouer_niveau2)
        button(ecran, "Niveau 3", 410, (hauteur_ecran / 2), 100, 50, BLEU, BLEU_CLAIR, jouer_niveau3)
        button(ecran, "FIN", 540, (hauteur_ecran / 2), 100, 50, VIOLET, VIOLET_CLAIR, jouer_fin)
        pygame.display.update()


def button(ecran, msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # si la souris survole le bouton, on lui met sa couleur claire
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(ecran, ac, (x, y, w, h))
        # Si on a cliqué sur le bouton, on exécute l'action
        if click[0] == 1 and action != None:
            action()
    else:
        # si la souris est en dehors du bouton, on lui met sa couleur normal
        pygame.draw.rect(ecran, ic, (x, y, w, h))
    # Ecriture du texte sur le bouton
    pygame.font.init()
    font = pygame.font.SysFont("comicsansms", 20)
    texteSurface = font.render(msg, True, BLANC)
    texteRectangle = texteSurface.get_rect()
    texteRectangle.center = ((x + (w / 2)), (y + (h / 2)))
    ecran.blit(texteSurface, texteRectangle)


def jouer_niveau1():
    global profondeur
    profondeur = 1


def jouer_niveau2():
    global profondeur
    profondeur = 2


def jouer_niveau3():
    global profondeur
    profondeur = 3


def jouer_fin():
    global fin_jeu
    fin_jeu = True


# =============================================================================
#     -------------------------partie console----------------------------------
# =============================================================================

# créer une matrice NB_LIGNE, NB_COLONNE remplie de zeros
def creer_plateau():
    plateau = np.zeros((NB_LIGNE, NB_COLONNE), dtype=int)
    return plateau


# afficher la matrice en inversant l'ordre des lignes
def afficher_plateau(plateau):
    print(np.flip(plateau, 0))


# Y a t'il encore de la place dans la colonne choisie
def emplacement_valide(plateau, colonne):
    if plateau[NB_LIGNE - 1][colonne] == 0:
        return True
    else:
        return False


# le dernier jeton placé est-il gagnant
# On teste dans toutes les directions, s'il y a 4 jetons identiques qui se suivent
# Si l'on trouve un coup gagnant et si la modification du plateau est autorisée
# on indique sur le plateau les cases gagnantes de façon à les afficher autrement
def coup_gagnant(plateau, jeton, modif):
    if jeton == ORDINATEUR:
        gagnant = GAGNANT_ORDI
    else:
        gagnant = GAGNANT_HUMAIN

    # test de toutes les positions horizontales
    for c in range(NB_COLONNE - 3):
        for r in range(NB_LIGNE):
            if plateau[r][c] == jeton and plateau[r][c + 1] == jeton and plateau[r][c + 2] == jeton and plateau[r][
                c + 3] == jeton:
                if modif:
                    plateau[r][c] = gagnant
                    plateau[r][c + 1] = gagnant
                    plateau[r][c + 2] = gagnant
                    plateau[r][c + 3] = gagnant
                return True

    # test de toutes les positions verticales
    for c in range(NB_COLONNE):
        for r in range(NB_LIGNE - 3):
            if plateau[r][c] == jeton and plateau[r + 1][c] == jeton and plateau[r + 2][c] == jeton and plateau[r + 3][
                c] == jeton:
                if modif:
                    plateau[r][c] = gagnant
                    plateau[r + 1][c] = gagnant
                    plateau[r + 2][c] = gagnant
                    plateau[r + 3][c] = gagnant
                return True

    # test de toutes les positions diagonales orientées vers la droite
    for c in range(NB_COLONNE - 3):
        for r in range(NB_LIGNE - 3):
            if plateau[r][c] == jeton and plateau[r + 1][c + 1] == jeton and plateau[r + 2][c + 2] == jeton and \
                    plateau[r + 3][c + 3] == jeton:
                if modif:
                    plateau[r][c] = gagnant
                    plateau[r + 1][c + 1] = gagnant
                    plateau[r + 2][c + 2] = gagnant
                    plateau[r + 3][c + 3] = gagnant
                return True

    # test de toutes les positions diagonales orientées vers la gauche
    for c in range(NB_COLONNE - 3):
        for r in range(3, NB_LIGNE):
            if plateau[r][c] == jeton and plateau[r - 1][c + 1] == jeton and plateau[r - 2][c + 2] == jeton and \
                    plateau[r - 3][c + 3] == jeton:
                if modif:
                    plateau[r][c] = gagnant
                    plateau[r - 1][c + 1] = gagnant
                    plateau[r - 2][c + 2] = gagnant
                    plateau[r - 3][c + 3] = gagnant
                return True


# Y at'il encore des places vides dans la matrice
def partie_nulle(plateau):
    for c in range(NB_COLONNE):
        for r in range(NB_LIGNE):
            if plateau[r][c] == 0:
                return False
    return True


# =============================================================================
# ------------------------Partie IA-----------------------------------------
# =============================================================================

def Applique_Coup(tableau, col, joueur):
    ligne = NB_LIGNE - Cases_libres_colonnes(tableau, col)
    tableau[ligne][col] = joueur
    return tableau


# renvoie le nombre de cases libres dans une colonne
def Cases_libres_colonnes(tableau, col):
    resultat = 0
    for lig in range(NB_LIGNE):
        if tableau[lig][col] == 0:
            resultat += 1
    return resultat


# une case est t'elle intéressante dans une direction donnée
# peut-on y aligner 4 jetons?
def Interet_Case_Direction(tableau, ligne, colonne, dx, dy, joueur):
    maxx = colonne + 3 * dx
    maxy = ligne + 3 * dy
    if (maxx > NB_COLONNE - 1) or (maxx < 0) or (maxy > NB_LIGNE - 1) or (maxy < 0):
        return 0
    else:
        if joueur == ORDINATEUR:
            adversaire = HUMAIN
        else:
            adversaire = ORDINATEUR

        i = 0
        # les cases vides ou occupées par le joueur sont intéressantes
        while (i < 4) and (tableau[ligne + i * dy][colonne + i * dx] != adversaire):
            i += 1
        if i == 4:
            return 1
        else:
            return 0


# Une case est elle interessante en regardant toutes les directions
def Interet_Case(tableau, ligne, colonne, joueur):
    resultat = Interet_Case_Direction(tableau, ligne, colonne, 1, 0, joueur) + \
               Interet_Case_Direction(tableau, ligne, colonne, 1, 1, joueur) + \
               Interet_Case_Direction(tableau, ligne, colonne, 0, 1, joueur) + \
               Interet_Case_Direction(tableau, ligne, colonne, 1, -1, joueur) + \
               Interet_Case_Direction(tableau, ligne, colonne, -1, 1, joueur) + \
               Interet_Case_Direction(tableau, ligne, colonne, -1, -1, joueur)
    return resultat


# pour le joueur l'état actuel du plateau est-il intéressant
def Interet_Plateau(tableau, joueur):
    resultat = 0
    for col in range(NB_COLONNE):
        for lig in range(NB_LIGNE):
            resultat += Interet_Case(tableau, lig, col, joueur)

    return resultat


# On regarde l'intéret de plateau pour l'ordinateur et pour l'humain
# La valeur du plateau est la différence des deux.
def Valeur_Terminale(tableau):
    return Interet_Plateau(tableau, ORDINATEUR) - Interet_Plateau(tableau, HUMAIN)


# On parcourt l'arbre min_max jusqu'à une certaine profondeur
def Valeur_MinMax(tableau, prof, est_max):
    gagne = coup_gagnant(tableau, ORDINATEUR, False)
    if gagne:
        return 10000
    gagne = coup_gagnant(tableau, HUMAIN, False)
    if gagne:
        return -10000
    if prof == 0:
        return Valeur_Terminale(tableau)
    # coup possible de l'ordinateur à cette profondeur
    if est_max:
        # coup possible de l'ordinateur
        resultat = -10001
        # Pour chaque colonne du tableau à cette profondeur
        for col in range(NB_COLONNE):
            if Cases_libres_colonnes(tableau, col) > 0:
                # Travailler sur une copie du plateau
                tableau2 = np.copy(tableau)
                # calculer son score à la profondeur donnée
                score = Valeur_MinMax(Applique_Coup(tableau2, col, ORDINATEUR), prof - 1, False)
                if score > resultat:
                    resultat = score
        return resultat
    else:
        # coup possible du joueur
        resultat = 10001
        for col in range(NB_COLONNE):
            # Pour chaque colonne du plateau à cette profondeur
            if Cases_libres_colonnes(tableau, col) > 0:
                # Travailler sur une copie du plateau
                tableau2 = np.copy(tableau)
                # calculer son score à la profondeur donnée
                score = Valeur_MinMax(Applique_Coup(tableau2, col, HUMAIN), prof - 1, True)
                if score < resultat:
                    resultat = score
        return resultat


# recherche du meilleur coup à jouer pour l'ordinateur
def Decision_MinMax(tableau, profmax):
    resultat = -1
    bscore = -10001
    for col in range(NB_COLONNE):
        if Cases_libres_colonnes(tableau, col) > 0:
            # on clacul la valeur_MinMax pour chaque colonne du plateau
            tableau2 = np.copy(tableau)
            score = Valeur_MinMax(Applique_Coup(tableau2, col, ORDINATEUR), profmax, False)
            if score > bscore:
                bscore = score
                resultat = col
                # print("score ", score, "col: ", col)

    return resultat


# =============================================================================
#                      Début partie
# =============================================================================

pygame.init()
profondeur = 1
largeur = NB_COLONNE * LARGEUR_CASE
hauteur = (NB_LIGNE + 1) * LARGEUR_CASE
taille = (largeur, hauteur)
ecran = pygame.display.set_mode(taille)
fin_jeu = False

# page d'instructions
intro_jeu(ecran)
while not fin_jeu:
    # ------------------------------------------------------------------------
    plateau = creer_plateau()
    game_over = False
    if profondeur == 1:
        # avec une profondeur de 1, l'ordinateur joue mal
        # alors on le laisse commencer
        tour = 1
        premierCoup = True
    else:
        # choix aléatoire de celui qui commence
        tour = random.randint(1, 2)
        premierCoup = False

    dessiner_plateau(plateau)
    # -----------------------------------------------------------------------
    # Boucle de jeu
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                fin_jeu = True
                pygame.quit()
                sys.exit()

                # on déplace le jeton avec la souris
            if event.type == pygame.MOUSEMOTION:
                # effacer la première ligne du plateau
                pygame.draw.rect(ecran, NOIR, (0, 0, largeur, LARGEUR_CASE))
                # position de la souris
                posx = event.pos[0]
                # si joueur 1 on affiche un jeton rouge, à la position x de la souris
                if tour == HUMAIN:
                    pygame.draw.circle(ecran, JAUNE, (posx, int(LARGEUR_CASE / 2)), RAYON)
                    # on met l'écran à jour
                    pygame.display.update()

                    # --------------------------------------
            if tour == HUMAIN:
                # le joueur a cliqué avec le bouton de la souris
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # effacer la première ligne du plateau
                    pygame.draw.rect(ecran, NOIR, (0, 0, largeur, LARGEUR_CASE))
                    # position de la souris au moment du clic
                    posx = event.pos[0]
                    # choix du numéro de colonne par le joueur 2
                    # calcul du numéro de colonne correspondant à l'abcisse de la souris
                    colonne = int(math.floor(posx / LARGEUR_CASE))

                    if emplacement_valide(plateau, colonne):
                        # Joue un coup dans la colonne
                        Applique_Coup(plateau, colonne, HUMAIN)
                        # tester si le joueur a gagné
                        gagne = coup_gagnant(plateau, HUMAIN, True)
                        if gagne:
                            # dessiner_plateau(plateau)
                            myfont = pygame.font.SysFont("comicsansms", 40)
                            texte_image = myfont.render("Le joueur a gagné", True, COULEUR_HUMAIN)
                            ecran.blit(texte_image, [100, 10])
                            game_over = True

                        if partie_nulle(plateau):
                            myfont = pygame.font.SysFont("comicsansms", 40)
                            texte_image = myfont.render("Partie Nulle", True, BLANC)
                            ecran.blit(texte_image, [100, 10])
                            pygame.display.update()
                            game_over = True

                        dessiner_plateau(plateau)
                        tour = ORDINATEUR

            else:
                # niveau 1, premier coup: on oblige l'ordi à jouer la colonne
                # du milieu.
                if premierCoup:
                    colonne = 3
                    premierCoup = False
                else:
                    # On fait une copie du plateau et on recherche par
                    # l'algorithme Min_Max la meilleure colonne à jouer
                    tableau = np.copy(plateau)
                    colonne = Decision_MinMax(tableau, profondeur)

                # Jouer la colonne trouvée par l'algorithme
                if emplacement_valide(plateau, colonne):
                    # Joue un coup dans la colonne
                    Applique_Coup(plateau, colonne, ORDINATEUR)
                    # tester si l'ordinateur a gagné
                    gagne = coup_gagnant(plateau, ORDINATEUR, True)
                    if gagne:
                        # dessiner_plateau(plateau)
                        myfont = pygame.font.SysFont("comicsansms", 40)
                        texte_image = myfont.render("L'ordinateur a gagné", True, COULEUR_ORDI)
                        ecran.blit(texte_image, [100, 10])
                        game_over = True

                    if partie_nulle(plateau):
                        myfont = pygame.font.SysFont("comicsansms", 40)
                        texte_image = myfont.render("Partie Nulle", True, BLANC)
                        ecran.blit(texte_image, [100, 10])
                        pygame.display.update()
                        game_over = True

                    dessiner_plateau(plateau)
                    pygame.draw.circle(ecran, COULEUR_HUMAIN, (int(LARGEUR_CASE / 2), int(LARGEUR_CASE / 2)), RAYON)
                    pygame.display.update()
                    tour = HUMAIN

    pygame.time.wait(5000)
    # page d'instructions
    intro_jeu(ecran)

pygame.quit()
sys.exit

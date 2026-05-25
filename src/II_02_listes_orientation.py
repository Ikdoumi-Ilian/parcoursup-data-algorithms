"""
Auteur : Ikdoumi Ilian
"""

from II_00_orientation import *
from math import sqrt

def affiche_liste_orientation(liste_orientation):
    """
    Rôle : Affiche les informations d'une liste de type orientation
    Type des données :
        liste_orientation : liste de type orientation 
    Résultat : aucun (affichage uniquement)
    """
    for i in range(0,len(liste_orientation)):
        print(affichage_orientation(liste_orientation[i]))
def liste_to_orientation(liste):
    """
    Rôle : Transforme une liste en une liste de type orientation
    Type des données :
        liste : liste avec trois valeurs qui rentrent dans les condition de la class orientation
    Résultat : liste de type orientation
    """
    l=orientation(float(liste[0]),liste[1],(liste[2]))
    return l

def liste_liste_to_orientation(liste_liste):
    """
    Rôle : Transforme une liste de listes en liste liste de type orientation
    Type des données :
        liste_liste : liste de type orientation
    Résultat : liste de liste de type orientation
    """
    liste_orientation=[]
    for i in range(len(liste_liste)):
        liste_orientation.append(liste_to_orientation(liste_liste[i]))
    return liste_orientation

def min_effectif_EG(liste):
    """
    Rôle : Calcule l'effectif minimum parmi une liste d'orientations
    Type des données :
        liste : liste de type orientation
    Résultat : float (minimum des effectifs)
    """
    min=liste[0].effectif_EG
    for i in range(1,len(liste)):
        if min>liste[i].effectif_EG:
            min=liste[i].effectif_EG
    return min

def max_effectif_EG(liste):
    """
    Rôle : Calcule l'effectif maximum parmi une liste d'orientations
    Type des données :
        liste : liste de type orientation
    Résultat : float (maximum des effectifs)
    """
    max=liste[0].effectif_EG
    for i in range(1,len(liste)):
        if max<liste[i].effectif_EG:
            max=liste[i].effectif_EG
    return max

def moyenne_effectif_EG(liste):
    """
    Rôle : Calcule la moyenne des effectifs dans une liste d'orientations
    Type des données :
        liste : liste de type orientation
    Résultat : float (moyenne des effectifs)
    """
    somme=0
    longeur=len(liste)
    for i in range(0,len(liste)):
        somme=somme + liste[i].effectif_EG
    moyenne=somme/longeur
    return moyenne

def ecart_type_effectif_EG(liste):
    """
    Rôle : Calcule l'écart type des effectifs dans une liste d'orientations
    Type des données :
        liste : liste de type orientation
    Résultat : float (écart type)
    """
    moy = moyenne_effectif_EG( liste )
    somme = 0
    for i in range(0,len(liste)) :
        somme = somme + (liste[i].effectif_EG-moy)**2
    Resultat = sqrt( somme/len(liste))
    return Resultat

def filtrage_orientation_region(l_orientation, nom):
    """
    Rôle : Filtrer la liste d'orientations selon une région donnée
    Type des données :
        l_orientation : liste de type orientation
        nom : str (nom de la région)
    Résultat : liste filtrée d'objets orientation
    """
    l_non_numerique_orientation=[]
    for i in range (0 , len(l_orientation)):           
        if l_orientation[i].region==nom:
            l_non_numerique_orientation.append(l_orientation[i])
    return l_non_numerique_orientation

def filtrage_orientation_filiere(l_orientation, nom):
    """
    Rôle : Filtrer la liste d'orientations selon une filière donnée
    Type des données :
        l_orientation : liste de type orientation
        nom : str (nom de la filière)
    Résultat : liste filtrée d'objets orientation
    """
    l_non_numerique_orientation=[]
    for i in range (0 , len(l_orientation)):           
        if l_orientation[i].filiere==nom:
            l_non_numerique_orientation.append(l_orientation[i])
    return l_non_numerique_orientation

def orientation_est_triee(l_orientation):
    """
    Rôle : Vérifie si la liste est triée selon l'effectif_EG croissant
    Type des données :
        l_orientation : liste de type orientation
    Résultat : booléen (True si triée)
    """
    trier_orientation = True
    i = 0
    while i < len( l_orientation )-1 and trier_orientation :
        if l_orientation[i].effectif_EG > l_orientation[i+1].effectif_EG :
            trier_orientation = False
        else :
            i = i +1
    return trier_orientation

def plus_petit_indice_min_orientation(l_orientation, debut, fin):
    """
    Rôle : Renvoie l'indice du plus petit effectif_EG entre debut et fin
    Type des données :
        l_orientation : liste de type orientation
        debut, fin : int
    Résultat : int (indice)
    """
    imin_orientation = debut
    for i in range(debut,fin):
        if l_orientation[i].effectif_EG<l_orientation[imin_orientation].effectif_EG :
            imin_orientation=i
    return imin_orientation

def triee_par_indice_min_orientation(l_orientation):
    """
    Rôle : Trie la liste d'orientation par sélection (indice du minimum)
    Type des données :
        l_orientation : liste de type orientation
    Résultat : liste triée (ordre croissant sur effectif_EG)
    """
    longueur=len(l_orientation)
    for i in range(0,len(l_orientation)-1):
        ind_min_orientation=plus_petit_indice_min_orientation(l_orientation,i,longueur)
        tmp_orientation=l_orientation[i]
        l_orientation[i]=l_orientation[ind_min_orientation]
        l_orientation[ind_min_orientation]=tmp_orientation
    return l_orientation


def mediane_triee_orientation(l_orientation):
    """
    Rôle : Calcule la médiane d'une liste triée d'orientations
    Type des données :
        l_orientation : liste triée de type orientation
    Résultat : float (médiane des effectifs)
    """
    milieu_orientation = len(l_orientation) //2
    if len(l_orientation)%2 == 0 :
        med_orientation = (l_orientation[milieu_orientation-1].effectif_EG + l_orientation[milieu_orientation].effectif_EG)/2
    else:
        med_orientation = l_orientation[milieu_orientation].effectif_EG
    return med_orientation

def modalite_totale(l_orientation):
    """
    Rôle : Renvoie la liste des valeurs distinctes de effectif_EG
    Type des données :
        l_orientation : liste triée de type orientation
    Résultat : liste de float (modalités distinctes)
    """
    modalite_totale=[l_orientation[0].effectif_EG]
    i = 1
    while i < len(l_orientation):
        if l_orientation[i-1].effectif_EG != l_orientation[i].effectif_EG:
            modalite_totale.append(l_orientation[i].effectif_EG)
            i+=1
        else:
            i+=1
    return modalite_totale

def recherche_dicho_quelconque(l_orientation, effectif_EG):
    """
    Rôle : Recherche un effectif_EG dans une liste triée (méthode dichotomique)
    Type des données :
        l_orientation : liste triée de type orientation
        effectif_EG : float (valeur recherchée)
    Résultat : int (indice ou -1 si absent)
    """
    g = 0
    d = len(l_orientation) -1
    indice = -1
    while g<=d and indice==-1 :
        m = (g+d)//2
        if l_orientation[m].effectif_EG == effectif_EG :
            indice=m
        elif  effectif_EG > l_orientation[m].effectif_EG:
            g = m+1
        else:
            d=m-1
    return indice

def recherche_dicho_plus_petit_indice(l_orientation, effectif_EG):
    """
    Rôle : Recherche l'indice du plus petit élément égal à effectif_EG
    Type des données :
        l_orientation : liste triée de type orientation
        effectif_EG : float
    Résultat : int (indice ou -1 si absent)
    """
    g = 0
    d = len(l_orientation) -1
    indice_min = -1
    while( g <= d) :
        m = (g+d)//2
        if l_orientation[m].effectif_EG == effectif_EG :
            indice_min = m
            d = m-1
        elif  effectif_EG < l_orientation[m].effectif_EG :
            d = m-1
        else:
            g = m+1
    return  indice_min

def recherche_dicho_plus_grand_indice(l_orientation, effectif_EG):
    """
    Rôle : Recherche l'indice du plus grand élément égal à effectif_EG
    Type des données :
        l_orientation : liste triée de type orientation
        effectif_EG : float
    Résultat : int (indice ou -1 si absent)
    """
    g = 0
    d = len(l_orientation) -1
    indice_max = -1
    while( g <= d) :
        m = (g+d)//2
        if l_orientation[m].effectif_EG == effectif_EG :
            indice_max = m
            g = m+1
        elif  effectif_EG < l_orientation[m].effectif_EG :
            d = m-1
        else:
            g = m+1
    return  indice_max

def nombres_occurrences(l_orientation, effectif_EG):
    """
    Rôle : Calcule le nombre d'occurrences d'une valeur effectif_EG
    Type des données :
        l_orientation : liste triée de type orientation
        effectif_EG : float
    Résultat : int (nombre d'occurrences)
    """
    indice_min = recherche_dicho_plus_petit_indice(l_orientation, effectif_EG)
    if indice_min == -1:
        return 0 
    indice_max = recherche_dicho_plus_grand_indice(l_orientation, effectif_EG)
    return indice_max - indice_min + 1

"""
Auteur:Ikdoumi Ilian
"""


from II_02_listes_orientation import*
from outils_csv import*


fichier = "Donnée/II_data_0.csv"
separateur = ","
encodage = "latin-1"
nb_lignes_entete = 1
print("Affichage du contenu du fichier "+ fichier + "\n--------")
data_0 = lecture_fichier_csv(fichier, separateur, encodage, nb_lignes_entete)
liste_orientations_0=[]
print(len(liste_orientations_0))
if len(liste_orientations_0)<18:
    print(data_0)








fichier = "Donnée/II_data_1.csv"
separateur = ","
encodage = "latin-1"
nb_lignes_entete = 1
data_1 = lecture_fichier_csv(fichier, separateur, encodage, nb_lignes_entete)
print("Affichage du contenu du fichier "+ fichier + "\n--------")
print(data_1)
liste_orientations_1=(liste_liste_to_orientation(data_1[1]))
print(len(liste_orientations_1))
if len(liste_orientations_1)<18:
    print(liste_orientations_1)





fichier = "Donnée/II_data_5.csv"
separateur = ","
encodage = "latin-1"
nb_lignes_entete = 1
data_5 = lecture_fichier_csv(fichier, separateur, encodage, nb_lignes_entete)
print("Affichage du contenu du fichier "+ fichier + "\n--------")
print(data_5)
liste_orientations_5=(liste_liste_to_orientation(data_5[1]))
print(len(liste_orientations_5))
if len(liste_orientations_5)<18:
    print(liste_orientations_5)





fichier = "Donnée/II_data_20.csv"
separateur = ","
encodage = "latin-1"
nb_lignes_entete = 1
data_20 = lecture_fichier_csv(fichier, separateur, encodage, nb_lignes_entete)
print("Affichage du contenu du fichier "+ fichier + "\n--------")
print(data_20)
liste_orientations_20=(liste_liste_to_orientation(data_20[1]))
print(len(liste_orientations_20))
if len(liste_orientations_20)<18:
    print(liste_orientations_20)






fichier = "Donnée/II_data_100.csv"
separateur = ","
encodage = "latin-1"
nb_lignes_entete = 1
data_100 = lecture_fichier_csv(fichier, separateur, encodage, nb_lignes_entete)
print("Affichage du contenu du fichier "+ fichier + "\n--------")
print(data_100)
liste_orientations_100=(liste_liste_to_orientation(data_100[1]))
print(len(liste_orientations_100))
if len(liste_orientations_100)<18:
    print(liste_orientations_100)



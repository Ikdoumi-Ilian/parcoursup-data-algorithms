"""
Auteur : Ikdoumi Ilian
"""


from II_02_listes_orientation import *
from outils_csv import*


liste_courante=[orientation(effectif_EG=549.0, region='Bordeaux', filiere='Philosophie'), orientation(effectif_EG=1.0, region='Nord', filiere='Faculté de Médecine'), orientation(effectif_EG=100.0, region='Toulouse', filiere=' Chimie - Parcours Cycle Ingénieur'), orientation(effectif_EG=7.0, region='Aix-Marseille', filiere='Cybersécurité'), orientation(effectif_EG=77.0, region='Nantes', filiere='Sciences et Techniques des Activités Physiques et Sportives')]


arret =False 
while arret ==False :

    print("voici la liste courante :\n",liste_courante)
    print("voici la liste des modalite des valeurs numeriques :\n",modalite_totale(triee_par_indice_min_orientation(liste_courante)))

    menu=("1-ouverture d'un fichier parmi une liste \n2-filtrage des données de la liste courante \n3- affichage d'indicateur statistique de la liste courante \n4-quitter")
    print(menu)
    choix=input("votre choix  : ")
    if choix=="4":
        arret = True
    if choix =="1":
        print("quel taille de fichier voulait vus choisir pour remplacer la liste courante ?")
        print("1-fichier avec 1 ligne de données \n2-fichier avec 5 ligne de données \n3-fichier avec 20 ligne de données \n4-fichier avec 100 ligne de données \n")
        choix_2=input("votre choix : ")
        if choix_2=="1":
            fichier = "Donnée/II_data_1.csv"
            separateur = ","
            encodage = "latin-1"
            nb_lignes_entete = 1
            data_1 = lecture_fichier_csv(fichier, separateur, encodage, nb_lignes_entete)
            liste_orientations_1=(liste_liste_to_orientation(data_1[1]))
            liste_courante=liste_orientations_1
        if choix_2=="2":
            fichier = "Donnée/II_data_5.csv"
            separateur = ","
            encodage = "latin-1"
            nb_lignes_entete = 1
            data_5 = lecture_fichier_csv(fichier, separateur, encodage, nb_lignes_entete)
            liste_orientations_5=liste_liste_to_orientation(data_5[1])
            liste_courante=liste_orientations_5
        if choix_2=="3":
            fichier = "Donnée/II_data_20.csv"
            separateur = ","
            encodage = "latin-1"
            nb_lignes_entete = 1
            data_20 = lecture_fichier_csv(fichier, separateur, encodage, nb_lignes_entete)
            liste_orientations_20=liste_liste_to_orientation(data_20[1])
            liste_courante=liste_orientations_20
        if choix_2=="4":
            fichier = "Donnée/II_data_100.csv"
            separateur = ","
            encodage = "latin-1"
            nb_lignes_entete = 1
            data_100 = lecture_fichier_csv(fichier, separateur, encodage, nb_lignes_entete)
            liste_orientations_100=liste_liste_to_orientation(data_100[1])
            liste_courante=liste_orientations_100
    if choix=="2":
        print("vous pouvez flitrer vos données soit par la region soit par la filiere que est votre choix ?")
        print("1-region \n2-filliere")
        choix_3=input("choix : ")
        if choix_3=="1":
            print("le filtrage va etre effectué ecrivez une region par exemple 'Bordeaux' PS:Atention au majuscule et aux fautes d'hortographe votre liste_courante sera donc filtré il n'y aura que les listes d'orientation avec comme region Bordeaux")
            choix_region=input("region : ")
            liste_courante=filtrage_orientation_region(liste_courante,choix_region)
        if choix_3=="2":
            print("le filtrage va etre effectué ecrivez une region par exemple 'Philosophie' PS:Atention au majuscule et aux fautes d'hortographe votre liste_courante sera donc filtré il n'y aura que les listes d'orientation qui à comme filiere Philosophie")
            choix_filiere=input("filiere : ")
            liste_courante=filtrage_orientation_filiere(liste_courante,choix_filiere)
    if choix=="3":
        print("quel est l'indicateur statistique des effectifs d'eleve de terminale générale que vous voulez affiché ?")
        print("1-Minimum\n2-Maximum\n3-Moyenne\n4-Ecart type\n5-Mediane\n6-nombre d’occurrences d'une valeur ")
        choix_4=input("choix :")
        if choix_4=="1":
            print(min_effectif_EG(liste_courante))
        if choix_4=="2":
            print(max_effectif_EG(liste_courante))
        if choix_4=="3":
            print(moyenne_effectif_EG(liste_courante))
        if choix_4 =="4":
            print(ecart_type_effectif_EG(liste_courante))
        if choix_4 =="5":
            print(mediane_triee_orientation(triee_par_indice_min_orientation(liste_courante)))
        if choix_4 =="6":
            valeur = int(input("valeur choisit pour voir le nombre d'occurence : "))
            print(nombres_occurrences(liste_courante, valeur))
            
            
        
        

    

        
        

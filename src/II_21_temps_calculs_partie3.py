"""
Auteur : Ikdoumi Ilian
"""
from outils_dessin import*
from II_02_listes_orientation import*
from outils_mesure import*
import timeit
from outils_csv import*

liste_orientations_1=(liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_1.csv", ",", "latin-1", 1)[1]))
liste_orientations_5=(liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_5.csv", ",", "latin-1", 1)[1]))
liste_orientations_20=(liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_20.csv", ",", "latin-1", 1)[1]))
liste_orientations_100=(liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_100.csv", ",", "latin-1", 1)[1]))
liste_orientations_14080=(liste_liste_to_orientation(lecture_fichier_csv("base_projet.csv", ",", "latin-1", 1)[1]))


nb_repet=10
instructions_initialistaion="""
from II_02_listes_orientation import liste_to_orientation
from II_02_listes_orientation import liste_liste_to_orientation
from II_02_listes_orientation import plus_petit_indice_min_orientation
from II_02_listes_orientation import triee_par_indice_min_orientation
from II_02_listes_orientation import recherche_dicho_quelconque
from II_02_listes_orientation import recherche_dicho_plus_petit_indice
from II_02_listes_orientation import recherche_dicho_plus_grand_indice
from II_02_listes_orientation import nombres_occurrences
from outils_csv import lecture_fichier_csv
liste_orientations_14080=triee_par_indice_min_orientation((liste_liste_to_orientation(lecture_fichier_csv("base_projet.csv", ",", "latin-1", 1)[1])))
liste_orientations_100=triee_par_indice_min_orientation((liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_100.csv", ",", "latin-1", 1)[1])))
liste_orientations_20=triee_par_indice_min_orientation((liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_20.csv", ",", "latin-1", 1)[1])))
liste_orientations_5=triee_par_indice_min_orientation((liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_5.csv", ",", "latin-1", 1)[1])))
liste_orientations_1=triee_par_indice_min_orientation((liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_1.csv", ",", "latin-1", 1)[1])))
"""





print("Afichage du temps d'execution de la fonction recherche_dicho_quelconque selon la taille de la liste :")
instructions_a_mesurer_14080_recherche_dicho_quelconque= """
recherche_dicho_quelconque_14080=recherche_dicho_quelconque(liste_orientations_14080,effectif_EG=77.0)
"""
temps_14080_recherche_dicho_quelconque = timeit.timeit(stmt=instructions_a_mesurer_14080_recherche_dicho_quelconque,setup=instructions_initialistaion,number=nb_repet)
temps_exec_14080_recherche_dicho_quelconque = temps_en_nanoseconde(temps_14080_recherche_dicho_quelconque/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_quelconque pour une liste d'orientation avec 14080 donnée: ",temps_exec_14080_recherche_dicho_quelconque ," nanoseconde")


instructions_a_mesurer_100_recherche_dicho_quelconque= """
recherche_dicho_quelconque_100=recherche_dicho_quelconque(liste_orientations_100,effectif_EG=77.0)
"""
temps_100_recherche_dicho_quelconque = timeit.timeit( stmt=instructions_a_mesurer_100_recherche_dicho_quelconque,setup=instructions_initialistaion,number=nb_repet )
temps_exec_100_recherche_dicho_quelconque = temps_en_nanoseconde(temps_100_recherche_dicho_quelconque/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_quelconque pour une liste d'orientation avec 100 donnée: ",temps_exec_100_recherche_dicho_quelconque ," nanoseconde")


instructions_a_mesurer_20_recherche_dicho_quelconque= """
recherche_dicho_quelconque_20=recherche_dicho_quelconque(liste_orientations_20,effectif_EG=77.0)
"""
temps_20_recherche_dicho_quelconque = timeit.timeit( stmt=instructions_a_mesurer_20_recherche_dicho_quelconque,setup=instructions_initialistaion,number=nb_repet )
temps_exec_20_recherche_dicho_quelconque= temps_en_nanoseconde(temps_20_recherche_dicho_quelconque/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_quelconque pour une liste d'orientation avec 20 donnée: ",temps_exec_20_recherche_dicho_quelconque," nanoseconde")


instructions_a_mesurer_5_recherche_dicho_quelconque="""
recherche_dicho_quelconque_5=recherche_dicho_quelconque(liste_orientations_5,effectif_EG=77.0)
"""
temps_5_recherche_dicho_quelconque= timeit.timeit( stmt=instructions_a_mesurer_5_recherche_dicho_quelconque,setup=instructions_initialistaion,number=nb_repet )
temps_exec_5_recherche_dicho_quelconque= temps_en_nanoseconde(temps_5_recherche_dicho_quelconque/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_quelconque pour une liste d'orientation avec 5 donnée: ",temps_exec_5_recherche_dicho_quelconque," nanoseconde")


instructions_a_mesurer_1_recherche_dicho_quelconque= """
recherche_dicho_quelconque_1=recherche_dicho_quelconque(liste_orientations_1,effectif_EG=77.0)
"""
temps_1_recherche_dicho_quelconque= timeit.timeit( stmt=instructions_a_mesurer_1_recherche_dicho_quelconque,setup=instructions_initialistaion,number=nb_repet )

temps_exec_1_recherche_dicho_quelconque= temps_en_nanoseconde(temps_1_recherche_dicho_quelconque/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_quelconque pour une liste d'orientation avec 1 donnée: ",temps_exec_1_recherche_dicho_quelconque," nanoseconde")





print("---------------------------------------------------------------------------")
print("Afichage du temps d'execution de la fonction recherche_dicho_plus_petit_indice selon la taille de la liste :")
instructions_a_mesurer_14080_recherche_dicho_plus_petit_indice= """
recherche_dicho_plus_petit_indice_14080=recherche_dicho_plus_petit_indice(liste_orientations_14080,effectif_EG=77.0)
"""
temps_14080_recherche_dicho_plus_petit_indice = timeit.timeit(stmt=instructions_a_mesurer_14080_recherche_dicho_plus_petit_indice,setup=instructions_initialistaion,number=nb_repet)
temps_exec_14080_recherche_dicho_plus_petit_indice = temps_en_nanoseconde(temps_14080_recherche_dicho_plus_petit_indice/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_plus_petit_indice pour une liste d'orientation avec 14080 donnée: ",temps_exec_14080_recherche_dicho_plus_petit_indice ," nanoseconde")


instructions_a_mesurer_100_recherche_dicho_plus_petit_indice= """
recherche_dicho_plus_petit_indice_100=recherche_dicho_plus_petit_indice(liste_orientations_100,effectif_EG=77.0)
"""
temps_100_recherche_dicho_plus_petit_indice = timeit.timeit( stmt=instructions_a_mesurer_100_recherche_dicho_plus_petit_indice,setup=instructions_initialistaion,number=nb_repet )
temps_exec_100_recherche_dicho_plus_petit_indice = temps_en_nanoseconde(temps_100_recherche_dicho_plus_petit_indice/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_plus_petit_indice pour une liste d'orientation avec 100 donnée: ",temps_exec_100_recherche_dicho_plus_petit_indice ," nanoseconde")


instructions_a_mesurer_20_recherche_dicho_plus_petit_indice= """
recherche_dicho_plus_petit_indice_20=recherche_dicho_plus_petit_indice(liste_orientations_20,effectif_EG=77.0)
"""
temps_20_recherche_dicho_plus_petit_indice = timeit.timeit( stmt=instructions_a_mesurer_20_recherche_dicho_plus_petit_indice,setup=instructions_initialistaion,number=nb_repet )
temps_exec_20_recherche_dicho_plus_petit_indice= temps_en_nanoseconde(temps_20_recherche_dicho_plus_petit_indice/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_plus_petit_indice pour une liste d'orientation avec 20 donnée: ",temps_exec_20_recherche_dicho_plus_petit_indice," nanoseconde")


instructions_a_mesurer_5_recherche_dicho_plus_petit_indice="""
recherche_dicho_plus_petit_indice_5=recherche_dicho_plus_petit_indice(liste_orientations_5,effectif_EG=77.0)
"""
temps_5_recherche_dicho_plus_petit_indice= timeit.timeit( stmt=instructions_a_mesurer_5_recherche_dicho_plus_petit_indice,setup=instructions_initialistaion,number=nb_repet )
temps_exec_5_recherche_dicho_plus_petit_indice= temps_en_nanoseconde(temps_5_recherche_dicho_plus_petit_indice/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_plus_petit_indice pour une liste d'orientation avec 5 donnée: ",temps_exec_5_recherche_dicho_plus_petit_indice," nanoseconde")


instructions_a_mesurer_1_recherche_dicho_plus_petit_indice= """
recherche_dicho_plus_petit_indice_1=recherche_dicho_plus_petit_indice(liste_orientations_1,effectif_EG=77.0)
"""
temps_1_recherche_dicho_plus_petit_indice= timeit.timeit( stmt=instructions_a_mesurer_1_recherche_dicho_plus_petit_indice,setup=instructions_initialistaion,number=nb_repet )

temps_exec_1_recherche_dicho_plus_petit_indice= temps_en_nanoseconde(temps_1_recherche_dicho_plus_petit_indice/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_plus_petit_indice pour une liste d'orientation avec 1 donnée: ",temps_exec_1_recherche_dicho_plus_petit_indice," nanoseconde")



print("la courbe rouge est pour la fonction recherche_dicho_quelconque et la bleu pour la fonction recherche_dicho_plus_petit_indice")


courbe1 = [(0, 0), (1,temps_exec_1_recherche_dicho_quelconque), (5, temps_exec_5_recherche_dicho_quelconque), (20, temps_exec_20_recherche_dicho_quelconque), (100, temps_exec_100_recherche_dicho_quelconque)]
courbe2 = [(0, 0), (1,temps_exec_1_recherche_dicho_plus_petit_indice), (5, temps_exec_5_recherche_dicho_plus_petit_indice), (20, temps_exec_20_recherche_dicho_plus_petit_indice), (100, temps_exec_100_recherche_dicho_plus_petit_indice)]
dessine_lignes_brisees(courbe1,courbe2)








print("---------------------------------------------------------------------------")
print("Afichage du temps d'execution de la fonction recherche_dicho_plus_grand_indice selon la taille de la liste :")
instructions_a_mesurer_14080_recherche_dicho_plus_grand_indice= """
recherche_dicho_plus_grand_indice_14080=recherche_dicho_plus_grand_indice(liste_orientations_14080,effectif_EG=77.0)
"""
temps_14080_recherche_dicho_plus_grand_indice = timeit.timeit(stmt=instructions_a_mesurer_14080_recherche_dicho_plus_grand_indice,setup=instructions_initialistaion,number=nb_repet)
temps_exec_14080_recherche_dicho_plus_grand_indice = temps_en_nanoseconde(temps_14080_recherche_dicho_plus_grand_indice/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_plus_grand_indice pour une liste d'orientation avec 14080 donnée: ",temps_exec_14080_recherche_dicho_plus_grand_indice ," nanoseconde")


instructions_a_mesurer_100_recherche_dicho_plus_grand_indice= """
recherche_dicho_plus_grand_indice_100=recherche_dicho_plus_grand_indice(liste_orientations_100,effectif_EG=77.0)
"""
temps_100_recherche_dicho_plus_grand_indice = timeit.timeit( stmt=instructions_a_mesurer_100_recherche_dicho_plus_grand_indice,setup=instructions_initialistaion,number=nb_repet )
temps_exec_100_recherche_dicho_plus_grand_indice = temps_en_nanoseconde(temps_100_recherche_dicho_plus_grand_indice/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_plus_grand_indice pour une liste d'orientation avec 100 donnée: ",temps_exec_100_recherche_dicho_plus_grand_indice ," nanoseconde")


instructions_a_mesurer_20_recherche_dicho_plus_grand_indice= """
recherche_dicho_plus_grand_indice_20=recherche_dicho_plus_grand_indice(liste_orientations_20,effectif_EG=77.0)
"""
temps_20_recherche_dicho_plus_grand_indice = timeit.timeit( stmt=instructions_a_mesurer_20_recherche_dicho_plus_grand_indice,setup=instructions_initialistaion,number=nb_repet )
temps_exec_20_recherche_dicho_plus_grand_indice= temps_en_nanoseconde(temps_20_recherche_dicho_plus_grand_indice/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_plus_grand_indice pour une liste d'orientation avec 20 donnée: ",temps_exec_20_recherche_dicho_plus_grand_indice," nanoseconde")


instructions_a_mesurer_5_recherche_dicho_plus_grand_indice="""
recherche_dicho_plus_grand_indice_5=recherche_dicho_plus_grand_indice(liste_orientations_5,effectif_EG=77.0)
"""
temps_5_recherche_dicho_plus_grand_indice= timeit.timeit( stmt=instructions_a_mesurer_5_recherche_dicho_plus_grand_indice,setup=instructions_initialistaion,number=nb_repet )
temps_exec_5_recherche_dicho_plus_grand_indice= temps_en_nanoseconde(temps_5_recherche_dicho_plus_grand_indice/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_plus_grand_indice pour une liste d'orientation avec 5 donnée: ",temps_exec_5_recherche_dicho_plus_grand_indice," nanoseconde")


instructions_a_mesurer_1_recherche_dicho_plus_grand_indice= """
recherche_dicho_plus_grand_indice_1=recherche_dicho_plus_grand_indice(liste_orientations_1,effectif_EG=77.0)
"""
temps_1_recherche_dicho_plus_grand_indice= timeit.timeit( stmt=instructions_a_mesurer_1_recherche_dicho_plus_grand_indice,setup=instructions_initialistaion,number=nb_repet )

temps_exec_1_recherche_dicho_plus_grand_indice= temps_en_nanoseconde(temps_1_recherche_dicho_plus_grand_indice/nb_repet)
print("voici le temps d'execution de la fonction recherche_dicho_plus_grand_indice pour une liste d'orientation avec 1 donnée: ",temps_exec_1_recherche_dicho_plus_grand_indice," nanoseconde")













print("---------------------------------------------------------------------------")
print("Afichage du temps d'execution de la fonction nombres_occurrences selon la taille de la liste :")
instructions_a_mesurer_14080_nombres_occurrences= """
nombres_occurrences14080=nombres_occurrences(liste_orientations_14080,effectif_EG=77.0)
"""
temps_14080_nombres_occurrences = timeit.timeit(stmt=instructions_a_mesurer_14080_nombres_occurrences,setup=instructions_initialistaion,number=nb_repet)
temps_exec_14080_nombres_occurrences = temps_en_nanoseconde(temps_14080_nombres_occurrences/nb_repet)
print("voici le temps d'execution de la fonction nombres_occurrences pour une liste d'orientation avec 14080 donnée: ",temps_exec_14080_nombres_occurrences ," nanoseconde")


instructions_a_mesurer_100_nombres_occurrences= """
nombres_occurrences_100=nombres_occurrences(liste_orientations_100,effectif_EG=77.0)
"""
temps_100_nombres_occurrences = timeit.timeit( stmt=instructions_a_mesurer_100_nombres_occurrences,setup=instructions_initialistaion,number=nb_repet )
temps_exec_100_nombres_occurrences = temps_en_nanoseconde(temps_100_nombres_occurrences/nb_repet)
print("voici le temps d'execution de la fonction nombres_occurrences pour une liste d'orientation avec 100 donnée: ",temps_exec_100_nombres_occurrences ," nanoseconde")


instructions_a_mesurer_20_nombres_occurrences= """
nombres_occurrences_20=nombres_occurrences(liste_orientations_20,effectif_EG=77.0)
"""
temps_20_nombres_occurrences = timeit.timeit( stmt=instructions_a_mesurer_20_nombres_occurrences,setup=instructions_initialistaion,number=nb_repet )
temps_exec_20_nombres_occurrences= temps_en_nanoseconde(temps_20_nombres_occurrences/nb_repet)
print("voici le temps d'execution de la fonction nombres_occurrences pour une liste d'orientation avec 20 donnée: ",temps_exec_20_nombres_occurrences," nanoseconde")


instructions_a_mesurer_5_nombres_occurrences="""
nombres_occurrences_5=nombres_occurrences(liste_orientations_5,effectif_EG=77.0)
"""
temps_5_nombres_occurrences= timeit.timeit( stmt=instructions_a_mesurer_5_nombres_occurrences,setup=instructions_initialistaion,number=nb_repet )
temps_exec_5_nombres_occurrences= temps_en_nanoseconde(temps_5_nombres_occurrences/nb_repet)
print("voici le temps d'execution de la fonction nombres_occurrences pour une liste d'orientation avec 5 donnée: ",temps_exec_5_nombres_occurrences," nanoseconde")


instructions_a_mesurer_1_nombres_occurrences= """
nombres_occurrences_1=nombres_occurrences(liste_orientations_1,effectif_EG=77.0)
"""
temps_1_nombres_occurrences= timeit.timeit( stmt=instructions_a_mesurer_1_nombres_occurrences,setup=instructions_initialistaion,number=nb_repet )

temps_exec_1_nombres_occurrences= temps_en_nanoseconde(temps_1_nombres_occurrences/nb_repet)
print("voici le temps d'execution de la fonction nombres_occurrences pour une liste d'orientation avec 1 donnée: ",temps_exec_1_nombres_occurrences," nanoseconde")



print("la courbe rouge est pour la fonction recherche_dicho_plus_grand_indice et la bleu pour la fonction nombres_occurrences")


courbe3 = [(0, 0), (1,temps_exec_1_recherche_dicho_plus_grand_indice), (5, temps_exec_5_recherche_dicho_plus_grand_indice), (20, temps_exec_20_recherche_dicho_plus_grand_indice), (100, temps_exec_100_recherche_dicho_plus_grand_indice)]
courbe4 = [(0, 0), (1,temps_exec_1_nombres_occurrences), (5, temps_exec_5_nombres_occurrences), (20, temps_exec_20_nombres_occurrences), (100, temps_exec_100_nombres_occurrences)]
dessine_lignes_brisees(courbe3,courbe4)

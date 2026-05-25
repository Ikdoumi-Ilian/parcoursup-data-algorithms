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
from II_02_listes_orientation import min_effectif_EG
from II_02_listes_orientation import max_effectif_EG
from II_02_listes_orientation import moyenne_effectif_EG
from II_02_listes_orientation import ecart_type_effectif_EG
from outils_csv import lecture_fichier_csv
liste_orientations_14080=(liste_liste_to_orientation(lecture_fichier_csv("base_projet.csv", ",", "latin-1", 1)[1]))
liste_orientations_100=(liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_100.csv", ",", "latin-1", 1)[1]))
liste_orientations_20=(liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_20.csv", ",", "latin-1", 1)[1]))
liste_orientations_5=(liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_5.csv", ",", "latin-1", 1)[1]))
liste_orientations_1=(liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_1.csv", ",", "latin-1", 1)[1]))
"""


print("Afichage du temps d'execution de la fonction minimum selon la taille de la liste :")
instructions_a_mesurer_14080_min= """
min_14080=min_effectif_EG(liste_orientations_14080)
"""
temps_14080_min = timeit.timeit(stmt=instructions_a_mesurer_14080_min,setup=instructions_initialistaion,number=nb_repet)
temps_exec_14080_min = temps_en_nanoseconde(temps_14080_min/nb_repet)
print("voici le temps d'execution de la fonction minimum pour une liste d'orientation avec 14080 donnée: ",temps_exec_14080_min ," nanoseconde")


instructions_a_mesurer_100_min= """
min_100=min_effectif_EG(liste_orientations_100)
"""
temps_100_min = timeit.timeit( stmt=instructions_a_mesurer_100_min,setup=instructions_initialistaion,number=nb_repet )
temps_exec_100_min = temps_en_nanoseconde(temps_100_min/nb_repet)
print("voici le temps d'execution de la fonction minimum pour une liste d'orientation avec 100 donnée: ",temps_exec_100_min ," nanoseconde")


instructions_a_mesurer_20_min= """
min_20=min_effectif_EG(liste_orientations_20)
"""
temps_20_min = timeit.timeit( stmt=instructions_a_mesurer_20_min,setup=instructions_initialistaion,number=nb_repet )
temps_exec_20_min= temps_en_nanoseconde(temps_20_min/nb_repet)
print("voici le temps d'execution de la fonction minimum pour une liste d'orientation avec 20 donnée: ",temps_exec_20_min," nanoseconde")


instructions_a_mesurer_5_min="""
min_5=min_effectif_EG(liste_orientations_5)
"""
temps_5_min= timeit.timeit( stmt=instructions_a_mesurer_5_min,setup=instructions_initialistaion,number=nb_repet )
temps_exec_5_min= temps_en_nanoseconde(temps_5_min/nb_repet)
print("voici le temps d'execution de la fonction minimum pour une liste d'orientation avec 5 donnée: ",temps_exec_5_min," nanoseconde")


instructions_a_mesurer_1_min= """
min_1=min_effectif_EG(liste_orientations_1)
"""
temps_1_min= timeit.timeit( stmt=instructions_a_mesurer_1_min,setup=instructions_initialistaion,number=nb_repet )

temps_exec_1_min= temps_en_nanoseconde(temps_1_min/nb_repet)
print("voici le temps d'execution de la fonction minimum pour une liste d'orientation avec 1 donnée: ",temps_exec_1_min," nanoseconde")


print("---------------------------------------------------------------------------")
print("Afichage du temps d'execution de la fonction maximum selon la taille de la liste :")
instructions_a_mesurer_14080_max= """
max_14080=max_effectif_EG(liste_orientations_14080)
"""
temps_14080_max = timeit.timeit(stmt=instructions_a_mesurer_14080_max,setup=instructions_initialistaion,number=nb_repet)
temps_exec_14080_max = temps_en_nanoseconde(temps_14080_max/nb_repet)
print("voici le temps d'execution de la fonction maximum pour une liste d'orientation avec 14080 donnée: ",temps_exec_14080_max ," nanoseconde")


instructions_a_mesurer_100_max= """
max_100=max_effectif_EG(liste_orientations_100)
"""
temps_100_max = timeit.timeit( stmt=instructions_a_mesurer_100_max,setup=instructions_initialistaion,number=nb_repet )
temps_exec_100_max = temps_en_nanoseconde(temps_100_max/nb_repet)
print("voici le temps d'execution de la fonction maximum pour une liste d'orientation avec 100 donnée: ",temps_exec_100_max ,"nanoseconde")


instructions_a_mesurer_20_max= """
max_20=max_effectif_EG(liste_orientations_20)
"""
temps_20_max = timeit.timeit( stmt=instructions_a_mesurer_20_max,setup=instructions_initialistaion,number=nb_repet )
temps_exec_20_max= temps_en_nanoseconde(temps_20_max/nb_repet)
print("voici le temps d'execution de la fonction maximum pour une liste d'orientation avec 20 donnée: ",temps_exec_20_max," nanoseconde")


instructions_a_mesurer_5_max="""
max_5=max_effectif_EG(liste_orientations_5)
"""
temps_5_max= timeit.timeit( stmt=instructions_a_mesurer_5_max,setup=instructions_initialistaion,number=nb_repet )
temps_exec_5_max= temps_en_nanoseconde(temps_5_max/nb_repet)
print("voici le temps d'execution de la fonction maximum pour une liste d'orientation avec 5 donnée: ",temps_exec_5_max," nanoseconde")


instructions_a_mesurer_1_max= """
max_1=max_effectif_EG(liste_orientations_1)
"""
temps_1_max= timeit.timeit( stmt=instructions_a_mesurer_1_max,setup=instructions_initialistaion,number=nb_repet )

temps_exec_1_max= temps_en_nanoseconde(temps_1_max/nb_repet)
print("voici le temps d'execution de la fonction maximum pour une liste d'orientation avec 1 donnée: ",temps_exec_1_max," nanoseconde")
print("la courbe rouge est pour la fonction moyenne et la bleu pour la fonction ecart type")

courbe1 = [(0, 0), (1,temps_exec_1_min), (5, temps_exec_5_min), (20, temps_exec_20_min), (100, temps_exec_100_min)]
courbe2 = [(0, 0), (1,temps_exec_1_max), (5, temps_exec_5_max), (20, temps_exec_20_max), (100, temps_exec_100_max)]
dessine_lignes_brisees(courbe1,courbe2)

print("---------------------------------------------------------------------------")
print("Afichage du temps d'execution de la fonction moyenne selon la taille de la liste :")

instructions_a_mesurer_14080_moy= """
moy_14080=moyenne_effectif_EG(liste_orientations_14080)
"""
temps_14080_moy = timeit.timeit(stmt=instructions_a_mesurer_14080_moy,setup=instructions_initialistaion,number=nb_repet)
temps_exec_14080_moy = temps_en_nanoseconde(temps_14080_moy/nb_repet)
print("voici le temps d'execution de la fonction moyenne pour une liste d'orientation avec 14080 donnée: ",temps_exec_14080_moy ," nanoseconde")


instructions_a_mesurer_100_moy= """
moy_100=moyenne_effectif_EG(liste_orientations_100)
"""
temps_100_moy = timeit.timeit( stmt=instructions_a_mesurer_100_moy,setup=instructions_initialistaion,number=nb_repet )
temps_exec_100_moy = temps_en_nanoseconde(temps_100_moy/nb_repet)
print("voici le temps d'execution de la fonction moyenne pour une liste d'orientation avec 100 donnée: ",temps_exec_100_moy ,"nanoseconde")


instructions_a_mesurer_20_moy= """
moy_20=moyenne_effectif_EG(liste_orientations_20)
"""
temps_20_moy = timeit.timeit( stmt=instructions_a_mesurer_20_moy,setup=instructions_initialistaion,number=nb_repet )
temps_exec_20_moy= temps_en_nanoseconde(temps_20_moy/nb_repet)
print("voici le temps d'execution de la fonction maximum pour une liste d'orientation avec 20 donnée: ",temps_exec_20_moy," nanoseconde")


instructions_a_mesurer_5_moy="""
moy_5=moyenne_effectif_EG(liste_orientations_5)
"""
temps_5_moy= timeit.timeit( stmt=instructions_a_mesurer_5_moy,setup=instructions_initialistaion,number=nb_repet )
temps_exec_5_moy= temps_en_nanoseconde(temps_5_moy/nb_repet)
print("voici le temps d'execution de la fonction moyenne pour une liste d'orientation avec 5 donnée: ",temps_exec_5_moy," nanoseconde")


instructions_a_mesurer_1_moy= """
moy_1=moyenne_effectif_EG(liste_orientations_1)
"""
temps_1_moy= timeit.timeit( stmt=instructions_a_mesurer_1_moy,setup=instructions_initialistaion,number=nb_repet )

temps_exec_1_moy= temps_en_nanoseconde(temps_1_moy/nb_repet)
print("voici le temps d'execution de la fonction moyenne pour une liste d'orientation avec 1 donnée: ",temps_exec_1_moy," nanoseconde")



print("---------------------------------------------------------------------------")
print("Afichage du temps d'execution de la fonction ecart type selon la taille de la liste :")

instructions_a_mesurer_14080_et= """
et_14080=ecart_type_effectif_EG(liste_orientations_14080)
"""
temps_14080_et = timeit.timeit(stmt=instructions_a_mesurer_14080_et,setup=instructions_initialistaion,number=nb_repet)
temps_exec_14080_et = temps_en_nanoseconde(temps_14080_et/nb_repet)
print("voici le temps d'execution de la fonction ecart type pour une liste d'orientation avec 14080 donnée: ",temps_exec_14080_et ," nanoseconde")


instructions_a_mesurer_100_et= """
et_100=ecart_type_effectif_EG(liste_orientations_100)
"""
temps_100_et = timeit.timeit( stmt=instructions_a_mesurer_100_et,setup=instructions_initialistaion,number=nb_repet )
temps_exec_100_et = temps_en_nanoseconde(temps_100_et/nb_repet)
print("voici le temps d'execution de la fonction ecart type pour une liste d'orientation avec 100 donnée: ",temps_exec_100_et ,"nanoseconde")


instructions_a_mesurer_20_et= """
et_20=ecart_type_effectif_EG(liste_orientations_20)
"""
temps_20_et = timeit.timeit( stmt=instructions_a_mesurer_20_et,setup=instructions_initialistaion,number=nb_repet )
temps_exec_20_et= temps_en_nanoseconde(temps_20_et/nb_repet)
print("voici le temps d'execution de la fonction ecart type pour une liste d'orientation avec 20 donnée: ",temps_exec_20_et," nanoseconde")


instructions_a_mesurer_5_et="""
et_5=ecart_type_effectif_EG(liste_orientations_5)
"""
temps_5_et= timeit.timeit( stmt=instructions_a_mesurer_5_et,setup=instructions_initialistaion,number=nb_repet )
temps_exec_5_et= temps_en_nanoseconde(temps_5_et/nb_repet)
print("voici le temps d'execution de la fonction ecart type pour une liste d'orientation avec 5 donnée: ",temps_exec_5_et," nanoseconde")


instructions_a_mesurer_1_et= """
et_1=ecart_type_effectif_EG(liste_orientations_1)
"""
temps_1_et= timeit.timeit( stmt=instructions_a_mesurer_1_et,setup=instructions_initialistaion,number=nb_repet )

temps_exec_1_et= temps_en_nanoseconde(temps_1_et/nb_repet)
print("voici le temps d'execution de la fonction ecart type pour une liste d'orientation avec 1 donnée: ",temps_exec_1_et," nanoseconde")



print("la courbe rouge est pour la fonction moyenne et la bleu pour la fonction ecart type")


courbe3 = [(0, 0), (1,temps_exec_1_moy), (5, temps_exec_5_moy), (20, temps_exec_20_moy), (100, temps_exec_100_moy)]
courbe4 = [(0, 0), (1,temps_exec_1_et), (5, temps_exec_5_et), (20, temps_exec_20_et), (100, temps_exec_100_et)]
dessine_lignes_brisees(courbe3,courbe4)





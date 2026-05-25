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
from II_02_listes_orientation import mediane_triee_orientation
from II_02_listes_orientation import modalite_totale
from II_02_listes_orientation import plus_petit_indice_min_orientation
from II_02_listes_orientation import triee_par_indice_min_orientation
from II_02_listes_orientation import orientation_est_triee
from outils_csv import lecture_fichier_csv
liste_orientations_14080=triee_par_indice_min_orientation((liste_liste_to_orientation(lecture_fichier_csv("base_projet.csv", ",", "latin-1", 1)[1])))
liste_orientations_100=triee_par_indice_min_orientation((liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_100.csv", ",", "latin-1", 1)[1])))
liste_orientations_20=triee_par_indice_min_orientation((liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_20.csv", ",", "latin-1", 1)[1])))
liste_orientations_5=triee_par_indice_min_orientation((liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_5.csv", ",", "latin-1", 1)[1])))
liste_orientations_1=triee_par_indice_min_orientation((liste_liste_to_orientation(lecture_fichier_csv("Donnée/II_data_1.csv", ",", "latin-1", 1)[1])))
"""





print("Afichage du temps d'execution de la fonction est triee selon la taille de la liste :")
instructions_a_mesurer_14080_est_triee= """
est_triee_14080=orientation_est_triee(liste_orientations_14080)
"""
temps_14080_est_triee = timeit.timeit(stmt=instructions_a_mesurer_14080_est_triee,setup=instructions_initialistaion,number=nb_repet)
temps_exec_14080_est_triee = temps_en_nanoseconde(temps_14080_est_triee/nb_repet)
print("voici le temps d'execution de la fonction est_triee pour une liste d'orientation avec 14080 donnée: ",temps_exec_14080_est_triee ," nanoseconde")


instructions_a_mesurer_100_est_triee= """
est_triee_100=orientation_est_triee(liste_orientations_100)
"""
temps_100_est_triee = timeit.timeit( stmt=instructions_a_mesurer_100_est_triee,setup=instructions_initialistaion,number=nb_repet )
temps_exec_100_est_triee = temps_en_nanoseconde(temps_100_est_triee/nb_repet)
print("voici le temps d'execution de la fonction est_triee pour une liste d'orientation avec 100 donnée: ",temps_exec_100_est_triee ," nanoseconde")


instructions_a_mesurer_20_est_triee= """
est_triee_20=orientation_est_triee(liste_orientations_20)
"""
temps_20_est_triee = timeit.timeit( stmt=instructions_a_mesurer_20_est_triee,setup=instructions_initialistaion,number=nb_repet )
temps_exec_20_est_triee= temps_en_nanoseconde(temps_20_est_triee/nb_repet)
print("voici le temps d'execution de la fonction est_triee pour une liste d'orientation avec 20 donnée: ",temps_exec_20_est_triee," nanoseconde")


instructions_a_mesurer_5_est_triee="""
est_triee_5=orientation_est_triee(liste_orientations_5)
"""
temps_5_est_triee= timeit.timeit( stmt=instructions_a_mesurer_5_est_triee,setup=instructions_initialistaion,number=nb_repet )
temps_exec_5_est_triee= temps_en_nanoseconde(temps_5_est_triee/nb_repet)
print("voici le temps d'execution de la fonction est_triee pour une liste d'orientation avec 5 donnée: ",temps_exec_5_est_triee," nanoseconde")


instructions_a_mesurer_1_est_triee= """
est_triee_1=orientation_est_triee(liste_orientations_1)
"""
temps_1_est_triee= timeit.timeit( stmt=instructions_a_mesurer_1_est_triee,setup=instructions_initialistaion,number=nb_repet )

temps_exec_1_est_triee= temps_en_nanoseconde(temps_1_est_triee/nb_repet)
print("voici le temps d'execution de la fonction est_triee pour une liste d'orientation avec 1 donnée: ",temps_exec_1_est_triee," nanoseconde")





print("---------------------------------------------------------------------------")
print("Afichage du temps d'execution de la fonction triee_par_indice_min selon la taille de la liste :")
instructions_a_mesurer_14080_triee_par_indice_min= """
triee_par_indice_min_14080=triee_par_indice_min_orientation(liste_orientations_14080)
"""
temps_14080_triee_par_indice_min = timeit.timeit(stmt=instructions_a_mesurer_14080_triee_par_indice_min,setup=instructions_initialistaion,number=nb_repet)
temps_exec_14080_triee_par_indice_min = temps_en_nanoseconde(temps_14080_triee_par_indice_min/nb_repet)
print("voici le temps d'execution de la fonction triee_par_indice_min pour une liste d'orientation avec 14080 donnée: ",temps_exec_14080_triee_par_indice_min ," nanoseconde")


instructions_a_mesurer_100_triee_par_indice_min= """
triee_par_indice_min_100=triee_par_indice_min_orientation(liste_orientations_100)
"""
temps_100_triee_par_indice_min = timeit.timeit( stmt=instructions_a_mesurer_100_triee_par_indice_min,setup=instructions_initialistaion,number=nb_repet )
temps_exec_100_triee_par_indice_min = temps_en_nanoseconde(temps_100_triee_par_indice_min/nb_repet)
print("voici le temps d'execution de la fonction triee_par_indice_min pour une liste d'orientation avec 100 donnée: ",temps_exec_100_triee_par_indice_min ," nanoseconde")


instructions_a_mesurer_20_triee_par_indice_min= """
triee_par_indice_min_20=triee_par_indice_min_orientation(liste_orientations_20)
"""
temps_20_triee_par_indice_min = timeit.timeit( stmt=instructions_a_mesurer_20_triee_par_indice_min,setup=instructions_initialistaion,number=nb_repet )
temps_exec_20_triee_par_indice_min= temps_en_nanoseconde(temps_20_triee_par_indice_min/nb_repet)
print("voici le temps d'execution de la fonction triee_par_indice_min pour une liste d'orientation avec 20 donnée: ",temps_exec_20_triee_par_indice_min," nanoseconde")


instructions_a_mesurer_5_triee_par_indice_min="""
triee_par_indice_min_5=triee_par_indice_min_orientation(liste_orientations_5)
"""
temps_5_triee_par_indice_min= timeit.timeit( stmt=instructions_a_mesurer_5_triee_par_indice_min,setup=instructions_initialistaion,number=nb_repet )
temps_exec_5_triee_par_indice_min= temps_en_nanoseconde(temps_5_triee_par_indice_min/nb_repet)
print("voici le temps d'execution de la fonction triee_par_indice_min pour une liste d'orientation avec 5 donnée: ",temps_exec_5_triee_par_indice_min," nanoseconde")


instructions_a_mesurer_1_triee_par_indice_min= """
triee_par_indice_min_1=triee_par_indice_min_orientation(liste_orientations_1)
"""
temps_1_triee_par_indice_min= timeit.timeit( stmt=instructions_a_mesurer_1_triee_par_indice_min,setup=instructions_initialistaion,number=nb_repet )

temps_exec_1_triee_par_indice_min= temps_en_nanoseconde(temps_1_triee_par_indice_min/nb_repet)
print("voici le temps d'execution de la fonction triee_par_indice_min pour une liste d'orientation avec 1 donnée: ",temps_exec_1_triee_par_indice_min," nanoseconde")



print("la courbe rouge est pour la fonction est_triee et la bleu pour la fonction triee_par_indice_min")


courbe1 = [(0, 0), (1,temps_exec_1_est_triee), (5, temps_exec_5_est_triee), (20, temps_exec_20_est_triee), (100, temps_exec_100_est_triee)]
courbe2 = [(0, 0), (1,temps_exec_1_triee_par_indice_min), (5, temps_exec_5_triee_par_indice_min), (20, temps_exec_20_triee_par_indice_min), (100, temps_exec_100_triee_par_indice_min)]
dessine_lignes_brisees(courbe1,courbe2)








print("---------------------------------------------------------------------------")
print("Afichage du temps d'execution de la fonction mediane selon la taille de la liste :")
instructions_a_mesurer_14080_med= """
med_14080=mediane_triee_orientation(liste_orientations_14080)
"""
temps_14080_med = timeit.timeit(stmt=instructions_a_mesurer_14080_med,setup=instructions_initialistaion,number=nb_repet)
temps_exec_14080_med = temps_en_nanoseconde(temps_14080_med/nb_repet)
print("voici le temps d'execution de la fonction mediane pour une liste d'orientation avec 14080 donnée: ",temps_exec_14080_med ," nanoseconde")


instructions_a_mesurer_100_med= """
med_100=mediane_triee_orientation(liste_orientations_100)
"""
temps_100_med = timeit.timeit( stmt=instructions_a_mesurer_100_med,setup=instructions_initialistaion,number=nb_repet )
temps_exec_100_med = temps_en_nanoseconde(temps_100_med/nb_repet)
print("voici le temps d'execution de la fonction mediane pour une liste d'orientation avec 100 donnée: ",temps_exec_100_med ," nanoseconde")


instructions_a_mesurer_20_med= """
med_20=mediane_triee_orientation(liste_orientations_20)
"""
temps_20_med = timeit.timeit( stmt=instructions_a_mesurer_20_med,setup=instructions_initialistaion,number=nb_repet )
temps_exec_20_med= temps_en_nanoseconde(temps_20_med/nb_repet)
print("voici le temps d'execution de la fonction mediane pour une liste d'orientation avec 20 donnée: ",temps_exec_20_med," nanoseconde")


instructions_a_mesurer_5_med="""
med_5=mediane_triee_orientation(liste_orientations_5)
"""
temps_5_med= timeit.timeit( stmt=instructions_a_mesurer_5_med,setup=instructions_initialistaion,number=nb_repet )
temps_exec_5_med= temps_en_nanoseconde(temps_5_med/nb_repet)
print("voici le temps d'execution de la fonction mediane pour une liste d'orientation avec 5 donnée: ",temps_exec_5_med," nanoseconde")


instructions_a_mesurer_1_med= """
med_1=mediane_triee_orientation(liste_orientations_1)
"""
temps_1_med= timeit.timeit( stmt=instructions_a_mesurer_1_med,setup=instructions_initialistaion,number=nb_repet )

temps_exec_1_med= temps_en_nanoseconde(temps_1_med/nb_repet)
print("voici le temps d'execution de la fonction mediane pour une liste d'orientation avec 1 donnée: ",temps_exec_1_med," nanoseconde")













print("---------------------------------------------------------------------------")
print("Afichage du temps d'execution de la fonction modalite_totale selon la taille de la liste :")
instructions_a_mesurer_14080_modalite_totale= """
modalite_totale_14080=modalite_totale(liste_orientations_14080)
"""
temps_14080_modalite_totale = timeit.timeit(stmt=instructions_a_mesurer_14080_modalite_totale,setup=instructions_initialistaion,number=nb_repet)
temps_exec_14080_modalite_totale = temps_en_nanoseconde(temps_14080_modalite_totale/nb_repet)
print("voici le temps d'execution de la fonction modalite_totale pour une liste d'orientation avec 14080 donnée: ",temps_exec_14080_modalite_totale ," nanoseconde")


instructions_a_mesurer_100_modalite_totale= """
modalite_totale_100=modalite_totale(liste_orientations_100)
"""
temps_100_modalite_totale = timeit.timeit( stmt=instructions_a_mesurer_100_modalite_totale,setup=instructions_initialistaion,number=nb_repet )
temps_exec_100_modalite_totale = temps_en_nanoseconde(temps_100_modalite_totale/nb_repet)
print("voici le temps d'execution de la fonction modalite_totale pour une liste d'orientation avec 100 donnée: ",temps_exec_100_modalite_totale ," nanoseconde")


instructions_a_mesurer_20_modalite_totale= """
modalite_totale_20=modalite_totale(liste_orientations_20)
"""
temps_20_modalite_totale = timeit.timeit( stmt=instructions_a_mesurer_20_modalite_totale,setup=instructions_initialistaion,number=nb_repet )
temps_exec_20_modalite_totale= temps_en_nanoseconde(temps_20_modalite_totale/nb_repet)
print("voici le temps d'execution de la fonction modalite_totale pour une liste d'orientation avec 20 donnée: ",temps_exec_20_modalite_totale," nanoseconde")


instructions_a_mesurer_5_modalite_totale="""
modalite_totale_5=modalite_totale(liste_orientations_5)
"""
temps_5_modalite_totale= timeit.timeit( stmt=instructions_a_mesurer_5_modalite_totale,setup=instructions_initialistaion,number=nb_repet )
temps_exec_5_modalite_totale= temps_en_nanoseconde(temps_5_modalite_totale/nb_repet)
print("voici le temps d'execution de la fonction modalite_totale pour une liste d'orientation avec 5 donnée: ",temps_exec_5_modalite_totale," nanoseconde")


instructions_a_mesurer_1_modalite_totale= """
modalite_totale_1=modalite_totale(liste_orientations_1)
"""
temps_1_modalite_totale= timeit.timeit( stmt=instructions_a_mesurer_1_modalite_totale,setup=instructions_initialistaion,number=nb_repet )

temps_exec_1_modalite_totale= temps_en_nanoseconde(temps_1_modalite_totale/nb_repet)
print("voici le temps d'execution de la fonction modalite_totale pour une liste d'orientation avec 1 donnée: ",temps_exec_1_modalite_totale," nanoseconde")



print("la courbe rouge est pour la fonction mediane et la bleu pour la fonction  modalite_totale")


courbe3 = [(0, 0), (1,temps_exec_1_med), (5, temps_exec_5_med), (20, temps_exec_20_med), (100, temps_exec_100_med)]
courbe4 = [(0, 0), (1,temps_exec_1_modalite_totale), (5, temps_exec_5_modalite_totale), (20, temps_exec_20_modalite_totale), (100, temps_exec_100_modalite_totale)]
dessine_lignes_brisees(courbe3,courbe4)

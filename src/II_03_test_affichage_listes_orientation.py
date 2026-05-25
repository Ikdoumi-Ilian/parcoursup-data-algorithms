"""
Auteur : Ikdoumi Ilian
"""


from II_02_listes_orientation import*

lis_orientation_test1=[orientation(effectif_EG=549.0, region='Bordeaux', filiere='Philosophie'), orientation(effectif_EG=1.0, region='Nord', filiere='Faculté de Médecine'), orientation(effectif_EG=100.0, region='Toulouse', filiere=' Chimie - Parcours Cycle Ingénieur'), orientation(effectif_EG=7.0, region='Aix-Marseille', filiere='Cybersécurité'), orientation(effectif_EG=77.0, region='Nantes', filiere='Sciences et Techniques des Activités Physiques et Sportives')]
lis_orientation_test2=[orientation(effectif_EG=549.0, region='Bordeaux', filiere='Philosophie'), orientation(effectif_EG=1.0, region='Nord', filiere='Faculté de Médecine'), orientation(effectif_EG=100.0, region='Toulouse', filiere=' Chimie - Parcours Cycle Ingénieur')]
lis_orientation_test3=[orientation(effectif_EG=549.0, region='Bordeaux', filiere='Philosophie')]



print("affichage de la premiere liste de test avec 5 differentes données de class orientation :\n")  # Résultat attendu à préciser
affiche_liste_orientation(lis_orientation_test1)

print("affichage de la deuxieme liste de test avec 3 differentes données de class orientation :\n ")  # Résultat attendu à préciser
affiche_liste_orientation(lis_orientation_test2)


print("affichage de la troisieme liste de test avec 1 donnée de class orientation :\n")  # Résultat attendu à préciser
affiche_liste_orientation(lis_orientation_test3)







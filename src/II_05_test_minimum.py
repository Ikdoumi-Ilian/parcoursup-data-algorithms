"""
Auteur: Ikdoumi Ilian
"""


from II_02_listes_orientation import*
lis_orientation_test_min_1=[orientation(effectif_EG=549.0, region='Bordeaux', filiere='Philosophie'), orientation(effectif_EG=1.0, region='Nord', filiere='Faculté de Médecine'), orientation(effectif_EG=100.0, region='Toulouse', filiere=' Chimie - Parcours Cycle Ingénieur'), orientation(effectif_EG=7.0, region='Aix-Marseille', filiere='Cybersécurité'), orientation(effectif_EG=77.0, region='Nantes', filiere='Sciences et Techniques des Activités Physiques et Sportives')]
lis_orientation_test_min_2=[orientation(effectif_EG=549.0, region='Bordeaux', filiere='Philosophie'), orientation(effectif_EG=1.0, region='Nord', filiere='Faculté de Médecine'), orientation(effectif_EG=100.0, region='Toulouse', filiere=' Chimie - Parcours Cycle Ingénieur')]
lis_orientation_test_min_3=[orientation(effectif_EG=549.0, region='Bordeaux', filiere='Philosophie')]

print("calcul du minimum de la premiere liste de test avec 5 differentes données de class orientation :\n")  
print(min_effectif_EG(lis_orientation_test_min_1))  # Résultat attendu 1.0


print("calcul du minimum de la deuxieme liste de test avec 3 differentes données de class orientation :\n ")  
print(min_effectif_EG(lis_orientation_test_min_2))  # Résultat attendu 1.0


print("calcul du minimum de la troisieme liste de test avec 1 donnée de class orientation :\n")  
print(min_effectif_EG(lis_orientation_test_min_3))  # Résultat attendu 1.0

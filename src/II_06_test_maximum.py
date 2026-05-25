"""
Auteur : Ikdoumi Ilian
"""


from II_02_listes_orientation import*



lis_orientation_test_max_1=[orientation(effectif_EG=549.0, region='Bordeaux', filiere='Philosophie'), orientation(effectif_EG=1.0, region='Nord', filiere='Faculté de Médecine'), orientation(effectif_EG=100.0, region='Toulouse', filiere=' Chimie - Parcours Cycle Ingénieur'), orientation(effectif_EG=7.0, region='Aix-Marseille', filiere='Cybersécurité'), orientation(effectif_EG=77.0, region='Nantes', filiere='Sciences et Techniques des Activités Physiques et Sportives')]
lis_orientation_test_max_2=[orientation(effectif_EG=50.0, region='Bordeaux', filiere='Philosophie'), orientation(effectif_EG=1.0, region='Nord', filiere='Faculté de Médecine'), orientation(effectif_EG=100.0, region='Toulouse', filiere=' Chimie - Parcours Cycle Ingénieur')]
lis_orientation_test_max_3=[orientation(effectif_EG=5.0, region='Bordeaux', filiere='Philosophie')]

print("calcul du maximum de la premiere liste de test avec 5 differentes données de class orientation :\n")  
print(max_effectif_EG(lis_orientation_test_max_1))  # Résultat attendu 549


print("calcul du maximum de la deuxieme liste de test avec 3 differentes données de class orientation :\n ")  
print(max_effectif_EG(lis_orientation_test_max_2))  # Résultat attendu 100


print("calcul du maximum de la troisieme liste de test avec 1 donnée de class orientation :\n")  
print(max_effectif_EG(lis_orientation_test_max_3))  # Résultat attendu 5.0

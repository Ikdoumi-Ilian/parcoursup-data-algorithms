"""
Auteur : Ikdoumi Ilian
"""
from II_02_listes_orientation import*
lis_orientation_test1=[orientation(effectif_EG=1.0, region='Bordeaux', filiere='Philosophie'),
                       orientation(effectif_EG=1.0, region='Nord', filiere='Faculté de Médecine'),
                       orientation(effectif_EG=77.0, region='Toulouse', filiere=' Chimie - Parcours Cycle Ingénieur'),
                       orientation(effectif_EG=77.0, region='Aix-Marseille', filiere='Cybersécurité'),
                       orientation(effectif_EG=97.0, region='Nantes', filiere='Sciences et Techniques des Activités Physiques et Sportives')]

lis_orientation_test1_triee=triee_par_indice_min_orientation(lis_orientation_test1)


print(recherche_dicho_plus_petit_indice(lis_orientation_test1_triee , effectif_EG=77.0))  # Résultat attendu 2
print(recherche_dicho_plus_petit_indice(lis_orientation_test1_triee , effectif_EG=1.0))  # Résultat attendu 0
print(recherche_dicho_plus_petit_indice(lis_orientation_test1_triee , effectif_EG=97.0))  # Résultat attendu 4
print(recherche_dicho_plus_petit_indice(lis_orientation_test1_triee , effectif_EG=7.0))  # Résultat attendu -1




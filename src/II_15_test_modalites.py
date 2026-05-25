"""
Auteur : Ikdoumi Ilian
"""
from II_02_listes_orientation import*




lis_orientation_test1=[orientation(effectif_EG=549.0, region='Bordeaux', filiere='Philosophie'), orientation(effectif_EG=1.0, region='Nord', filiere='Faculté de Médecine'), orientation(effectif_EG=100.0, region='Toulouse', filiere=' Chimie - Parcours Cycle Ingénieur'), orientation(effectif_EG=7.0, region='Aix-Marseille', filiere='Cybersécurité')]
lis_orientation_test2=[orientation(effectif_EG=1.0, region='Nord', filiere='Faculté de Médecine'), orientation(effectif_EG=1.0, region='Toulouse', filiere=' Chimie - Parcours Cycle Ingénieur'),orientation(effectif_EG=1.0, region='Aix-Marseille', filiere='Cybersécurité')]



print(modalite_totale(lis_orientation_test1))  # Résultat attendu [549.0, 1.0, 100.0, 7.0]
print(modalite_totale(lis_orientation_test2))  # Résultat attendu [1.0]

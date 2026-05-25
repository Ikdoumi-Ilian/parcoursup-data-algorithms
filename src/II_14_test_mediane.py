"""
Auteur : Ikdoumi Ilian
"""
from II_02_listes_orientation import*




lis_orientation_test1=[orientation(effectif_EG=549.0, region='Bordeaux', filiere='Philosophie'), orientation(effectif_EG=1.0, region='Nord', filiere='Faculté de Médecine'), orientation(effectif_EG=9.0, region='Toulouse', filiere=' Chimie - Parcours Cycle Ingénieur'), orientation(effectif_EG=7.0, region='Aix-Marseille', filiere='Cybersécurité')]
lis_orientation_test2=[orientation(effectif_EG=1.0, region='Nord', filiere='Faculté de Médecine'), orientation(effectif_EG=100.0, region='Toulouse', filiere=' Chimie - Parcours Cycle Ingénieur'),orientation(effectif_EG=7.0, region='Aix-Marseille', filiere='Cybersécurité')]

lis_orientation_test1_trie=triee_par_indice_min_orientation(lis_orientation_test1)
lis_orientation_test2_trie=triee_par_indice_min_orientation(lis_orientation_test2)
print("voici les deux listes triee : ") 
print(lis_orientation_test1_trie)  
print(lis_orientation_test2_trie)  

print("calcul des deux medianes : ")  
print(mediane_triee_orientation(lis_orientation_test1_trie))  # Résultat attendu 8
print(mediane_triee_orientation(lis_orientation_test2_trie))  # Résultat attendu 7

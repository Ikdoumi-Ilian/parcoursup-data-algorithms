"""
Auteur:Ikdoumi Ilian
"""
from II_02_listes_orientation import*


lis_orientation=[orientation(effectif_EG=549.0, region='Bordeaux', filiere='Philosophie'),orientation(effectif_EG=549.0, region='Bordeaux', filiere='Philosophie'), orientation(effectif_EG=1.0, region='Nord', filiere='Faculté de Médecine'), orientation(effectif_EG=100.0, region='Toulouse', filiere=' Chimie - Parcours Cycle Ingénieur'), orientation(effectif_EG=7.0, region='Aix-Marseille', filiere='Cybersécurité'), orientation(effectif_EG=77.0, region='Nantes', filiere='Sciences et Techniques des Activités Physiques et Sportives')]


print("test de filtrage par region :\n")  
print("filtrage par la region Nord :\n")  
print(filtrage_orientation_region(lis_orientation,"Nord"))  
print("--------------------------------------------------------------------------\n")  
print("filtrage par la region Bordeaux :\n")  
print(filtrage_orientation_region(lis_orientation,"Bordeaux"))  
print("--------------------------------------------------------------------------\n")  



print("test de filtrage par filliere :\n")  
print("filtrage par la filliere Philosophie :\n")  
print(filtrage_orientation_filiere(lis_orientation,"Philosophie"))  
print("--------------------------------------------------------------------------\n")  
print("filtrage par la region Faculté de Médecine:\n")  
print(filtrage_orientation_filiere(lis_orientation,"Faculté de Médecine")) 



"""
Auteur: Ikdoumi Ilian le 7/03
"""

from dataclasses import dataclass

@dataclass
class orientation:
    effectif_EG: str
    region: str
    filiere: str

def affichage_orientation(orientation):
    """
    Rôle : affiche les informations d'une instance de la classe orientation
    Type des données :
        orientation : objet de la classe orientation contenant les attributs :
            - effectif_EG : str
            - region : str
            - filiere : str
    Résultat : aucun (affichage uniquement)
    """
    print(orientation.effectif_EG, orientation.region, orientation.filiere)

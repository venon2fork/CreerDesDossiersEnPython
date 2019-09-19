import os

chemin = "Ajouter votre propre chemin"

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

for key, value in d.items():
    for f in value:
        ds = os.path.join(chemin,key,f)
        os.makedirs(ds,exist_ok=True)
    
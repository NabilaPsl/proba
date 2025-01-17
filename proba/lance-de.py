import random  # Importer le module random
# Définir la liste représentant un dé à 6 faces
faces_du_de = [1, 2, 3, 4, 5, 6]
# Initialiser les variables
T = 10000  # Nombre total de lancers
n = 0      # Compteur du nombre de fois où l'on obtient un 3
# Simuler 10 000 lancers
for i in range(T):
    lancer = random.choice(faces_du_de)  # Sélectionner aléatoirement une face du dé
    if lancer == 3:
        n += 1  # Incrémenter le compteur si le numéro obtenu est 3

# Calculer les probabilités
P1 = n / T        # Probabilité observée
P2 = 1 / 6        # Probabilité théorique
# Afficher les résultats
print(f"Probabilité observée (P1) : {P1}")
print(f"Probabilité théorique (P2) : {P2}")
print(f"Différence : {abs(P1 - P2)}")

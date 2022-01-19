
from random import randint
# jeu de juste prix
# choisir un nombre entre 1 et 1000
# statut du jeu ( on/off )
# tant que le jeu n'est pas fini
# -> entré un prix
# -> si il trouve le juste prix "c'est gagné !"
# -> sinon on affiche "c'est moin" ou "c'est plus"

prix = randint(1, 1000)

running = True

while running:
    prix_user = int(input(print("entré un prix entre 1 et 1000")))
    if prix_user == prix:
        print("BRAVO")
        running = False
    elif prix_user > prix:
        print("c'est moin")
    elif prix_user < prix:
        print("c'est plus")

print("FIN DU JEU MERCI D'AVOIR JOUER")
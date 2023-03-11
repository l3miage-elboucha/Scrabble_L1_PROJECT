import random
from scrabble import *


joueurs = []
dic = init_dico()
sac = init_pioche(dic)

# initialisation du joueurs
nb_joueurs = int(input('Entrez le nombre de joueurs (min/max 2/4): '))
for i in range(nb_joueurs):
	joueur = {}
	joueur["nom"] = input('Entrer le nom du joueur{}: '.format(i+1))
	joueur["main"] = piocher(7, sac)
	joueur["score"] = 0
	joueurs.append(joueur)

# le 1er tour (joueur) est choisi aléatoirement 
joueur_courant = random.choice(joueurs)

partie_finie = False
while not partie_finie:
	tour_joueur(joueur_courant)
	partie_finie = est_finie(sac, joueurs)
	if (not partie_finie):
		joueur_courant = joueur_suiv(joueurs, joueur_courant)

# aprés la fin du partie, le joueur gagnant (joueur_courant) remporte la valeur cumulée des lettres qui restent a l'adversaire et l'adversaire soustrait cette valeur de son propre score
joueur_gagnant = joueur_courant
for j in joueurs:
	for c in j["main"]:
		j["score"] -= dic[c]["val"]
	if (j["score"] > joueur_gagnant["score"]):
		joueur_gagnant = j


print('\n'*4)
print('\t BRAVO {} , Vous avez gagné avec un score de {} \t'.format(joueur_gagnant["nom"], joueur_gagnant["score"]))
print('\n'*4)

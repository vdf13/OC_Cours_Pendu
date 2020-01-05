"""TP du cours Python sur le jeu du pendu
fichiers: 
donnees.py 
fonctions.py 
pendu.py
score
"""

#from donnees import *
from fonctions import *

nb_essai = 8
score = recup_score()		# recupère les scores
utilisateur = nom_utilisateur()		# on demande le nom

# tester si le joueur existe ou le créer dans le fichier score
if utilisateur not in score.keys():		# teste clé du dict
	score[utilisateur] = 0

continuer_partie = "o"		# variable pour stoper le jeu

# corps du programme
while continuer_partie != "n":
	print("joueur {0}: {1} point(s)".format(utilisateur, score[utilisateur]))
	mot = choisir_mot()
	print(mot)			# debug
	lettre = cx_lettre()
	if lettre in mot:
		print("Bravo ! Vous avez trouvé une lettre, le \" {0} \" est dans le mot.".format(lettre))
	else:
		print("Désolé, cette lettre n'est pas dans le mot")
		nb_essai -= 1
		print(nb_essai)

	continuer_partie = input("Voulez-vous continuer la partie (O/N) ?")
	continuer_partie = continuer_partie.lower()

# la partie est finie on enregistre les scores
enrg_score(score)





enrg_score(score)


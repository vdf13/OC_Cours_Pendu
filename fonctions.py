# fichier des fonction du pendu
import os
os.chdir("C:/01_DATA/PYTHON/pendu")
import pickle

from random import randrange
from random import choice
from donnees import *


# Ouvrir le  fichier donnees et créer la liste de mots
# variable liste
fichier = open("donnees.py", "r")	# ouvre le fichier
contenu = fichier.read()			# importe le contenu
liste = contenu.split("\n")			# converti la str en list
fichier.close()


# Appeler un mot du fichier donnees et le choisir
# variable


# a supprimer mot_cache = ["*", "*", "*", "*", "*", "*", "*", "*"]

# decomposer les lettres du mot 

# Création d'un dictionnaire rempli de *  pour chaque lettre
def mot_masque():
	""" Fonction qui masque le mot choisi et crée le dict
	pour afficher les lettres trouvées"""
	mot_mask = {}
	mot_cible = []
	i = 0
	while i < len(mot):
		mot_mask[i] = "*"
		mot_cible.append(mot[i])
		i += 1

# demander la lettre du joueur et nombre de tentative
def cx_lettre():
	lettre = input("Tapez une lettre: ")
	lettre = lettre.lower()
	c = 0
	if lettre not lettre.isalpha():
		print("Ceci n'est pas un caractère acceptable")
		return cx_lettre()
	else:
		return lettre

def choisir_mot():
	"""Cette fonction renvoie le mot choisi dans la liste
	On utilise la fonction randrange du module random, 
	un autre choix avec choice"""	
	i = randrange(0, len(liste))		# ouvre le module aléatoire de 0 à la taille de la liste
	mot = liste[i]
	return mot
	# return choice(liste)

def nom_utilisateur():
	""" Obtenir le nom du joueru et l'inscrire dans 
	le fichier score """
	utilisateur = input("entrez le nom du joueur :")
	# Mettre la première lettre en majuscule
	utilisateur = utilisateur.Capitalize()
	if not utilisateur.isalnum() or len(utilisateur)<4:
		print ("ce nom n'est pas correct.")
		return nom_utilisateur()
	else:
		return utilisateur

def enrg_score():
	""" Enregistrer les scores dans un fichier score, 
	le créer si il n'existe pas"""


def recup_score():
	""" Récupère les anciens scores du fichiers chargé dans un dictionnaire"""




# code a integrer dans le fichier principal
		for b in mot_cible:
			if lettre == b:
				mot_mask[c] = b
				c += 1


	
		







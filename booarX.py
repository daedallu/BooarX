#!/usr/bin/env python3

import collect_items as c_i #une module pour collecter les donnees
import specnum as sn #un module pour modifier les donnees
import logo_ascii as logo
import pseudo_secrets as pseudo
#listes vides
list_edit=[]
list_main=[]
#charge le buffer pour la présentation du logo en ascii
logo.presentation("BooarX.txt")
#procedure de insertion des donnees
print("NAME=", end="")
c_i.items_collect('')
print("SURNAME=", end="")
c_i.items_collect('')
print("BIRTH(YYYYMMDD)=", end="")
c_i.birth_collect('')
print("NICKNAME=", end="")
c_i.items_collect('')
print("PARTNER=", end="")
c_i.items_collect('')
print("BIRTH(YYYYMMDD)=", end="")
c_i.birth_collect('')
print("NICKNAME=", end="")
c_i.items_collect('')
print("CHILD=", end="")
c_i.items_collect('')
print("BIRTH(YYYYMMDD)=", end="")
c_i.birth_collect('')
print("NICKNAME=", end="")
c_i.items_collect('')
print("SPORTS IDOL=", end="")
c_i.items_collect('')
print("MOTHER=", end="")
c_i.items_collect('')
print("FATHER=", end="")
c_i.items_collect('')
print("COMPANY=", end="")
c_i.items_collect('')
print("PET NAME=", end="")
c_i.items_collect('')

#procedure de insertion de donnees autres et diverses 
while True:
	print('> ')
	string=c_i.items_collect('')
	if string=='':
		break
"""
La fonction qui copie la liste temporaire stockee dans 
la bibliotheque est transferee ou stockee dans la variable.
Ainsi, nous disposons d une copie securisee du contenu qui 
peut continuer a etre traite dans les prochaines fonctions des autres bibliotheques.
"""
list_basic=list(c_i.copy_list_basic('')	)

"""
Une fonction pour renvoyer la liste stockee dans le module. 
Il est applique comme un test pour voir s il y a quelque chose sur la liste et si les etapes precedentes ont fonctionne. 
Comme il pas indispensable au fonctionnement du code dans son ensemble, il est commente par defaut.
"""
#c_i.return_list()

"""
Ici, la copie de la liste stockee dans le module collect_items est prise et avec une boucle for, 
les eléments de list_basic sont transmis un a un a list_edit, pour une nouvelle section de 
modification des donnees.
"""
for i in list_basic:
	list_edit.append(i)

print(list_basic)

"""
Une fonction pour stocker une copie de list_basic dans 
le module, pour le modification de donnees.
"""
sn.copy_list(list_edit) 

mode_spec=input('INSERT SPECIAL CHARS? Y/N\n> ')
ms=mode_spec.lower()

if mode_spec=='y':
	"""
	Ces fonctions modifie les strings, en changeant certaines lettres 
	par des caractères spéciaux, générant ainsi une plus grande variation 
	de ces strings. Exemple : 'vovomafalda' -> 'vovom@f@ld@'
	"""
	sn.spec_char()
	sn.spec_char_misc()

mode_num=input('INSERT NUMBERS? Y/N\n> ')
mn=mode_num.lower()

if mode_num=='y':
	"""
	Ces fonctions, comme les precedentes, modifient les strings, 
	en inserant uniquement des chiffres a la place de certaines lettres.
	"""
	sn.num_char()
	sn.num_char_misc()

"""
Une fonction pour passer les elements de la liste interne du module vers la liste vide du code
(dans ce cas, 'list_main')
"""
list_main = sn.transfer_list(list_main)

print(list_main)





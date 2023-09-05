#!/usr/bin/env python3

import collect_items as c_i #une bibliotheque pour collecter les donnees
import handling_of_data as hdata #une bibliotheque pour modifier les donnees
import logo_ascii as logo
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

c_i.return_list()

for i in list_basic:
	list_edit.append(i)

print(list_basic)
	
hdata.copy_list(list_edit)
hdata.spec_char()
list_main = hdata.transfer_list(list_main)

print(list_main)





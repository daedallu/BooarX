from magic_spell import *
import pseudo_secrets as pseudo
from random import randint

listA=['banana', 'hammock', 'cuñado']
spell="eu sou hacker de computacao"
list_vide=[]

a=cut_edges(cut_voc(spell))
string=to_string(a)
b=mirror(listA)
print(string, b)
i=0
size=10
while i<size:
    psswd=''.join(pseudo.choice(listA) for psswd in range(randint(0,5)))
    list_vide.append(psswd)
    i=i+1


print(list_vide)
	

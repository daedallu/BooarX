import secrets

mainlist=[]
listA=[]
listNum=[]
listModspec=["**","_","@", "$",]
#ranGo=int(input("DEFINE A RANGE= "))
def presentation():
	f=open("BooarX.txt", "r")
	print(f.read())
	print('\n')
	print("WELCOME TO BOOARX!") 
	print("MAKE A KEYLIST IN TXT FOR YOUR TARGET!\n\n")

	
def main():
	global listA, mainlist
	name = input('NAME= ')
	listA.append(name.lower())
	surname = input('SURNAME= ')
	listA.append(surname.lower())
	nick = input('NICKNAME= ')
	listA.append(nick.lower())
	birth = input('BIRTHDAY(aaaammdd= ')
	listA.append(birth.lower())
	partner = input('PARTNER/SPOUSE/CONSORT= ')
	listA.append(partner.lower())
	nickpart = input('NICKNAME= ')
	listA.append(nickpart.lower())
	sonname = input("CHILD'S NAME= ")
	listA.append(sonname.lower())
	nickchild = input('NICKNAME= ')
	listA.append(nickchild.lower())
	father = input("FATHER'S NAME= ")
	listA.append(father.lower())
	mother = input("MOTHER'S NAME= ")
	listA.append(mother.lower())
	faith = input("FAITH(RELIGIOUS FIGURE)= ")
	listA.append(faith.lower())
	sport = input('SPORTS IDOL= ')
	listA.append(sport.lower())
	petname = input('PET NAME= ')
	listA.append(petname.lower())
	for i in listA:
		x=i.replace(" ","")
		mainlist.append(x)
i=0
e=1

def various():
	global listA, i, e
	print('OTHER STRING(S) RELATED TO TARGET. <!> TO STOP')
	while i<e:
		other = input('> ')
		if other == '!':
			other = ""
			e=0
		else:
			otherX=other.replace(" ", "")
			listA.append(otherX)
def num():
	global listA, listNum, i, e
	print("D'YOU WANNA PUT NUMBERS IN LIST? <n> for not.")
	chooz=input("> ")
	if chooz == 'n' or chooz=='N':
		pass
	else:
		global listA, mainlist
		
		for item in listA:
			rep1=item.replace("o", "0")
			listNum.append(rep1)
			rep2=rep1.replace("a", "4")
			listNum.append(rep2)
			rep3= rep2.replace('i','1')
			listNum.append(rep3)
			rep4=rep3.replace("z", "2")
			listNum.append(rep4)
			rep5=rep4.replace("e", "3")
			listNum.append(rep5)
			rep6= rep5.replace('g','9')
			listNum.append(rep6)
			rep7= rep6.replace('t','7')
			listNum.append(rep7)
			rep8= rep7.replace('s','5')
			listNum.append(rep8)
			rep9= rep8.replace('b','6')
			listNum.append(rep9)
		for i in listNum:
			mainlist.append(i)

def upperRep():
	global listA
	
	for item in listA:
		a=item.capitalize()
		mainlist.append(a)		
def charspec():	
	print("D'YOU WANNA PUT SPECIAL CHAR IN LIST? <n> for not.")
	chooz=input("> ")
	if chooz == 'n' or chooz=='N':
		pass
	else:
		global listA, listModspec, mainlist
		
		for item in listA:
			rep1=item.replace("o", "*")
			listModspec.append(rep1)
			rep2=rep1.replace("a", "@")
			listModspec.append(rep2)
			rep3= rep2.replace('h','#')
			listModspec.append(rep3)
			rep4= rep2.replace('s','$')
			listModspec.append(rep4)
		for i in listModspec:
			mainlist.append(i)
			
def  rmClone():
	global mainlist
	for item in mainlist:
		if item not in mainlist:
			mainlist.append(item)
		mainlist.sort()
		return 1

def sorT():
	global mainlist
	mainlist.sort()
presentation()
name=input("NAME OF TXT FILE= ")
main()
various()
num()
upperRep()
charspec()
rmClone()
sorT()
ranGo= len(mainlist)**2
#msg=f'{ranGo} was generated based on provided data.'
#print(msg)
f=open(f"{name}.txt", "a")
for i in range(ranGo): 
	word = ''.join(secrets.choice(mainlist) for i in range(1, 5))
	if word != " " or word != "":
		f.write(f'{word}\n')
		f.write(f'**{word}**\n')
		f.write(f'##{word}##\n')
f.close()
	
	



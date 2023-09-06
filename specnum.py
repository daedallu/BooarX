listA=[]
listB=[]

def copy_list(std_list):
	global listA
	listA=std_list.copy()

	
def spec_char():
	global listA
	for i in listA:
		replone=i.replace('a','@')
		listB.append(replone)
		repltwo=i.replace('s','$')
		listB.append(repltwo)
		replthree=i.replace('h','#')
		listB.append(replthree)
		replfour=i.replace('i','%')
		listB.append(replfour)
	return listB
	
def spec_char_misc():
	global listA
	for i in listA:
		replone=i.replace('a','@')
		listB.append(replone)
		repltwo=replone.replace('s','$')
		listB.append(repltwo)
		replthree=repltwo.replace('h','#')
		listB.append(replthree)
		replfour=replthree.replace('i','%')
		listB.append(replfour)
	return listB
	
def num_char():
	global listA
	for i in listA:
		replone=i.replace('a','4')
		listB.append(replone)
		repltwo=i.replace('b','6')
		listB.append(repltwo)
		replthree=i.replace('e','3')
		listB.append(replthree)
		replfour=i.replace('g','9')
		listB.append(replfour)
		replfive=i.replace('i','1')
		listB.append(replfive)
		replsix=i.replace('o','0')
		listB.append(replsix)
		replseven=i.replace('s','5')
		listB.append(replseven)
		repleight=i.replace('t','7')
		listB.append(repleight)
		replnine=i.replace('z','2')
		listB.append(replnine)
	return listB

def num_char_misc():
	global listA
	for i in listA:
		replone=i.replace('a','4')
		listB.append(replone)
		repltwo=replone.replace('b','6')
		listB.append(repltwo)
		replthree=repltwo.replace('e','3')
		listB.append(replthree)
		replfour=replthree.replace('g','9')
		listB.append(replfour)
		replfive=replfour.replace('i','1')
		listB.append(replfive)
		replsix=replfive.replace('o','0')
		listB.append(replsix)
		replseven=replsix.replace('s','5')
		listB.append(replseven)
		repleight=replseven.replace('t','7')
		listB.append(repleight)
		replnine=repleight.replace('t','7')
		listB.append(replnine)
	return listB

def transfer_list(std_list):
	global listB
	std_list=listB.copy()
	return std_list
	


	

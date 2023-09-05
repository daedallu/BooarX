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



def transfer_list(std_list):
	global listB
	std_list=listB.copy()
	return std_list
	


	

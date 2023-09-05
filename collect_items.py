
list_basic=[]

def copy_list_basic(cp_list_basic):
	global list_basic
	cp_list_basic=list_basic.copy()
	return cp_list_basic
	
	
def items_collect(new_item):
	global list_basic
	i=input(" ")
	new_item = i.replace(" ","")
	if new_item!=" " or new_item!="":
		list_basic.append(new_item)
	return new_item
	
def birth_collect(new_item):
	global list_basic
	i=input(" ")
	LENGTH=len(i)
	new_item = i.replace(" ","")
	if new_item!=" " or new_item!="":
		list_basic.append(new_item)
	if LENGTH!=8 and LENGTH!=0:
		raise Exception("The birth data must have 'YYYYMMDD' format.")
	
def return_list():
	global list_basic
	print(list_basic)

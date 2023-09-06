

list_exit=[]
list_exit_novoc=[]
list_exit_clean=[]
list_vocoff=['a','e','i','o','u','A','E','I','O','U']

def to_string(list_main):
	for i in list_main:
		abc=''.join(list_main)
	return abc
	
def cut_clone(list_main):
	for i in list_main:
		if i not in list_exit:
			list_exit.append(i.upper())
	return list_exit

def cut_voc(list_main):
	for i in list_main:
		if i not in list_vocoff:
			list_exit_novoc.append(i.upper())
	return list_exit_novoc

def cut_white_spaces(list_main):
	for i in list_main:
		if i !=' ':
				list_exit_clean.append(i.upper())
	return list_exit_clean


	


			
			
			
			

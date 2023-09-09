
std_list_mirror=[]
std_list_exit=[]
std_list_exit_novoc=[]
std_list_exit_clean=[]
std_list_vocoff=['a','e','i','o','u','A','E','I','O','U']

def to_string(std_list_a):
	for i in std_list_a:
		abc=''.join(std_list_a)
	return abc

def cut_voc(std_list_c):
    std_list_exit_novoc.clear()
    for i in std_list_c:
        if i not in std_list_vocoff:
            std_list_exit_novoc.append(i.lower())
    return std_list_exit_novoc

def cut_edges(std_list_d):
    std_list_exit_clean.clear()
    for i in std_list_d:
        if i !=' ' and  i not in std_list_exit_clean:
            std_list_exit_clean.append(i.lower())
    return std_list_exit_clean

def mirror(std_list_d):
    std_list_mirror.clear()
    for i in std_list_d:
        abc=i[::-1]
        std_list_mirror.append(abc) 
    return std_list_mirror
    

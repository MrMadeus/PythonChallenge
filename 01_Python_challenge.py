def shift(code_string):
	fin_string = ''
	for i in code_string:
		if i in " .'":
			fin_string = fin_string + i
		else:
			fin_string = fin_string + chr(ord(i) + 2)
	return fin_string

set_string = input('Введите строку:')
print (shift(set_string))
import urllib.request
import re

set_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
i = 12345
while True:
	open_url = set_url + str(i)
	setUrl = urllib.request.urlopen(open_url)
	data_line = setUrl.read()
	line = data_line.decode('utf8')
	print(line)
	find_numbers = re.findall(r'\d+', line)
	if line == 'Yes. Divide by two and keep going.':
		i = str(int(i) / 2)
	elif len(find_numbers) == 2:
		i = find_numbers[1]
	elif len(find_numbers) != 1:
		print(line)
		break
	else:
		i = find_numbers[0]
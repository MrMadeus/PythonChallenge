import urllib.request
import re

def bodyguards(set_str):
	if len(set_str) != 9:
		return ''
	if re.match(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', set_str):
		return set_str[4]
	else:
		return ''

i = 0
set_line = ''
setUrl = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
for bline in setUrl.readlines():
	line = bline.decode('utf8')
	if line == '<!--\n':
		i = 1
	if i == 1:
		set_line = set_line + line

fin_str = ''
for i in range(0, len(set_line)):
	fin_str = fin_str + bodyguards(set_line[i:i + 9])

print(fin_str)
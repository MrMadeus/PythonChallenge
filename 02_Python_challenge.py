import urllib.request

def letters(setstr):
	final_str = ''
	for i in setstr:
		if ord(i) in (40 and range(97, 123)):
			final_str = final_str + i
	return final_str

i = 0
set_line = ''
setUrl = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
for bline in setUrl.readlines():
	line = bline.decode('utf8')
	if line == '<!--\n':
		i = i + 1
	if i == 2:
		set_line = set_line + line

print(letters(set_line))

count_s = {}
for i in set_line:
	if i not in count_s:
		count_s[i] = 1
	else:
		count_s[i] = count_s[i] + 1

result_string = ''

for key in count_s:
	if count_s[key] == 1:
		result_string = result_string + key

print(result_string)
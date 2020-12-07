import urllib.request
import pickle

data = ''
set_url = 'http://www.pythonchallenge.com/pc/def/banner.p'
setUrl = urllib.request.urlopen(set_url)
for bline in setUrl.readlines():
	line = bline.decode('utf8')
	data = data + line[:-1] #use slising to remove '/n'

#print(data)

with open('pick.p', 'wb') as f:
	f.write(str(data))

with open('pick.p', 'rb') as f:
	exp_data = pickle.load(f)

print(exp_data)
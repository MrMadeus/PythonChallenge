import urllib.request
import pickle

data = ''
set_url = 'http://www.pythonchallenge.com/pc/def/banner.p'
setUrl = urllib.request.urlopen(set_url)

exp_data = pickle.load(setUrl)

for line in exp_data:
	print(''.join([k * j for k, j in line]))
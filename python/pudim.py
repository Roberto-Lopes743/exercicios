import urllib
import urllib.request
try:
    urllib.request.urlopen('https://www.pudim.com')
except urllib.error.URLError as e:
    print('O site Pudim não está acessível no momento.')
else:
    print('o site esta acessível no momento.')
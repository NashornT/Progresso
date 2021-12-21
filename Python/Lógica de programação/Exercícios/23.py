import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://google.com.br/')
except urllib.request.URLError:
    print('Site não acessível no momento.')
else:
    print('Site acessivel')



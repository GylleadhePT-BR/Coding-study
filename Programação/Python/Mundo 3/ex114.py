import urllib
from urllib import request



try:
    site = urllib.request.urlopen('https://www.Youtube.com')
except urllib.error.URLError:
    print('O site não está disponivel....')
else:
    print('O site está acessivel...')
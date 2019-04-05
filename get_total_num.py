url = 'http://192.168.1.8:5000/total.htm'

import urllib
import re
pat = re.compile('[0-9]+')
sock = urllib.urlopen(url)
li = pat.findall(sock.read())
sock.close()
size = int(li[0])
print size
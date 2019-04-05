# -*- coding: latin-1 -*-
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '2.3.3'
desired_caps['deviceName'] = '$ LGOTMS3ee9f2'
desired_caps['noReset'] = True
desired_caps['fullReset'] = False

TIEMPO_ACTUALIZAR = 120
TIEMPO_ESPERA = 0.1
NUMERO_CONTACTOS = 7
PRIMER_CONTACTO = "Anahi"
NUM_POSTAL = "+593"
IP_APPIUM = 'http://localhost:4723/wd/hub'
IP = "192.168.0.1"

import socket
import urllib
import re
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()

pat = re.compile('[0-9]+')
url = "http://"+IP+":5000/total.htm"
sock = urllib.urlopen(url)
li1 = pat.findall(sock.read())
sock.close()

url = "http://"+IP+":5000/max_contactos.htm"
sock = urllib.urlopen(url)
li2 = pat.findall(sock.read())
sock.close()

MAXIMO_CONTACTOS = int(li2[0])
TOTAL = int(li1[0])

import saludos
MENSAJE = saludos.MENSAJE
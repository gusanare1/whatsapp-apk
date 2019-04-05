# -*- coding: latin-1 -*-
'''
ACTUALIZR IP******
para abrir uiautomatorviewer:
	cmd
	adb devices
	uiautomatorviewer
		cd C:\Users\lenov\AppData\Local\Android\Sdk\tools\bin
		uiautomatorviewer.bat

ABRIR APPIUM
	no en modo server
	se abre la apk

CAMBIAR 099... POR 59399...	
ABRIR FLASK
cmd
cd Documents
python fla.py
'''
import constants_j1 as constants
from funcion import actualizar, enviar_foto, sleep, tiempo
import saludos
from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import math

TIEMPO_ACTUALIZAR = constants.TIEMPO_ACTUALIZAR
TIEMPO_ESPERA = constants.TIEMPO_ESPERA

TOTAL = constants.TOTAL
MAXIMO_CONTACTOS = constants.MAXIMO_CONTACTOS
IP_APPIUM = constants.IP_APPIUM
desired_caps = constants.desired_caps
IP = constants.IP
PRIMER_CONTACTO = constants.PRIMER_CONTACTO
NUM_POSTAL = constants.NUM_POSTAL

print("Tengo "+str(TOTAL)+" contactos y me envian "+str(MAXIMO_CONTACTOS)+" contactos")
fin_rango = int(math.ceil(float(TOTAL) / float(MAXIMO_CONTACTOS)))
print "Numero de veces que se va a correr: "+str(fin_rango)


flag_once_apk = True
flag_once_whatsapp = True

import time
starting_point = time.time()

for i in range(0,fin_rango):
	'''
	#***********************ABRIR APK ADDCONTACTO*****************************
	desired_caps['appPackage'] = 'com.example.lenov.addcontacto'
	desired_caps['appActivity'] = '.gus.MainActivity'
	driver = webdriver.Remote(IP_APPIUM, desired_caps)
	wait = WebDriverWait(driver, TIEMPO_ACTUALIZAR)
	tiempo("Abriendo APK",starting_point)
	if flag_once_apk:
		#SOLO 1 VEZ EL NUMERO SE ACTUALIZA
		xpath = "//android.widget.EditText[contains(@resource-id,'com.example.lenov.addcontacto:id/numero')]"
		wait_for = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
		apk = driver.find_element_by_xpath(xpath)
		#apk.click()
		sleep(TIEMPO_ESPERA)
		apk.clear()
		sleep(TIEMPO_ESPERA)
		apk.send_keys(IP)
		sleep(TIEMPO_ESPERA)
		xpath = "//android.widget.Button[contains(@resource-id,'com.example.lenov.addcontacto:id/actulizar')]"
		wait_for = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
		apk = driver.find_element_by_xpath(xpath)
		apk.click()
		sleep(TIEMPO_ESPERA)
		flag_once_apk = False
		
	xpath = "//android.widget.Button[contains(@resource-id,'com.example.lenov.addcontacto:id/crear')]"
	wait_for = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
	apk = driver.find_element_by_xpath(xpath)
	apk.click()
	sleep(TIEMPO_ESPERA)
	driver.close_app()	
	tiempo("Cerrando APK",starting_point)
	'''
	#***********************ABRIR WHATSAPP*****************************
	try:
		print ("Tratando de entrar con HomeActivity")
		desired_caps['appPackage'] = 'com.whatsapp'
		desired_caps['appActivity'] = '.HomeActivity'
		driver = webdriver.Remote(IP_APPIUM, desired_caps)
		tiempo("Abriendo Whatsapp",starting_point)
		
		
	except :
		print ("Tratando de entrar con Main")
		desired_caps['appPackage'] = 'com.whatsapp'
		desired_caps['appActivity'] = '.Main'
		driver = webdriver.Remote(IP_APPIUM, desired_caps)
		
	wait = WebDriverWait(driver, TIEMPO_ACTUALIZAR)
	xpath = "//android.widget.ImageView[contains(@content-desc,'Nuevo chat')]"
	wait_for = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
	nuevo_chat = driver.find_element_by_xpath(xpath)
	nuevo_chat.click()
	sleep(TIEMPO_ESPERA)
	
	#PRESIONO A ACTUALIZAR 
	actualizar(driver)
	sleep(TIEMPO_ESPERA)
	#ESPERO ASTA QUE LLEGUEN ACTUALIZACIONES DE QUE PODEMOS ENVIAR A LOS CONTACTOS
	xpath = "//android.widget.ProgressBar[contains(@resource-id,'com.whatsapp:id/progress_bar')]"
	WebDriverWait(driver, TIEMPO_ACTUALIZAR).until(EC.invisibility_of_element_located((By.XPATH,xpath)))
	sleep(TIEMPO_ESPERA)
		
	
	flag_while = True
	array_nombre = []
	while(flag_while):
		try:
			xpath = "//android.widget.TextView"
			arr = driver.find_elements_by_xpath(xpath)
			sleep(TIEMPO_ESPERA)
			#J320AG DE 7 EN 7 -->MAXIMO
				
			for i in range(0,len(arr)):
				elem = arr[i].text
				if PRIMER_CONTACTO in elem:
					print "ENCONTRAD EL PRIMER CONTACTO"
					flag_while = False
				elif NUM_POSTAL in elem:
					if elem not in array_nombre:
						array_nombre.append(elem)
						#print "Enviando a: "+elem		
						#TIEMPO ESTIMADO 40seg
						#TIEMPO (2) 25s
						enviar_foto(driver, elem)
						tiempo("Enviado a "+elem,starting_point)
				sleep(TIEMPO_ESPERA)

			driver.swipe(300,1200,300,500)
			sleep(TIEMPO_ESPERA)
		except Exception as e:
			import traceback
			print(traceback.format_exc())
			
	array_nombre = []
	sleep(TIEMPO_ESPERA)
	driver.close_app()
	tiempo("Cerrando Whatsapp",starting_point)
	
	#***********************ABRIR APK ADDCONTACTO*****************************
	
	desired_caps['appPackage'] = 'com.example.lenov.addcontacto'
	desired_caps['appActivity'] = '.gus.MainActivity'
	driver = webdriver.Remote(IP_APPIUM, desired_caps)
	tiempo("Abiendo APK",starting_point)
	wait = WebDriverWait(driver, TIEMPO_ACTUALIZAR)
	print "Click en borrar"
	sleep(TIEMPO_ESPERA)
	xpath = "//android.widget.Button[contains(@resource-id,'com.example.lenov.addcontacto:id/borrar')]"
	wait_for = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
	apk = driver.find_element_by_xpath(xpath)
	apk.click()
	sleep(TIEMPO_ESPERA)
	driver.close_app()
	flag_once_whatsapp = True
	tiempo("Cerrando Apk",starting_point)
	
print "FIN"

tiempo("Total",starting_point)
sleep(TIEMPO_ESPERA)

import winsound
frequency = 2000  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

'''
http://www.software-testing-tutorials-automation.com/2015/10/ui-automator-viewer-get-android-app.html
uiautomatorviewer
uiautomatorviewer
python Documents/appium1.py

NSYALADORES
appium windows (jdk): https://bitbucket.org/appium/appium.app/downloads/
python 2: https://www.python.org/download/releases/2.7.2/
samsung drivers: 
'''
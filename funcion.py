# -*- coding: latin-1 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import constants

TIEMPO_ACTUALIZAR = constants.TIEMPO_ACTUALIZAR
TIEMPO_ESPERA = constants.TIEMPO_ESPERA
MENSAJE = constants.MENSAJE

def dormir(driver, xpath):
	wait = WebDriverWait(driver, TIEMPO_ACTUALIZAR)
	wait_for = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))


def actualizar(driver):
	#CLICK ACTUALIZAR
	xpath = "//android.widget.ImageView[contains(@content-desc,'Más opciones')]"
	dormir(driver, xpath)
	adjuntar = driver.find_element_by_xpath(xpath)
	adjuntar.click()
	sleep(TIEMPO_ESPERA)
	
	xpath = "//android.widget.TextView[contains(@text,'Actualizar')]"
	dormir(driver, xpath)
	actualizar =driver.find_element_by_xpath(xpath)
	actualizar.click()
	sleep(TIEMPO_ESPERA)
	
def enviar_foto(driver, elem):
	
	
	#ELEMENTO AL Q HACER CLICK (Abriendo el chat..)		
	xpath = "//android.widget.TextView[contains(@text,'"+elem+"')]"
	dormir(driver, xpath)
	el_click = driver.find_element_by_xpath(xpath)
	el_click.click()
	sleep(TIEMPO_ESPERA)
	
	#CLICK ADJUNTAR 
	xpath = "//android.widget.ImageButton[contains(@content-desc,'Adjuntar')]"
	dormir(driver, xpath)
	adjuntar = driver.find_element_by_xpath(xpath)
	adjuntar.click()
	sleep(TIEMPO_ESPERA)
	
	#CLICK GALERIA
	xpath = "//android.widget.ImageView[contains(@content-desc,'Galería')]"
	dormir(driver, xpath)
	galeria = driver.find_element_by_xpath(xpath)
	galeria.click()
	sleep(TIEMPO_ESPERA)
	
	#CLICK todos los archivos
	xpath = "//android.widget.TextView[contains(@text,'Todos los archivos')]"
	dormir(driver, xpath)
	galeria_todos_archivos = driver.find_element_by_xpath(xpath)
	galeria_todos_archivos.click()
	sleep(TIEMPO_ESPERA)
	
	#CLICK en el primera foto
	xpath = "//android.widget.ImageView[contains(@content-desc,'Foto')]"
	dormir(driver, xpath)
	foto = driver.find_elements_by_xpath(xpath)
	foto[0].click()
	sleep(TIEMPO_ESPERA)
	
	
	#CLICK EN ANADIR COMENTARIOS
	#PRIMERO ES UN TEXTVIEW.. LUEGO CUANDO LO SELECCIONAS, ES UN EDITTEXT
	
	xpath = "//android.widget.TextView[contains(@resource-id,'com.whatsapp:id/caption')]"
	dormir(driver, xpath)
	escribir = driver.find_element_by_xpath(xpath)
	escribir.click()
	sleep(TIEMPO_ESPERA)
	xpath = "//android.widget.EditText[contains(@text,'Añadir un comentario...')]"
	dormir(driver, xpath)
	escribir = driver.find_element_by_xpath(xpath)
	#escribir.click()
	sleep(TIEMPO_ESPERA)
	escribir.send_keys(MENSAJE)
	
	
	#CLICK en enviar la foto
	xpath = "//android.widget.ImageButton[contains(@content-desc,'Enviar')]"
	dormir(driver, xpath)
	enviar_foto = driver.find_element_by_xpath(xpath)
	enviar_foto.click()
	sleep(TIEMPO_ESPERA)
	
	#CLICK atras
	xpath = "//android.widget.LinearLayout[contains(@content-desc,'Navegar hacia arriba')]"
	dormir(driver, xpath)
	atras = driver.find_element_by_xpath(xpath)
	atras.click()
	sleep(TIEMPO_ESPERA)

	#ERROR A...
	try:
		xpath = "//android.widget.ImageView[contains(@content-desc,'Nuevo chat')]"
		dormir(driver,xpath)
		nuevo_chat = driver.find_element_by_xpath(xpath)
		nuevo_chat.click()
		sleep(TIEMPO_ESPERA)
	except:
		pass

def tiempo(fun, starting_point):
	from time import time
	elapsed_time = time() - starting_point
	elapsed_time_int = int(elapsed_time) 
	elapsed_time_minutes = elapsed_time_int / 60 
	elapsed_time_seconds = elapsed_time_int % 60
	print("Tiempo "+fun+" :"+str(elapsed_time_minutes)+" minutos y "+str(elapsed_time_seconds)+" segundos")
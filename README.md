# whatsapp-apk
Poner el PATH de java (para Android Studio y Appium), descargar Android Studio y SDK de android. Luego poner path de Sdk de android (File->Setting->Appariencia|Setting ->SDK).<br/>
Instalar python2 y sus dependencias (Appium-client selenium y flask)
Poner path de python
El telefono debe ser mayor a 5.0 Android
Recopilar ANDROID SOURCE CODE en android Studio (*****CUANDO SE CREE UN PROYECTO QUE NO SEA CON KOTLIN SINO CON JAVA****)
***SACAR LAS NOTIFICACIONES DEL CELULAR
CAMBIAR LAS CONFIGURACIONES DEL SCRIPT (EN CONSTANTS***.PY)
    *****
    desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '$ ADB DEVICES'
desired_caps['noReset'] = True
desired_caps['fullReset'] = False

TIEMPO_ACTUALIZAR = 120
TIEMPO_ESPERA = 0.1
NUMERO_CONTACTOS = 7
PRIMER_CONTACTO = "Anahi" #CREAR PRIMER CONTACTO
NUM_POSTAL = "+593"
IP_APPIUM = 'http://localhost:4723/wd/hub'
IP = "192.168.1.4"

 DESCOMENTAR AAPPIUM_J1 "ADD CONTACT"
 CAMBIAR desired_caps['appPackage'] = 'xxxx' POR EL PAQUETE COMPILADO Y desired_caps['appActivity'] = 'xxx' POR EL NOMBRE DE DE LA APLICACION 

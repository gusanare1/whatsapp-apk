# whatsapp-apk
Poner el PATH de java (para Android Studio y Appium), descargar Android Studio y SDK de android. Luego poner path de Sdk de android (File->Setting->Appariencia|Setting ->SDK).<br/>
Instalar python2 y sus dependencias (Appium-client selenium y flask)<br/>
Poner path de python<br/>
El telefono debe ser mayor a 5.0 Android<br/>
Recopilar ANDROID SOURCE CODE en android Studio (*****CUANDO SE CREE UN PROYECTO QUE NO SEA CON KOTLIN SINO CON JAVA****)<br/>
***SACAR LAS NOTIFICACIONES DEL CELULAR<br/>
CAMBIAR LAS CONFIGURACIONES DEL SCRIPT (EN CONSTANTS***.PY)<br/>
    *****<br/>
    desired_caps['platformVersion'] = '7.1.2'<br/>
desired_caps['deviceName'] = '$ ADB DEVICES'<br/>
<br/>
TIEMPO_ACTUALIZAR = 120<br/>
TIEMPO_ESPERA = 0.1<br/>
NUMERO_CONTACTOS = 7<br/>
PRIMER_CONTACTO = "Anahi" #CREAR PRIMER CONTACTO<br/>
NUM_POSTAL = "+593"<br/>
IP = "192.168.1.4"<br/>

 DESCOMENTAR AAPPIUM_J1 "ADD CONTACT"<br/>
 CAMBIAR desired_caps['appPackage'] = 'xxxx' POR EL PAQUETE COMPILADO Y <br/>
 desired_caps['appActivity'] = 'xxx' POR EL NOMBRE DE DE LA APLICACION <br/>

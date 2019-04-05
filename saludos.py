# -*- coding: latin-1 -*-

CUERPO = "Esta rosa es para que tenga buen dia"
SALUDOS = "Buen dia"

def morning():
    return 'Buenos dias'

def afternoon():
    return 'Buenas tardes'

def night():
    return 'Buenas noches'

	
TOD = {
		7: morning,
		8: morning,
		9: morning,
		10: morning,
		11: morning,
		12: afternoon,
		13: afternoon,
		14: afternoon,
		15: afternoon,
		16: afternoon,
		17: afternoon,
		18: night,
		19: night,
		20: night,
		21: night,
		22: night
		
        }
import datetime
now = datetime.datetime.now()
hora = int(now.hour)
SALUDOS = TOD[hora]()
print("Los salids son automaticos")
CUERPO = raw_input("Ingrese el cuerpo del mensaje: ")
MENSAJE = CUERPO+". \n"+SALUDOS+"."

print("Mensaje a enviar: "+MENSAJE)
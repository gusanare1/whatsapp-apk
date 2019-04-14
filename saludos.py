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
		0: night(),
		1: night(),
		2: night(),
		3: night(),
		4: night(),
		5: night(),
		6: morning(),
		7: morning(),
		8: morning(),
		9: morning(),
		10: morning(),
		11: morning(),
		12: afternoon(),
		13: afternoon(),
		14: afternoon(),
		15: afternoon(),
		16: afternoon(),
		17: afternoon(),
		18: night(),
		19: night(),
		20: night(),
		21: night(),
		22: night(),
		23: night(),
        }
import datetime
now = datetime.datetime.now()
hora = int(now.hour)
SALUDOS = TOD[hora]
print("Los salids son automaticos")
CUERPO = raw_input("Ingrese el cuerpo del mensaje: ")
MENSAJE = CUERPO+". \n"+str(SALUDOS)+"."

print("Mensaje a enviar: "+MENSAJE)
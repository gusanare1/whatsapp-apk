from flask import Flask
from flask import request

MAX = 50 #MAXIMO CONTACTOS POR GET
'''
LA IP PRIVADA DEL EQUIPO
'''
IP = '192.168.1.8' #cambiar si no hay conexion a internet... (manual)

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()

PATH_FILE = "familia.csv"
app = Flask(__name__)

'''
RECORREMOS EL ARCHIVO Y MANDAMOS 
*****TODO SECUENCIAL******
0-> SI ES EL COMIENZO
NUM-> DESDE EL NUMERO SIGUIENTE AL QUE RECIBO
'''



@app.route("/data.htm")
def data():
	#ultimo numero 
	num = request.args.get('num')
	lines = ""
	i=0
	sgte = False
	if num=="0":
		with open(PATH_FILE) as file:
			for line in file:
				line = line.strip() #or some other preprocessing
				if line[:3]=="593":
					line = "+"+line
				lines = lines+line +";"#storing everything in memory!
				i=i+1
				if(i==MAX):
					break;
			lines = lines[:-1]
	else:
		with open(PATH_FILE) as file:
			for line in file:
				line = line.strip() #or some other preprocessing
				
				if sgte:
					if line[:3]=="593":
						line = "+"+line
					lines = lines+line +";"#storing everything in memory!
					i=i+1
				
				if line == num:
					sgte = True
				
				if(i==MAX):
					break;
			lines = lines[:-1]
	print(lines)
	return lines
	

'''
RECORREMOS EL ARCHIVO Y MANDAMOS 
*****TODO SECUENCIAL******
0-> SI ES EL COMIENZO
NUM-> DESDE EL NUMERO SIGUIENTE AL QUE RECIBO
'''
@app.route("/remo.htm")
def remo():
	#ultimo numero 
	num = request.args.get('num')
	SIZE = int(request.args.get('size'))
	lines = ""
	i=0
	sgte = False
	if num=="0":
		with open(PATH_FILE) as file:
			for line in file:
				line = line.strip() #or some other preprocessing
				if line[:3]=="593":
					line = "+"+line
				lines = lines+line +";"#storing everything in memory!
				i=i+1
				if(i==MAX):
					break;
			lines = lines[:-1]
	else:
		with open(PATH_FILE) as file:
			for line in file:
				line = line.strip() #or some other preprocessing
				
				if sgte:
					break
				if line == num:
					sgte = True
				if line[:3]=="593":
					line = "+"+line
				
				lines = lines+line +";"#storing everything in memory!
						
			lines_ = lines[:-1].split(';')[-SIZE:]
			lines = ';'.join(str(x) for x in lines_)
	print(lines)
	return lines

	
@app.route("/todos.htm")
def todos():
	#ultimo numero 
	lines = ""
	i=0
	with open(PATH_FILE) as file:
		for line in file:
			line = line.strip() #or some other preprocessing
			if line[:3]=="593":
				line = "+"+line
			lines = lines+line +";"#storing everything in memory!
			i=i+1
			if(i==MAX):
				break;
		lines = lines[:-1]
	print(lines)
	return lines

	
	
@app.route("/total.htm")
def total():
	num = 0
	fichero = open(PATH_FILE, 'r')
	num = len(fichero.readlines()) # devolvera NUMERO DE LINEAS (CONTACTOS)
	fichero.close()
	return "NUm"+str(num)


@app.route("/max_contactos.htm")
def max_contactos():
	return "MAX"+str( MAX )
	
print("My IP: "+IP)
if __name__ == "__main__":
    app.run(host= IP)
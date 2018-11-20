"""Trabajo Practico N° 1 - Analisis Numerico - Curso Tarela - Grupo 6"""

#Martes 09 de Octubre

#Integrantes:
#Julian Garcia Delfino - 100784
#Franco Giordano - 100608
#Agustin Yanuchausky - 99496

from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np
import math

def printIntegrantes():

	"""Imprime mensaje inicial"""

	print(">Trabajo Practico N° 2 - Analisis Numerico - Curso Tarela - Grupo 6\n")
	print(">Tripulantes abordo:\n")
	print(">Julian Garcia Delfino - 100784\n>Franco Giordano - 100608\n>Agustin Yanuchausky - 99496\n")

def velocidadInicial(R, G = 6.674 * (10 ** -11), M1 = 5972 * (10 ** 21)):

	"""Calcula la velocidad inicial, si se quiere se puede pasar un h0 diferente, y en caso de ser otro planeta un R1 y M1 distintos"""

	return math.sqrt((G * M1) / R)

def periodoAngular(v0, R):

	"""Calcula el periodo ANngular en base al modulo de la velocidad"""

	return (2 * math.pi * R / v0)

def calcularR(R1 = 6.731 * (10 ** 6), h0 = 0.784 * (10 ** 6)):

	"""Calcula, en X, la posicion inicial de la nave"""

	return (R1 + h0)

def posicionInicialX(X1 = -4.67 * (10 ** 6), R1 = 6.731 * (10 ** 6), h0 = 0.784 * (10 ** 6)):

	"""Calcula, en X, la posicion inicial de la nave"""

	return (X1 - R1 - h0)

def condicionesIniciales():

	"""Calcula las condiciones iniciales y las almacena en una lista de 4 elementos"""

	condiciones_0 = {}
	R = calcularR()

	#Se agregan las condiciones triviales

	condiciones_0['Yn'] = 0
	condiciones_0['Vxn'] = 0

	#Se agregan las condiciones no triviales

	condiciones_0['Xn'] = posicionInicialX()
	condiciones_0['Vyn'] = velocidadInicial(R)

	return condiciones_0

def X_n(h, condicionesActuales, counter):

	"""Calcula una iteracion de la ecuacion Xn+1"""

	condicionesActuales[counter]['Xn'] = (condicionesActuales[counter].get('Xn') + h * condicionesActuales[counter].get('Vxn'))

def  Y_n(h, condicionesActuales, counter):

	"""Calcula una iteracion de la ecuacion Yn+1"""

	condicionesActuales[counter]['Yn'] = (condicionesActuales[counter].get('Yn') + h * condicionesActuales[counter].get('Vyn'))

def Vy_n(h, condicionesActuales, counter, M2, w, G = 6.674 * (10 ** -11), M1 = 5972 * (10 ** 21), y1 = 0, x1 = -4.670 * (10 ** 6), y2 = 0, x2 = 379.7 * (10 ** 6)):

	"""Calcula una iteracion de la ecuacion Vx n+1"""

	a1 = math.atan2((y1 - condicionesActuales[counter].get('Yn')), (x1 - condicionesActuales[counter].get('Xn')))

	d1Squared = (x1 - condicionesActuales[counter].get('Xn')) ** 2 + (y1 - condicionesActuales[counter].get('Yn')) ** 2

	fuerzaTerrea = (G * M1 / d1Squared) * math.sin(a1)

	if M2 == 0:

		fuerzaLunar = 0

	else:

		a2 = math.atan2((y2 - condicionesActuales[counter].get('Yn')), (x2 - condicionesActuales[counter].get('Xn')))

		d2Squared = (x2 - condicionesActuales[counter].get('Xn')) ** 2 + (y2 - condicionesActuales[counter].get('Yn')) ** 2

		fuerzaLunar = (G * M2 / d2Squared) * math.sin(a2)

	if w == 0:

		fuerzaCentripeta = 0

	else:

		ac = math.atan2(condicionesActuales[counter].get('Yn'), condicionesActuales[counter].get('Xn'))

		dg = math.sqrt(condicionesActuales[counter].get('Xn') ** 2 + condicionesActuales[counter].get('Yn') ** 2)

		fuerzaCentripeta = (w ** 2) * dg * math.sin(ac)

	condicionesActuales[counter]['Vyn'] = (condicionesActuales[counter].get('Vyn') + h * (fuerzaTerrea + fuerzaLunar + fuerzaCentripeta))

def Vx_n(h, condicionesActuales, counter, M2, w, G = 6.674 * (10 ** -11), M1 = 5972 * (10 ** 21), y1 = 0, x1 = -4.670 * (10 ** 6), y2 = 0, x2 = 379.7 * (10 ** 6)):

	"""Calcula una iteracion de la ecuacion Vx n+1"""

	a1 = math.atan2((y1 - condicionesActuales[counter].get('Yn')), (x1 - condicionesActuales[counter].get('Xn')))

	d1Squared = (x1 - condicionesActuales[counter].get('Xn')) ** 2 + (y1 - condicionesActuales[counter].get('Yn')) ** 2

	fuerzaTerrea = (G * M1 / d1Squared) * math.cos(a1)

	if M2 == 0:

		fuerzaLunar = 0

	else:

		a2 = math.atan2((y2 - condicionesActuales[counter].get('Yn')), (x2 - condicionesActuales[counter].get('Xn')))

		d2Squared = (x2 - condicionesActuales[counter].get('Xn')) ** 2 + (y2 - condicionesActuales[counter].get('Yn')) ** 2

		fuerzaLunar = (G * M2 / d2Squared) * math.cos(a2)

	if w == 0:

		fuerzaCentripeta = 0

	else:

		ac = math.atan2(condicionesActuales[counter].get('Yn'), condicionesActuales[counter].get('Xn'))

		dg = math.sqrt(condicionesActuales[counter].get('Xn') ** 2 + condicionesActuales[counter].get('Yn') ** 2)

		fuerzaCentripeta = (w ** 2) * dg * math.cos(ac)

	condicionesActuales[counter]['Vxn'] = (condicionesActuales[counter].get('Vxn') + h * (fuerzaTerrea + fuerzaLunar + fuerzaCentripeta))

def generarTierra(r1 = 6.731 * (10 ** 6), x1 = -4.670 * (10 ** 6)):

	x = []
	y = []

	counter = 0

	for angulo in range(0, 360, 1):

		x.append(r1 * (math.cos(angulo * math.pi / 180)))
		x[counter] += x1
		y.append(r1 * (math.sin(angulo * math.pi / 180)))

		counter += 1

	tierra = [x, y]

	return tierra

def eulerExplicito(condiciones_0, v0, R, M2 = 73.48 * (10 ** 21), w = 4.236 * (10 ** -7)):

	"""Metodo de resolucion de euler de forma explicita"""

	condicionesActuales = [condiciones_0]
	counter = 0

	#Se inicializan las condiciones actuales en las iniciales y se crea el diccionario que luego se implementara

	T = periodoAngular(v0, R)
	print('El periodo es: ' + str(T))

	h = int(input('Ingrese un valor  de paso: '))
	print('\n')

	aux = condicionesActuales[counter].copy()

	condicionesActuales.append(aux)

	counter += 1

	Vx_n(h, condicionesActuales, counter, M2, w)
	Vy_n(h, condicionesActuales, counter, M2, w)
	X_n(h, condicionesActuales, counter)
	Y_n(h, condicionesActuales, counter)

	while((counter * h) < 10 * T):

		aux = condicionesActuales[counter].copy()

		condicionesActuales.append(aux)

		counter += 1

		Vx_n(h, condicionesActuales, counter, M2, w)
		Vy_n(h, condicionesActuales, counter, M2, w)
		X_n(h, condicionesActuales, counter)
		Y_n(h, condicionesActuales, counter)

	x = [condicionesActuales[i].get('Xn') for i in range(0, len(condicionesActuales))]
	y = [condicionesActuales[i].get('Yn') for i in range(0, len(condicionesActuales))]

	tierra = generarTierra()

	plt.axis('equal')

	plt.plot(tierra[0], tierra[1], label = 'Tierra', color = 'blue')
	plt.plot(x, y, label = 'Trayecto', color = 'black')

	plt.legend(bbox_to_anchor = (0., 1.02, 1., .102), loc = 3, ncol = 2, mode = "expand", borderaxespad = 0.)

	plt.show()

def main():

	condiciones_0 = condicionesIniciales()

	opcion = int(input('>Ingrese 1 para probar la orbita terrestre \n>Ingrese 2 para probar la orbita terrestre - lunar\n Opcion: '))

	if opcion == 1:

		M2 = 0
		w = 0

		R = calcularR()

		v0 = velocidadInicial(R)
		print('La velocidad inicial es: ' + str(v0))

		eulerExplicito(condiciones_0, v0, R, M2, w)

	elif opcion == 2:

		v0 =int(input('Ingrese una velocidad inicial para el problema, 0 para finalizar \n Opcion: '))

		if v0 != 0: 

			while v0 != 0:

				R = calcularR()

				eulerExplicito(condiciones_0, v0, R)

				v0 = int(input('Ingrese una velocidad inicial para el problema, 0 para finalizar \n Opcion: '))
	
		print('Programa Finalizado')

	else:

		print('Opcion incorrecta')

main()


















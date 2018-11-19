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

def velocidadInicial(G = 6.674 * (10 ** -11), R, M1 = 5972 * (10 ** 21)):

	"""Calcula la velocidad inicial, si se quiere se puede pasar un h0 diferente, y en caso de ser otro planeta un R1 y M1 distintos"""

	return sqrt((G * M1) / (R))

def periodoAngular(v0, R):

	"""Calcula el periodo ANngular en base al modulo de la velocidad"""

	return (2 * math.pi / v0)

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

def X_n(h, condicionesActuales):

	"""Calcula una iteracion de la ecuacion Xn+1"""

	condicionesActuales['Xn'] = (condicionesActuales.get('Xn') + h * condicionesActuales.get('Vxn'))

def  Y_n(h, condicionesActuales):

	"""Calcula una iteracion de la ecuacion Yn+1"""

	condicionesActuales['Yn'] = (condicionesActuales.get('Yn') + h * condicionesActuales.get('Vyn'))

def Vy_n(h, G = 6.674 * (10 ** -11), M1 = 5972 * (10 ** 21), y1 = 0, x1 = -4.670 * (10 ** 6), condicionesActuales):

	"""Calcula una iteracion de la ecuacion Vx n+1"""

	a1 = math.atan((y1 - condicionesActuales.get('yn')) / (x1 - condicionesActuales.get('xn')))

	d1Squared = (x1 - condicionesActuales.get('xn')) ** 2 + (y1 - condicionesActuales.get('yn')) ** 2

	fuerzaTerrea = (G * M1 / d1Squared) * math.sin(a1)

	if M2 == 0:

		fuerzaLunar = 0

	else:

		a2 = math.atan((y2 - condicionesActuales.get('yn')) / (x2 - condicionesActuales.get('xn')))

		d2Squared = (x2 - condicionesActuales.get('xn')) ** 2 + (y2 - condicionesActuales.get('yn')) ** 2

		fuerzaLunar = (G * M2 / d2Squared) * math.sin(a2)

	if w == 0:

		fuerzaCentripeta = 0

	else:

		ac = math.atan(condicionesActuales.get('yn') / condicionesIniciales.get('xn'))

		dg = sqrt(condicionesActuales.get('xn') ** 2 + condicionesActuales.get('yn') ** 2)

		fuerzaCentripeta = (w ** 2) * dg * math.sin(ac)

	condicionesActuales['Vyn'] = (fuerzaTerrea + fuerzaLunar + fuerzaCentripeta)

def Vx_n(h, G = 6.674 * (10 ** -11), M1 = 5972 * (10 ** 21), M2 = 0, w = 0, y1 = 0, x1 = -4.670 * (10 ** 6), y2 = 0, x2 = 379.7 * (10 ** 6), condicionesActuales):

	"""Calcula una iteracion de la ecuacion Vx n+1"""

	a1 = math.atan((y1 - condicionesActuales.get('yn')) / (x1 - condicionesActuales.get('xn')))

	d1Squared = (x1 - condicionesActuales.get('xn')) ** 2 + (y1 - condicionesActuales.get('yn')) ** 2

	fuerzaTerrea = (G * M1 / d1Squared) * math.cos(a1)

	if M2 == 0:

		fuerzaLunar = 0

	else:

		a2 = math.atan((y2 - condicionesActuales.get('yn')) / (x2 - condicionesActuales.get('xn')))

		d2Squared = (x2 - condicionesActuales.get('xn')) ** 2 + (y2 - condicionesActuales.get('yn')) ** 2

		fuerzaLunar = (G * M2 / d2Squared) * math.cos(a2)

	if w == 0:

		fuerzaCentripeta = 0

	else:

		ac = math.atan(condicionesActuales.get('yn') / condicionesIniciales.get('xn'))

		dg = sqrt(condicionesActuales.get('xn') ** 2 + condicionesActuales.get('yn') ** 2)

		fuerzaCentripeta = (w ** 2) * dg * math.cos(ac)

	condicionesActuales['Vxn'] = (fuerzaTerrea + fuerzaLunar + fuerzaCentripeta)

def eulerExplicito(condiciones_0):

	"""Metodo de resolucion de euler de forma explicita"""

	#h = comprobarEstabilidad()
	#Hay que ver como codear esa funcion, primero quiero entender como hacerlo en lapiz y papel :D

	condicionesActuales = [condicionesIniciales()]
	counter = 0

	"""Se inicializan las condiciones actuales en las iniciales y se crea el diccionario que luego se implementara"""

	R = posicionInicialX()

	v0 = velocidadInicial(R)
	print('La velocidad inicial es:' + str(v0))

	T = periodoAngular(v0, R)
	print('El periodo es:' + str(T))

	












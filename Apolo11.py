"""Trabajo Practico N° 2 - Analisis Numerico - Curso Tarela - Grupo 6"""

#Miercoles 18 de Noviembre

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

def condicionesIniciales(V_dada):

	"""Calcula las condiciones iniciales y las almacena en una lista de 4 elementos"""

	condiciones_0 = {}
	R = calcularR()

	#Se agregan las condiciones triviales

	condiciones_0['Yn'] = 0
	condiciones_0['Vxn'] = 0

	#Se agregan las condiciones no triviales

	condiciones_0['Xn'] = posicionInicialX()

	if V_dada is 0:
		condiciones_0['Vyn'] = velocidadInicial(R)

	else:
		condiciones_0['Vyn'] = V_dada

	return condiciones_0

def X_n(h, condicionesActuales, counter):

	"""Calcula una iteracion de la ecuacion Xn+1"""

	condicionesActuales[counter]['Xn'] = (condicionesActuales[counter].get('Xn') + h * condicionesActuales[counter].get('Vxn'))

def  Y_n(h, condicionesActuales, counter):

	"""Calcula una iteracion de la ecuacion Yn+1"""

	condicionesActuales[counter]['Yn'] = (condicionesActuales[counter].get('Yn') + h * condicionesActuales[counter].get('Vyn'))

def Vy_n(h, condicionesActuales, counter, M2, w, RK = False, G = 6.674 * (10 ** -11), M1 = 5972 * (10 ** 21), y1 = 0, x1 = -4.670 * (10 ** 6), y2 = 0, x2 = 379.7 * (10 ** 6)):

	"""Calcula una iteracion de la ecuacion Vx n+1"""

	a1 = math.atan2((y1 - condicionesActuales[counter].get('Yn')), (x1 - condicionesActuales[counter].get('Xn')))

	d1Squared = dSquared(condicionesActuales[counter], estaTierra = True)

	fuerzaTerrea = (G * M1 / d1Squared) * math.sin(a1)

	if M2 is 0:

		fuerzaLunar = 0

	else:

		a2 = math.atan2((y2 - condicionesActuales[counter].get('Yn')), (x2 - condicionesActuales[counter].get('Xn')))

		d2Squared = dSquared(condicionesActuales[counter], estaLuna = True)

		fuerzaLunar = (G * M2 / d2Squared) * math.sin(a2)

	if w is 0:

		fuerzaCentripeta = 0

	else:

		ac = math.atan2(condicionesActuales[counter].get('Yn'), condicionesActuales[counter].get('Xn'))

		dg = math.sqrt(condicionesActuales[counter].get('Xn') ** 2 + condicionesActuales[counter].get('Yn') ** 2)

		fuerzaCentripeta = (w ** 2) * dg * math.sin(ac)

	Vy = (fuerzaTerrea + fuerzaLunar + fuerzaCentripeta)

	if RK is False:

		condicionesActuales[counter]['Vyn'] = condicionesActuales[counter].get('Vyn') + h * Vy

	else:

		return Vy

def Vx_n(h, condicionesActuales, counter, M2, w, RK = False, G = 6.674 * (10 ** -11), M1 = 5972 * (10 ** 21), y1 = 0, x1 = -4.670 * (10 ** 6), y2 = 0, x2 = 379.7 * (10 ** 6)):

	"""Calcula una iteracion de la ecuacion Vx n+1"""

	a1 = math.atan2((y1 - condicionesActuales[counter].get('Yn')), (x1 - condicionesActuales[counter].get('Xn')))

	d1Squared = dSquared(condicionesActuales[counter], estaTierra = True)

	fuerzaTerrea = (G * M1 / d1Squared) * math.cos(a1)

	if M2 is 0:

		fuerzaLunar = 0

	else:

		a2 = math.atan2((y2 - condicionesActuales[counter].get('Yn')), (x2 - condicionesActuales[counter].get('Xn')))

		d2Squared = dSquared(condicionesActuales[counter], estaLuna = True)

		fuerzaLunar = (G * M2 / d2Squared) * math.cos(a2)

	if w is 0:

		fuerzaCentripeta = 0

	else:

		ac = math.atan2(condicionesActuales[counter].get('Yn'), condicionesActuales[counter].get('Xn'))

		dg = math.sqrt(condicionesActuales[counter].get('Xn') ** 2 + condicionesActuales[counter].get('Yn') ** 2)

		fuerzaCentripeta = (w ** 2) * dg * math.cos(ac)

	Vx = (fuerzaTerrea + fuerzaLunar + fuerzaCentripeta)

	if RK is False:	

		condicionesActuales[counter]['Vxn'] = condicionesActuales[counter].get('Vxn') + h * Vx

	else:

		return Vx


def dSquared(condicion, estaTierra = False, estaLuna = False, y1 = 0, x1 = -4.670 * (10 ** 6), y2 = 0, x2 = 379.7 * (10 ** 6)):

	"""Calcula la distancia al cuadrado entre la nave espacial y tanto la tierra como la luna, a eleccion"""

	if estaTierra is True:
		dSquared = (x1 - condicion.get('Xn')) ** 2 + (y1 - condicion.get('Yn')) ** 2

	if estaLuna is True:
		dSquared = (x2 - condicion.get('Xn')) ** 2 + (y2 - condicion.get('Yn')) ** 2

	return dSquared

def generarTierra(r1 = 6.731 * (10 ** 6), x1 = -4.670 * (10 ** 6)):

	"""Genera los puntos pertenecientes a la grafia de la tierra"""

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

def generarLuna(r2 = 1.738 * (10 ** 6), x2 = 379.7 * (10 ** 6)):

	"""Genera los puntos pertenecientes a la grafia de la luna"""

	x = []
	y = []

	counter = 0

	for angulo in range(0, 360, 1):

		x.append(r2 * (math.cos(angulo * math.pi / 180)))
		x[counter] += x2
		y.append(r2 * (math.sin(angulo * math.pi / 180)))

		counter += 1

	luna = [x, y]

	return luna

def generarTrayectoria(condicionesActuales):

	"""Genera los vectores de posicion, con coordenadas x e y, de la trayctoria"""

	Tx = [condicionesActuales[i].get('Xn') for i in range(0, len(condicionesActuales))]
	Ty = [condicionesActuales[i].get('Yn') for i in range(0, len(condicionesActuales))]

	return [Tx, Ty]

def iterarEuler(h, condicionesActuales, counter, M2, w):

	"""Funcion para iterar con Euler"""

	Vx_n(h, condicionesActuales, counter, M2, w)
	Vy_n(h, condicionesActuales, counter, M2, w)
	X_n(h, condicionesActuales, counter)
	Y_n(h, condicionesActuales, counter)

def plotTrayectoria(trayectoria, estaLuna = False):

	"""Funcion para plotear todos los datos"""

	plt.axis('equal')

	tierra = generarTierra()
	plt.plot(tierra[0], tierra[1], label = 'Tierra', color = 'blue')

	if estaLuna is True:
		luna = generarLuna()
		plt.plot(luna[0], luna[1], label = 'Luna', color = 'grey')

	plt.plot(trayectoria[0], trayectoria[1], label = 'Trayecto', color = 'black')

	plt.legend(bbox_to_anchor = (0., 1.02, 1., .102), loc = 3, ncol = 2, mode = "expand", borderaxespad = 0.)

	plt.show()

def eulerExplicito(condicionesActuales, v0, M2 = 73.48 * (10 ** 21), w = 4.236 * (10 ** -7)):

	"""Resolucion mediante Euler Explicito"""

	#Se inicializan las condiciones actuales en las iniciales y se crea el diccionario que luego se implementara

	condicionesActuales.append(condicionesIniciales(V_dada = v0))

	counter = 0
	rotation = False
	isOnReach = True
	R = calcularR()

	#Se chequea si la luna esta presente mediante el valor de su masa M2

	h = float(input('>>Ingrese un valor de paso: '))
	print('\n')

	if h <= 0:
		print('>>>Paso Incorrecto')
		return False

	tierra = generarTierra()

	aux = condicionesActuales[counter].copy()

	condicionesActuales.append(aux)

	counter += 1

	iterarEuler(h, condicionesActuales, counter, M2, w)

	while rotation != True & isOnReach :

		aux = condicionesActuales[counter].copy()

		condicionesActuales.append(aux)

		counter += 1
		
		iterarEuler(h, condicionesActuales, counter, M2, w)

		if areWeDeadYet(condicionesActuales[counter]):
			print('>>>>>>>>La nave se estrello!<<<<<<<<\n')
			break

		if fullRotationCheck(condicionesActuales, counter):
			print('>>>>>>>>Orbita completada!<<<<<<<<\n')
			rotation = True

		if onReach(condicionesActuales[counter]) is False:
			print('>>>>>>>>Fuera de alcance<<<<<<<<')
			print('>>>>>>>>Perdimos la nave<<<<<<<<')
			print('>>>>>>>>Notifique a los familiares de los tripulantes<<<<<<<<\n')
			isOnReach = False
		
	printBitacora(condicionesActuales[0], h, counter)

	trayectoria = generarTrayectoria(condicionesActuales)

	if M2 is 0:
		plotTrayectoria(trayectoria)

	else:
		plotTrayectoria(trayectoria, estaLuna = True)

	return True

def printBitacora(condiciones_0, h, counter):

	print('\n')
	print('>Velocidad de partida: %.2f m/s' % condiciones_0.get('Vyn'))
	print('>Se tardo en completar la orbita: %.2f segundos o %.2f dias.' % (h * counter, h * counter / 3600))
	print('\n')

def onReach(condicion, x1 = -4.670 * (10 ** 6), x2 = 379.7 * (10 ** 6)):

	"""Se encarga de verificar que la nave siga dentro de un rango aceptable"""

	distanciaEntreLunaYTierra = x2 - x1

	if dSquared(condicion, estaTierra = True) ** 0.5 >= 1.5 * distanciaEntreLunaYTierra:
		return False

	return True

def energiaTotal(condicionesActuales, estaLuna = False):

	"""Se calcula la energia total y se grafica"""

	if estaLuna is True:
		energiaPotencialTotal = [energiaPotencial(condicionesActuales[i]) for i in range(0, len(condicionesActuales))]

	else:
		energiaPotencialTotal = [energiaPotencial(condicionesActuales[i], M2 = 0) for i in range(0, len(condicionesActuales))]

	energiaCineticaTotal = [energiaCinetica(condicionesActuales[i]) for i in range(0, len(condicionesActuales))]
	energiaMecanicaTotal = [energiaCineticaTotal[i] + energiaPotencialTotal[i] for i in range(0, len(condicionesActuales))]

	plotEnergia(energiaCineticaTotal, energiaPotencialTotal, energiaMecanicaTotal)

def plotEnergia(energiaCineticaTotal, energiaPotencialTotal, energiaMecanicaTotal):

	"""Se encarga de graficar todas las energias juntas"""

	plt.plot(energiaCineticaTotal, label = 'Energia Cinetica', color = 'red')
	plt.plot(energiaPotencialTotal, label = 'Energia Potencial', color = 'green')
	plt.plot(energiaMecanicaTotal, label = 'Energia Mecanica', color = 'blue')

	plt.legend(bbox_to_anchor = (0., 1.02, 1., .102), loc = 3, ncol = 2, mode = "expand", borderaxespad = 0.)

	plt.show()

def energiaCinetica(condicion):

	"""Calculo de la energia cinetica"""

	return 0.5 * (moduloVelocidad(condicion.get('Vxn'), condicion.get('Vyn')) ** 2)

def energiaPotencial(condicion, G = 6.674 * (10 ** -11), M1 = 5972 * (10 ** 21), M2 = 73.48 * (10 ** 21)):

	"""Calculo de la energia potencial"""

	energiaPotencial = -G * M1 / (dSquared(condicion, estaTierra = True) ** 0.5)

	if M2 != 0:

		energiaPotencial += -G * M2 / (dSquared(condicion, estaLuna = True) ** 0.5)

	return energiaPotencial

def moduloVelocidad(Vxn, Vyn):

	"""Calcula el modulo de la velocidad dado que tiene 2 componentes"""

	return math.sqrt(Vxn ** 2 + Vyn ** 2)

def areWeDeadYet(condicion, r1 = 6.731 * (10 ** 6), r2 = 1.738 * (10 ** 6)):

	"""Verifica si la nave choco, para asi, frenar la simulacion"""

	if (dSquared(condicion, estaLuna = True) ** 0.5 <= r2) | (dSquared(condicion, estaTierra = True) ** 0.5 <= r1):
		return True

	else:		
		return False

def fullRotationCheck(condicionesActuales, counter, x1 = -4.670 * (10 ** 6)):

	"""Verifica segun la rotacion de la nave si esta ha completado un ciclo 
	   (considerando una "orbita" una vuelta completa volviendo al punto de salida"""

	for division in range(1, 5):

		y = (condicionesActuales[counter].get('Yn') + condicionesActuales[counter - 1].get('Yn')) / division
		x = (condicionesActuales[counter].get('Xn') + condicionesActuales[counter - 1].get('Xn')) / division

		fase = math.atan2(y, x - x1)

		anterior = condicionesActuales[counter - 1].get('Yn')
		actual = condicionesActuales[counter].get('Yn')

		if (fase > -math.pi) & (fase < -3.13) & (anterior < 0) & (actual > anterior):
			return True 

	return False

def rocket():

	print('\n')
	print('         /\\')
	print('        /  \\')
	print('       /    \\')
	print('      /      \\')
	print('     /        \\')
	print('    /          \\')
	print('    ------------')
	print('    |    ()    |')
	print('   /|          |\\')
	print('  / |    ()    | \\')
	print(' /  |          |  \\')
	print(' ---|    ()    |---')
	print('    ------------')
	print('      |      |')
	print('      \\/\\/\\/\\/')
	print('    \\/\\/\\/\\/\\/\\/')
	print('  \\/\\/\\/\\/\\/\\/\\/\\/')
	print('\n>Gracias por volar con nosotros!\n>>Esperamos que no se haya estrellado\n')

def rungeKutta2(condicionesActuales, v0, M2 = 73.48 * (10 ** 21), w = 4.236 * (10 ** -7)):

	"""Resolucion mediante Runge Kutta de orden 2"""

	#Se inicializan las condiciones actuales en las iniciales y se crea el diccionario que luego se implementara

	condicionesActuales.append(condicionesIniciales(V_dada = v0))

	counter = 0
	rotation = False
	isOnReach = True
	R = calcularR()

	h = float(input('>>Ingrese un valor de paso: '))
	print('\n')

	if h <= 0:
		print('>>>Paso Incorrecto')
		return False

	while rotation != True & isOnReach :

		aux = condicionesActuales[counter].copy()

		condicionesActuales.append(aux)

		counter += 1
		
		iterarRK2(condicionesActuales, counter, h, M2, w)

		if areWeDeadYet(condicionesActuales[counter]):
			print('>>>>>>>>La nave se estrello!<<<<<<<<\n')
			break

		if fullRotationCheck(condicionesActuales, counter):
			print('>>>>>>>>Orbita completada!<<<<<<<<\n')
			rotation = True

		if onReach(condicionesActuales[counter]) is False:
			print('>>>>>>>>Fuera de alcance<<<<<<<<')
			print('>>>>>>>>Perdimos la nave<<<<<<<<')
			print('>>>>>>>>Notifique a los familiares de los tripulantes<<<<<<<<\n')
			isOnReach = False
		
	printBitacora(condicionesActuales[0], h, counter)

	trayectoria = generarTrayectoria(condicionesActuales)

	if M2 is 0:
		plotTrayectoria(trayectoria)

	else:
		plotTrayectoria(trayectoria, estaLuna = True)

	return True

def iterarRK2(condicionesActuales, counter, h, M2, w):

	r1 = h * condicionesActuales[counter].get('Vxn') #m
	s1 = h * condicionesActuales[counter].get('Vyn') #m
	q1 = h * Vx_n(h, condicionesActuales, counter, M2, w, RK = True) #m/S
	p1 = h * Vy_n(h, condicionesActuales, counter, M2, w, RK = True) #m/s

	condicionesActuales[counter]['Xn'] = condicionesActuales[counter].get('Xn') + r1
	condicionesActuales[counter]['Yn'] = condicionesActuales[counter].get('Yn') + s1
	condicionesActuales[counter]['Vxn'] = condicionesActuales[counter].get('Vxn') + q1
	condicionesActuales[counter]['Vyn'] = condicionesActuales[counter].get('Vyn') + p1

	r2 = h * condicionesActuales[counter].get('Vxn')
	s2 = h * condicionesActuales[counter].get('Vyn')
	q2 = h * Vx_n(h, condicionesActuales, counter, M2, w, RK = True)
	p2 = h * Vy_n(h, condicionesActuales, counter, M2, w, RK = True)

	condicionesActuales[counter]['Xn'] = condicionesActuales[counter].get('Xn') - r1
	condicionesActuales[counter]['Yn'] = condicionesActuales[counter].get('Yn') - s1
	condicionesActuales[counter]['Vxn'] = condicionesActuales[counter].get('Vxn') - q1
	condicionesActuales[counter]['Vyn'] = condicionesActuales[counter].get('Vyn') - p1

	condicionesActuales[counter]['Xn'] = condicionesActuales[counter].get('Xn') + 0.5 * (r1 + r2)
	condicionesActuales[counter]['Yn'] = condicionesActuales[counter].get('Yn') + 0.5 * (s1 + s2)
	condicionesActuales[counter]['Vxn'] = condicionesActuales[counter].get('Vxn') + 0.5 * (q1 + q2)
	condicionesActuales[counter]['Vyn'] = condicionesActuales[counter].get('Vyn') + 0.5 * (p1 + p2)

def opcionEuler():

	opcion = int(input('>Ingrese 1 para probar la orbita terrestre \n>Ingrese 2 para probar la orbita terrestre - lunar\n\n>Opcion: '))

	if opcion is 1:

		condicionesActuales = []

		#Se indica, con v0 = 0, que se debe calcular la velocidad inicial

		v0 = 0 

		print('\nSIMULACION DE ORBITA TERRESTRE\n')

		if eulerExplicito(condicionesActuales, v0, M2 = 0, w = 0):

			energiaTotal(condicionesActuales)

			print('>Se termino la simulacion!')

		else:
			print('>Fracaso en la simulacion.')

	elif opcion is 2:

		print('\nSIMULACION DE ORBITA TERRESTRE - LUNAR.\n')

		v0 = float(input('>Ingrese una velocidad inicial para el problema, 0 para finalizar.\n\n>Opcion: '))

		if v0 != 0: 

			while v0 != 0:

				condicionesActuales = []

				if eulerExplicito(condicionesActuales, v0):

					energiaTotal(condicionesActuales, estaLuna = True)

					print('>Se termino la simulacion!')

				else:
					print('>Fracaso en la simulacion')

				v0 = float(input('>Ingrese una velocidad inicial para el problema, 0 para finalizar.\n>Opcion: '))
	
		print('>Se termino la simulacion!')

def opcionRK():

	opcion = int(input('>Ingrese 1 para probar la orbita terrestre \n>Ingrese 2 para probar la orbita terrestre - lunar\n\n>Opcion: '))

	if opcion is 1:

		condicionesActuales = []

		#Se indica, con v0 = 0, que se debe calcular la velocidad inicial

		v0 = 0 

		print('\nSIMULACION DE ORBITA TERRESTRE\n')

		if rungeKutta2(condicionesActuales, v0, M2 = 0, w = 0):

			energiaTotal(condicionesActuales)

			print('>Se termino la simulacion!')

		else:
			print('>Fracaso en la simulacion.')

	elif opcion is 2:

		print('\nSIMULACION DE ORBITA TERRESTRE - LUNAR.\n')

		v0 = float(input('>Ingrese una velocidad inicial para el problema, 0 para finalizar.\n\n>Opcion: '))

		if v0 != 0: 

			while v0 != 0:

				condicionesActuales = []

				if rungeKutta2(condicionesActuales, v0):

					energiaTotal(condicionesActuales, estaLuna = True)

					print('>Se termino la simulacion!')

				else:
					print('>Fracaso en la simulacion')

				v0 = float(input('>Ingrese una velocidad inicial para el problema, 0 para finalizar.\n>Opcion: '))
	
		print('>Se termino la simulacion!')

def main():

	printIntegrantes()

	opcion = int(input('>Ingrese 1 para simular con Euler explicito \n>Ingrese 2 para simular con Runge Kutta de orden 2\n\n>Opcion: '))

	if opcion is 1:

		opcionEuler()
		rocket()

	elif opcion is 2:

		opcionRK()
		rocket()

	else:

		print('Opcion incorrecta')

main()
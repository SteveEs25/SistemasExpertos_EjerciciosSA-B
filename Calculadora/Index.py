#Importamos la clase Calcu
from Calculadora import Calcu

#La variable recoge los datos de la clase Calcu
calcu = Calcu()


def Menu():
	print(" ")
	print(" ")
	print("--CALCULADORA--")
	print(" ")
	print("Seleccione una opción")
	print("1 - Suma")
	print("2 - Resta")
	print("3 - Multiplicación")
	print("4 - División")
	print("5 - Raiz Cuadrada")
	print("6 - Elevación")
	print("0 - Salir")
	return int(input("Introducir opción: "))


while(True):
	opcion = Menu()

	if(opcion == 0):
		break	
	else:
		num1 = float(input("Digite el primer número: "))

		if(opcion != 5):
			if(opcion != 6):
				num2 = float(input("Digite el segundo número: "))
			else:
				num2 = float(input("Digite el valor de la elevación: "))


		#Llamando a las funciones dependiendo de la opcion seleccionada
		if(opcion == 1):
			calcu.Suma(num1, num2)

		elif(opcion == 2):
			calcu.Resta(num1, num2)

		elif(opcion == 3):
			calcu.Multi(num1, num2)

		elif(opcion == 4):
			if(num2 == 0):
				print("No se puede dividir entre 0")
			else:
				calcu.Division(num1, num2)

		elif(opcion == 5):
			calcu.Raiz(num1)

		elif(opcion == 6):
			calcu.Elevacion(num1, num2)

		else:
			print("Opción incorrecta")


print("ADIOS !!!")
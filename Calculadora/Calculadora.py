#Libreria para operaciones matemáticas
import math

class Calcu:

	def Suma(self, num1, num2):
		print(str(num1) + " + " + str(num2) + " = " + str(num1+num2))


	def Resta(self, num1, num2):
		print(str(num1) + " - " + str(num2) + " = " + str(num1-num2))


	def Multi(self, num1, num2):
		print(str(num1) + " X " + str(num2) + " = " + str(num1*num2))


	def Division(self, num1, num2):
		print(str(num1) + " / " + str(num2) + " = " + str(num1/num2))


	def Raiz(self, num1):
		print("La Raíz Cuadrada de " + str(num1) + " es = " + str(math.sqrt(num1)))


	def Elevacion(self, num1, num2):
		print("Elevar " + str(num1) + " a la " + str(num2) + " es = " + str(num1 ** num2))


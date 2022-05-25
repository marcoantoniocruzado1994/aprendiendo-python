""" def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
	try:		
		return num1/num2
	except ZeroDivisionError:
		return "No se puede dividir entre 0"
		
	
while True: # Se ejecuta siempre y cuando sea verdadero como es true entonces entra en un bucle infinito hasta que se cierre la condicion
	try:
		op1=(int(input("Introduce el primer numero: ")))
		op2=(int(input("Introduce el segundo numero: ")))
		break
	except ValueError:
		print("El valor introducido no es valido")


operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacon de ejecucion del programa ") """

def divide():
	try:
		op1 = (float(input("Introduce el primer numero: ")))
		op2 = (float(input("Introduce el segundo numero: ")))
		print("La division es: ", str(op1/op2))
	except ValueError:
		print("El valor introduciod no es valido")
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
	finally:
		print("Operacion finalizada")

divide()
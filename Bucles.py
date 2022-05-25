""" #bucle for 
for letra in  "Marco":
    if letra == "a":
        continue # salta el siguiente paso del bucle
    print(letra) #osea en este caso salta la letra a

print("---------------------------------")
#contar cuantos caracteres iguales hay en una cadena
cadena = "Hola mama soy marco"
cont = 0
for letra in cadena:
    if letra == "a":
        cont += 1
        continue
    print(letra)

print("Hay", cont, "letras a")
print("---------------------------------")
 """

print("---------------------------------")
class MiClase:
    pass #es una clase vacia y se puede implementar mas tarde y hace como que si no existiese
email = input("Introduce tu email: ")
for letra in email:
    if letra == "@":
        arroba = True
        break
else:
    arroba = False

print("El email tiene arroba ? :", arroba)
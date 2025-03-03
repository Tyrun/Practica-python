print("Hello CodeSandbox!")
print("Samuel")
print("Dulce")
print("Carlos")
print("Kevin Cortez")
print("Alejandro")
print("Vania Castrejon")
print("Fernando Agular sisneros")
print("Karina Noemi Pastrana")
print("Karina Maldonado Procopio")

""" Vamos a cocadenar """
nombre = "Kevin Cortez"
apellido = "Luciano"
print("Hola mi nombre es: ",nombre)
print("Hola, mi nombre es: ",nombre, apellido)#Hola mi nombre es: Kevin
print("Hola mi nombre es: ",nombre, "y mi apellido es:", apellido)#Hola mi nombre es: Kevin y mi apellido es: Luciano

""" Concatenación con diferentes tipos de datos """
mi_edad=19
mi_nombre="Kevin Cortez"
mi_apellido_paterno="Luciano"
mi_apellido_materno="Garcia"
soy_estudiante= True
soy_maestro= False

print("mi nombre es: ",mi_nombre, "mi apellido paterno es: ",mi_apellido_paterno, "mi apellido materno es: ", mi_apellido_materno, "mi edad es: ",mi_edad, "soy estudiante: ", soy_estudiante, "Soy maestro:", soy_maestro)

""" Uso de type - Averigua que tipo de dato recibes """
print(type(mi_edad)) # <class 'int'>
print(type(mi_nombre)) #<class 'str'>
print(type(soy_estudiante)) #<class 'bool'>


""" Operaciones matematicas """
numero_uno=78
numero_dos=87

print(numero_uno+numero_dos)
print(numero_uno-numero_dos)
print(numero_uno*numero_dos)
print(numero_uno/numero_dos)
print(numero_uno%numero_dos)




print("Dime tu nombre")
nombre = input()
print("El nombre que escribiste es: ", nombre)

print("Dime cuantos años tienes")
edad = input()
print("La edad que ingresaste es: ", edad)

print("Dime cuales son tus apellidos")
apellidos = input()
print("Los apellidos que ingresaste son:", apellidos)

print("¿Eres un estudiante?")
estudiante = input()
print(estudiante, "eres un estudiante")

print("¿Eres un maestro?")
maestro = input()
print(maestro, "eres un maestro")

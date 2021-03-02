# print()   # Imprimir en pantalla
# dir()     # Información de un dato
# type()    # Tipo de dato

#Definir función

# def hello(name="Person"):
#     print("Hello " + name)

# hello("joe")
# hello("ryan")
# hello()

# def add(numberOne, numberTwo):
#     return numberOne + numberTwo

# print(add(10, 30))

add = lambda numberOne, numberTwo: numberOne + numberTwo

print(add(10,30))
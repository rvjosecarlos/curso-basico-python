# String = Cadena de texto
nombre = "Carlos 😁"

# Enteros = Numeros sin punto decimal

edad = 30

print(nombre,edad)

# Casteo =  transformar un tipo de variable a otro

try:
    edad = float(edad)
    print(edad)
except:
    print("No se puede castear")

# Type es para saber el tipo de dato

print(type(nombre), type(edad))

# Bool =  Booleano = SI o No
legustas = True
print(legustas)
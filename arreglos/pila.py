# Pila en python
# El ultimo elemento que entra es el primer elemento que sale

pila = [1,2,3,4,5]

pila.append(6)
pila.append(7)

print(pila)

print(pila.pop()) # Extrae el ultimo elemento de la pila
print(pila)

print(pila.pop())
print(pila)
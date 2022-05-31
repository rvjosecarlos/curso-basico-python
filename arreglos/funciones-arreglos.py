# Arreglo o lista
lista = [1,2,3,4,5]

lista.append(9) #append agrega un elemento en la ultima posicion de la lista
print(lista)

lista.extend(lista) #extiende una lista a otra lista o podemos agregar algo iterable
print(lista)


lista = lista[::-1] # Indica que va a contar la lista del ultimo elemento al primero
print(lista) 

lista.reverse() #para revertir los elementos de la lista
print(lista)

lista.insert(0,900) # Inserta un elemento en una posicion especifica
lista.insert(9,34)
print(lista)

lista.remove(9) # Remueve un elemento de la lista que coincida con el parametro
print(lista)

lista.pop() # El pop quita un elemento de la lista en la posicion dada y lo recupera

print(lista.pop(1))
print(lista)

print(lista.count(3)) #Cuenta las veces que aparece un elemento en la lista que pasas como parametro

print(lista.index(5)) # Devuelve la posicion del elemento en la lista que buscas como parametro 

lista.sort() # Ordena la lista ascendentemente
print(lista)

lista.sort(reverse=True) # Ordenar descendentemente
print(lista)

lista1 = lista.copy() # copiar una lista. Es una copia superficial, solo copia los elementos base
print(lista1)

lista.clear() #Limpia la lista, quita todos los elementos de la lista
print(lista)

calificacion = int(input("Introduce la calificacion de la AZ.900\n"))

if calificacion < 700:
    print("No obtuviste el puntaje minimo aprobatorio")
elif calificacion > 1000:
    print("No mientas")
else:
    print("Felicidades, aprobaste el examen de certificación")



####### Verificar mayoria de edad #######
edad = int(input("Introduce tu edad\n"))

if edad >=18 and edad <=100:
    print("Bienvenido al mamitas")
elif edad > 100:
    print("Solo se fia a personas mayores de 90 años acompañados de sus abuelos")
elif edad < 0:
    print("Ni que fueras viajero en el tiempo")
else:
    print("No puedes llevar bebidas alcoholicas o cigarrillos")


# En python no hay switch-case
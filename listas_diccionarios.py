# Lista de nombres de estudiantes
estudiantes = ["Ana", "Luis", "Sofía", "Carlos"]
print("Lista de estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

# Diccionario de información de contacto
contacto = {"nombre": "María", "correo": "maria@example.com"}
print("Información de contacto:")
for clave, valor in contacto.items():
    print(clave, ":", valor)

# Script para agregar elementos a una lista
nueva_lista = []
while True:
    dato = input("Agrega un elemento a la lista (o escribe 'salir' para terminar): ")
    if dato.lower() == "salir":
        break
    nueva_lista.append(dato)

print("Lista final:", nueva_lista)

# Script para actualizar un diccionario
persona = {"nombre": "Pedro", "correo": "pedro@gmail.com"}
print("Diccionario inicial:", persona)
clave = input("¿Qué quieres actualizar (nombre/correo)?: ")
nuevo_valor = input(f"Ingresa el nuevo valor para {clave}: ")
persona[clave] = nuevo_valor
print("Diccionario actualizado:", persona)

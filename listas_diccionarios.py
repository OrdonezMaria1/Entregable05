# === Actividad 3: Listas y Diccionarios Relacionados ===

# Lista inicial de estudiantes
estudiantes = ["Ana", "Luis", "Sofía", "Carlos"]

# Diccionario: cada estudiante con su correo
contactos = {
    "Ana": "ana@example.com",
    "Luis": "luis@example.com",
    "Sofía": "sofia@example.com",
    "Carlos": "carlos@example.com"
}

while True:
    print("\n=== MENÚ ACTIVIDAD 3 ===")
    print("1. Mostrar estudiantes y sus correos")
    print("2. Agregar nuevo estudiante")
    print("3. Actualizar correo de un estudiante")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print("\nLista de estudiantes con correos:")
        for estudiante in estudiantes:
            print(estudiante, ":", contactos[estudiante])

    elif opcion == "2":
        nuevo = input("Ingresa el nombre del nuevo estudiante: ")
        correo = input(f"Ingresa el correo de {nuevo}: ")
        
        # Agregar a la lista y al diccionario
        estudiantes.append(nuevo)
        contactos[nuevo] = correo
        print(f"{nuevo} fue agregado con el correo {correo}.")

    elif opcion == "3":
        nombre = input("¿De qué estudiante quieres actualizar el correo?: ")
        if nombre in contactos:
            nuevo_correo = input(f"Ingresa el nuevo correo de {nombre}: ")
            contactos[nombre] = nuevo_correo
            print(f"Correo de {nombre} actualizado a {nuevo_correo}.")
        else:
            print("Ese estudiante no existe en la lista.")

    elif opcion == "4":
        print("¡Saliendo de la Actividad 3!")
        break

    else:
        print("Opción no válida, intenta de nuevo.")

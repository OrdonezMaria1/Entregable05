while True:
    print("\n=== MENÚ ===")
    print("1. Verificar si un número es par o impar")
    print("2. Mostrar cuadrados de una lista de números")
    print("3. Salir")
    
    opcion = input("Elige una opción (1-3): ")
    
    if opcion == "1":
        numero = int(input("Ingresa un número: "))
        if numero % 2 == 0:
            print(f"{numero} es par.")
        else:
            print(f"{numero} es impar.")

    elif opcion == "2":
        numeros = [1, 2, 3, 4, 5]
        print("Cuadrados de los números:")
        for n in numeros:
            print(f"{n}^2 = {n**2}")

    elif opcion == "3":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida, intenta de nuevo.")

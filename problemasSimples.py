import random

while True:
    print("\n=== MENÚ ACTIVIDAD 4 ===")
    print("1. Calculadora básica")
    print("2. Juego de adivinanza")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    # --- CALCULADORA ---
    if opcion == "1":
        print("\n--- CALCULADORA ---")
        print("Operaciones: suma, resta, multiplicacion, division")

        op = input("Elige una operación: ").lower()
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

        if op == "suma":
            print("Resultado:", a + b)
        elif op == "resta":
            print("Resultado:", a - b)
        elif op == "multiplicacion":
            print("Resultado:", a * b)
        elif op == "division":
            if b != 0:
                print("Resultado:", a / b)
            else:
                print("Error: división por cero")
        else:
            print("Operación no válida.")

    # --- JUEGO DE ADIVINANZA ---
    elif opcion == "2":
        print("\n--- JUEGO DE ADIVINANZA ---")
        numero_secreto = random.randint(1, 10)
        intento = 0
        adivinanza = -1

        print("He pensado un número entre 1 y 10. ¡Adivina cuál es!")

        while adivinanza != numero_secreto:
            adivinanza = int(input("Tu intento: "))
            intento += 1
            if adivinanza < numero_secreto:
                print("El número es mayor.")
            elif adivinanza > numero_secreto:
                print("El número es menor.")
            else:
                print(f"¡Correcto! Lo adivinaste en {intento} intentos.")

    # --- SALIR ---
    elif opcion == "3":
        print("¡Saliendo de la Actividad 4!")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
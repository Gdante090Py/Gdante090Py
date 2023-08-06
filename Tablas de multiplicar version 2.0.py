import random

def jugar_tablas():
    puntuacion = 0
    intentos = 10

    while intentos > 0:
        numero1 = random.randint(1, 10)
        numero2 = random.randint(1, 10)
        resultado = numero1 * numero2

        pregunta = f"¿Cuánto es {numero1} x {numero2}? "
        respuesta = int(input(pregunta))

        if respuesta == resultado:
            print("¡Correcto!")
            puntuacion += 1
        else:
            print("Incorrecto :(")
            print(f"La respuesta correcta era: {resultado}")

        intentos -= 1
        print(f"Te quedan {intentos} intentos\n")

    print(f"Juego terminado. Tu puntuación final es: {puntuacion}/10")

jugar_tablas()

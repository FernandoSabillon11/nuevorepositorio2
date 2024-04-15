import random

# Genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

intentos = 0
adivinado = False

print("¡Adivina el número secreto entre 1 y 100!")

while not adivinado:
    try:
        # Pide al usuario que ingrese un número
        guess = int(input("Ingresa un número: "))
        intentos += 1

        # Compara el número ingresado con el número secreto
        if guess == numero_secreto:
            adivinado = True
        elif guess < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        else:
            print("El número es menor. Intenta de nuevo.")

    except ValueError:
        print("Por favor, ingresa un número válido.")

# Cuando el usuario adivina el número
print(f"¡Felicitaciones! Adivinaste el número secreto {numero_secreto} en {intentos} intentos.")
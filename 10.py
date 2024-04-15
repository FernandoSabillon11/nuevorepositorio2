def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    num = int(input("Ingresa un número entero positivo: "))
    if es_primo(num):
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
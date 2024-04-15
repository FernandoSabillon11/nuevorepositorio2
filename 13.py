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

def lista_de_primos(limite):
    primos = []
    for num in range(2, limite):
        if es_primo(num):
            primos.append(num)
    return primos

try:
    limite = int(input("Ingrese un número límite para encontrar números primos: "))
    if limite <= 2:
        print("No hay números primos menores que", limite)
    else:
        primos = lista_de_primos(limite)
        print("Números primos menores que", limite, "son:", primos)
except ValueError:
    print("Por favor, ingrese un número válido.")
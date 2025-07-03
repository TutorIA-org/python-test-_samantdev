def filtrar_pares_descendente(lista):
    # Filtra solo los números pares
    pares = [num for num in lista if num % 2 == 0]
    # Ordena la lista de pares en orden descendente
    pares.sort(reverse=True)
    return pares
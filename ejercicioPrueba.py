def filtrar_pares(lista): 
    pares = []
    for i in lista:
        if i % 2 = 0:
            pares.append(i)
    pares.sort(reverse=True)
    return paress

resultado_global = None

def ejecutar():
    global resultado_global
    resultado_global = filtrar_pares([10, 3, 4, 5, 8, 11, 14, 7])
    print("Resultado:", resultado_global)

ejecutar()
lista = []
def enteros():
    dato = int(input("Ingrese un número entero, cuando quiera terminar ingrese 'fin': "))
    while dato != "fin":
        lista.append(int(dato))
        dato = input("Ingrese un número entero, cuando quiera terminar ingrese 'fin': ")
    print(lista)
enteros()

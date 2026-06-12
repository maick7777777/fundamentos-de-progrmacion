def MostarMenu():
    print("1 Ver carrito de tienda")
    print("2 Agregar juego al carrito")
    print("3 Ver mi carrito")
    print("4 Cargar fondos a la cartera")
    print("5 Pagar carrito")
    print("6 Ver mi biblioteca")
    print("7 Salir")


def MostrarJuegos(lista_generica):
    if not lista_generica:
        print("la lista se encuentra vacia")
    else:
        for recorrido in lista_generica:
            print(f"{recorrido["titulo"]}=$ {recorrido["precio "]}")


def CalcularTotal(lista_generica):
    suma=0
    for recorrido in lista_generica["precio"]:
        suma+= recorrido["precio"]
    return suma 


def BuscarJuego(catalogo,nombre_buscar):
    for recorrido in catalogo:
        if recorrido["titulo"].lower() == nombre_buscar["titulo"]


   
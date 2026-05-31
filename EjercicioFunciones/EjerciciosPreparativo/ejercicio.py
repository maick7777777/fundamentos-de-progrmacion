productos ={
    "Mouse" : [10, 15000],
    "Teclado" : [5, 25000],
    "Monitor" : [3, 18000]

}

#funcion para agregar productos
def agregar_productos(productos):
    nombre=input("Nombre del producto: ").strip()#quita los espacios en blanco 
    if nombre== " ":
        print("el nombre no puede estar vacio")

    if nombre in productos:
        print("el nombre ya esta en productos ")

    stock=int(input("Ingrese stock-->"))
    precio=int(input("Ingrese el precio $-->"))

    productos[nombre] = [stock,precio]
    print("Productos agregados correctamente ")

#funcion para mostrar los productos
"""""
def mostrar_producto(productos):
    for clave , valor in productos.items():
        print(f"nombre prodructo {clave}|stock y valor {valor}")
"""""
def mostrar_producto(productos):
    for i in productos.items():
        print(i)

#funcion para buscar los productos
def buscar_productos(productos):
    buscador=input("ingrese el producto a buscar-->").capitalize()
    for i in productos:
        if buscador in i:
            print(f"producto {buscador} existente")
            break
        else:
            print("el producto no existe")  
            break  
#funcion para buscar el producto mas caro
def producto_mas_caro(productos):
    precio_max=0
    producto_max= " "
    for clave, valor in productos.items():
        if valor[1]>precio_max:
            precio_max=valor[1]
            producto_max=clave

    print(f"el productos {producto_max} es el mayor con {precio_max}")

while True:
    print("MENU REGISTRO")
    print("1 Agregar producto")
    print("2 Mostrar productos")
    print("3 Buscar productos")
    print("4 Producto mas caro")
    print("5 salir ")

    try:
        op =int(input("Ingrese la opcion-->"))
    except ValueError:
        print("Solo se aceptan valores numericos ")

    if op==1:
        agregar_productos(productos)
    elif op==2:
        mostrar_producto(productos)
    elif op==3:
        buscar_productos(productos)
    elif op==4:
        producto_mas_caro(productos)
    elif op==5:
        break
    else:
        print("La opcion ingresada no es valida")                  

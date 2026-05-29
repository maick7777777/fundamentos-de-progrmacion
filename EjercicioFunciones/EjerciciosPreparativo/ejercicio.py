producto ={
    "Mouse" : [10, 15000],
    "Teclado" : [5, 25000],
    "Monitor" : [3, 18000]



}

def agregar_productos(productos):
    nombre=input("Nombre del producto: ").strip()#quita los espacios en blanco 
    if nombre== " ":
        print("el nombre no puede estar vacio")

    if nombre in producto:
        print("el nombre ya esta en productos ")

    stock=int(input("Ingrese stock-->"))
    precio=int(input("Ingrese el precio $-->"))

    productos[nombre] = [stock,precio]
    print("Productos agregados correctamente ")

while True:
    print("MENU REGISTRO")
    print("1 Agregar producto")
    print("2 Mostrar productos")
    print("3 Buscar productos")
    print("4 Producto mas caro")
    print("5 salir ")
    op =int(input("Ingrese la opcion-->"))

    if op==1:
        print
    elif op==2:
        print
    elif op==3:
        print  
    elif op==4:
        print
    elif op==5:
        break
    else:
        print("La opcion ingresada no es valida")                  

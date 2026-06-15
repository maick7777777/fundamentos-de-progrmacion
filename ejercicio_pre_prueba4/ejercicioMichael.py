lista_autos=[]

def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo ")
    print("3. Eliminar vehículo ")
    print("4. Actualizar disponibilidad ")
    print("5. Mostrar vehículos ")
    print("6. Salir ")
    print("===================================== ")

def selecion_opcion():
    while True:
        try:
            op=int(input("-->"))
            return op
        except ValueError:
            print("la opcion ingresada debe ser de valor numerico")    
        

#funcion para agregar vehucilos a la lista con diccionarios
def agregar_vehiculos(lista):
    modelo=input("Ingrese el modelo-> ")
    validacion_modelo_vehiculos(modelo)

    año=int(input("Ingrese el año del auto-> "))
    validacion_año_vehiculo(año)

    precio=float(input("Ingrese el precio-> "))
    validacion_precio_vehiculo(precio)
    
    if validacion_modelo_vehiculos==True and validacion_año_vehiculo==True and validacion_precio_vehiculo==True:
        vehiculos={
            "modelo" : modelo,
            "año" : int(año),
            "precio" : float(precio),
            "disponible" : False
        }
        print("vehiculo agregado correctamente")
        lista.append(vehiculos)
    else:
        print("el vehiculo no se puedo agregar")

#funcion de validacion del model del vehiculo
def validacion_modelo_vehiculos(modelo_auto_validar):
    
    if not modelo_auto_validar.strip():
        print("Modelo no puede estar vacio")
        return False
    else:
        return True   
    
#funcion de validacion del año del vehiculo    
def validacion_año_vehiculo(año_auto_validar):
    try:
        if int(año_auto_validar)<1900:
            print("El año debe ser mayor a 1900 ")
            return False
        else:
            return True
    except ValueError:
        print("solo se aceptan valores numericos")
        return False

#funcio de validacion del precio del vehiculo
def validacion_precio_vehiculo(precio_auto_validar):
    try:
        if float(precio_auto_validar)<0:
            print("el precio no puede ser 0 o menor  ")
            return False
        else:
            return True
    except ValueError:
        print("solo se aceptan valores numericos")
        return False
    

def buscar_vehiculo(lista, modelo_buscar):
    for indice, vehiculo in enumerate(lista):
        if vehiculo["modelo"]==modelo_buscar:
            return indice
        
    return -1

def actualizar_vehiculo(lista):
    for vehiculo in lista:
        if vehiculo["año"]>=2020:
            vehiculo["disponible"]=True
        else:
            vehiculo["disponible"]=False
    print("se actualizaron los estados")

def mostrar_vehiculo(lista):
    actualizar_vehiculo(lista)

    for vehiculo in lista:
        print("=== LISTA DE VEHICULOS === ")
        print(f"modelo: {vehiculo["modelo"]}")
        print(f"año: {vehiculo["año"]}")
        print(f"precio: {vehiculo["precio"]}")
        if vehiculo["disponible"]:
            print(f"estado: disponible ")
        else:
            print(f"estado: no disponible ")
        print("*"*20)




while True:
    menu()
    opcion=selecion_opcion()

    if(opcion==1):
        agregar_vehiculos(lista_autos)

    elif(opcion==2):
        modelo_buscado=input("Modelo a buscar->")
        posicion = buscar_vehiculo(lista_autos,modelo_buscado)
        
        if posicion != -1:
            print(f"posiscion del vehiculo {posicion}")
            vehiculo_enocntado = lista_autos[posicion]

            print(f"modelo {vehiculo_enocntado["modelo"]}")
            print(f"precio {vehiculo_enocntado["precio"]}")
            print(f"año {vehiculo_enocntado["año"]}")
        else:
            print(f"el modelo {modelo_buscado} no se encuantra registrado")    

    elif(opcion==3):
        buscar_vehiculo(lista_autos,modelo_buscado)
        vehiculo_eliminar=input("Modelo a eliminar-->")
        vehiculo_enocntado = lista_autos[posicion]
        if posicion != -1:
            lista_autos.remove(posicion)
            print("auto removido")
        else:    
            print(f"El vehículo {vehiculo_eliminar} no se encuentra registrado. ")
    
    elif(opcion==4):
        actualizar_vehiculo(lista_autos)
    elif(opcion==5):
        mostrar_vehiculo(lista_autos)             
    elif(opcion==6):
        break
lista_vehiculos=[]
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo ")
    print("3. Eliminar vehículo ")
    print("4. Actualizar disponibilidad ")
    print("5. Mostrar vehículos ")
    print("6. Salir ")
    print("===================================== ")

def selecionar_opcion():
    while True:    
        try:
            op=int(input("->"))
            return op
        except ValueError:
            print("Solo se aceptan valores numericos")  

def validador_modelo(modelo):
    if(modelo.strip()==""):
        return False
    else:
        return True

def validador_año(año):
    try:
        año= int(año)
        if int(año)<1900:
            return False
        else:
            return True
    except ValueError:
        return False

def validador_precio(precio):
    try:
        precio=float(precio)
        if float(precio)<0:
            return False
        else:
            return True
    except ValueError:
        return False
            


def agregar_vehiculo(lista):
    print("**AGREGAR VEHICULO**")
    modelo_vehiculo=input("Modelo->")
    modelo_valido= validador_modelo(modelo_vehiculo)
    if modelo_valido==False:
        print("Modelo no se puede encontar vasio ni contener solo espacios")
    else:
        print("Modelo valido")   
    print("-----------------------") 
    año_vehiculo=int(input("Año->"))
    año_valido=validador_año(año_vehiculo)
    if  año_valido==False:
        print("El año debe ser un numero entero mayor a 1900 ")
    else:
        print("Año valido")
    print("-----------------------") 
    precio_vehiculo=float(input("Valor->"))
    precio_valido=validador_precio(precio_vehiculo)
    if precio_valido==False:
        print("El precio debe ser un numero decimal mayor que 0")
    else:
        print("Precio valido") 
    print("-----------------------") 

    if(modelo_valido==True) and (año_valido==True) and (precio_valido==True):
        vehiculo={
            "modelo" : modelo_vehiculo,
            "año" : año_vehiculo,
            "precio": precio_vehiculo,
            "disponible" : False 
        }
        lista_vehiculos.append(vehiculo)   
        print("Vehiculo agregado correctamente") 
    else:
        print("el vehiculo no se agrego revise los mensajes de error")    


def buscar_vehiculo(lista, modelo_buscar):
    for indice, vehiculo in enumerate(lista):
        if vehiculo["modelo"]==modelo_buscar:
            return indice
    return indice -1    

def actualizar_disponibilidad(lista):
    for vehiculo in lista:
        if vehiculo["año"]>=2020:
            vehiculo["disponible"]=True
        else:
            vehiculo["disponible"]=False
    print("se actulizo la disponibilidad ")        

while True:    
    mostrar_menu()
    opcion=selecionar_opcion()

    if (opcion==1):
        agregar_vehiculo(lista_vehiculos)

    elif(opcion==2):
        modelo_buscar=input("Modelo a buscar-> ")
        print("-----------------------") 
        posicion=buscar_vehiculo(lista_vehiculos, modelo_buscar)
        if posicion!= -1:
            vehiculo_enocntrado=lista_vehiculos[posicion]
            print(f"Posicion del vehiculo: {posicion}")
            print(f"modelo{vehiculo_enocntrado ["modelo"]}")
            print(f"año{vehiculo_enocntrado ["año"]}")
            print(f"precio{vehiculo_enocntrado ["precio"]}")
            if vehiculo_enocntrado["disponible"]:
                print("disponible: si")
            else:
                print("disponible : no")    
        else:
            print("Vehiculo no encontrado")    

    elif(opcion==3):
        modelo_buscar=input("Modelo a eliminar-> ")
        posicion=buscar_vehiculo(lista_vehiculos, modelo_buscar)
        if posicion != 1:
            lista_vehiculos.pop(posicion)
            print(f"El vehiculo {modelo_buscar} se elimino correctamente")
        else:
            print(f"El vehículo {modelo_buscar} no se encuentra registrado.")    

    elif(opcion==4):
        actualizar_disponibilidad(lista_vehiculos)
    elif(opcion==5):
        actualizar_disponibilidad(lista_vehiculos)
        for automovil in lista_vehiculos:
            print(f"Modelo : {automovil["modelo"]}")
            print(f"Año: {automovil["año"]}")
            print(f"Precio: {automovil["precio"]}")
            if automovil["disponible"]==True:
                print(f"Estado: DISPONIBLE") 
            else:
                print(f"Estado: NO DISPNIBLE") 

    elif(opcion==6):
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
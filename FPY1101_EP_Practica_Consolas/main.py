consolas={}
ventas ={}

def agregar_consola(consolas, ventas):
    sigla=input("Sigla--> ").upper()
    sigla_validada=validador_sigla(sigla,consolas)

    nombre=input("Nombre--> ")
    nombre_validado=validador_nombre(nombre)

    fabricante=input("Fabricante-->")
    fabricante_validado=validador_fabricante(fabricante)

    año=int(input("Año-->"))
    año_validado= validador_año(año)

    precio=float(input("Precio-->"))
    precio_validado= validador_precio(precio)

    stock=int(input("Stock-->"))
    stock_validado=validador_stock(stock)

    if (sigla_validada==True) and (nombre_validado==True) and (fabricante_validado==True) and (año_validado==True) and (precio_validado==True) and (stock_validado==True):
        consolas[sigla] =[nombre, fabricante, año]

        ventas[sigla]=[precio, stock]
        print("Se agrego corrcetamente")
    else:
        print("No se logro agregar los valores")    
        

#validadores 
def validador_sigla(sigla, consola):   
    if sigla in consola:
        print("falso sigla")
        return False
    else:
        return True

def validador_nombre(nombre):
    if not nombre:
        print("falso nombre")
        return False
    
    if len(nombre)<3 or len(nombre)>40:
        print("falso nombre 2")
        return False
    else:
        return True 

def validador_fabricante(fabricante):
    if not fabricante:
            print("falso fabricante")
            return False
        
    if len(fabricante)<=2 or len(fabricante)>=30:
        print("falso fabricante 2")
        return False
    else:
        return True 

def validador_año(año):
    if año<=1972 and año>=2025:
        print("falso año")
        return False
    else:
        return True

def validador_precio(precio):
    if float(precio)<0:
        print("falso precio") 
        return False
    else:
        return True

def validador_stock(stock):
    if int(stock)>=0:
        return True
    else:
        print("falso stock")
        return False
 
def buscar_consola(consolas, ventas):
    sigla_buscar=input("Ingrese la sigla de la consola que quiere buscar--> ")
    for clave, valor in consolas.items():
        if clave == sigla_buscar:
            print("=== Consola Encontrada ===")
            print(f"Sigla : {consolas["sigla"]}")
            print(f"Nombre : {consolas["nombre"]}")
            print(f"Fabricante : {consolas["fabricante"]}")
            print(f"Año lanz : {consolas["año"]}")
            for clave, valor in ventas.items():
                if clave==sigla_buscar:
                        print(f"Precio : {ventas["precio"]}")
                        print(f"Stock : {ventas["stock"]}")
        else:
            print("Sigla buscada no existe ")

while True:
    print("***MENU PRINCIPAL***")
    print("-"*30)
    print("1. Agregar consola")
    print("2. Buscar consola")
    print("3. Eliminar consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")
    print("-"*30)
    while True:
        try:
            opcion=int(input("-->"))
            break
        except ValueError: 
            print("Solo se aceptan valores numericos") 

    if opcion==1:
        agregar_consola(consolas,ventas)
    elif opcion==2:
        buscar_consola(consolas,ventas)
    elif opcion==3:
        print("c")    
    elif opcion==4:
        print(consolas, ventas)    
    elif opcion==5:
        break   
    else:
        print("La opcion ingresada esta fuera de rango ")              
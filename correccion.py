arreglos = { 
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'], 
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'], 
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'], 
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'], 
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'], 
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'], 
} 

bodega = { 
    'FLO1': [15990, 8], 
    'FLO2': [29990, 3], 
    'FLO3': [9990, 12], 
    'FLO4': [24990, 5], 
    'FLO5': [19990, 0], 
    'FLO6': [22990, 6], 
} 

# --- MENÚ Y LECTURA ---
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            op = int(input("Ingrese opción: "))
            if 1 <= op <= 6:
                return op
            else:
                print("El numero ingresado esta fuera de rango [1 a 6]")
        except ValueError:
            print("Solo se aceptan valores numericos enteros")    

# --- OPCIÓN 1 ---
def unidades_tipo(tipobuscado, DiccionarioArreglos, DiccionarioBodegas):   
    tipobuscado = tipobuscado.strip().lower()
    cont_similares = 0

    for claveArreglos, valorArreglos in DiccionarioArreglos.items():
        if valorArreglos[1].lower() == tipobuscado:
            # Buscar directo en el diccionario de bodega (más eficiente)
            if claveArreglos in DiccionarioBodegas:
                cont_similares += DiccionarioBodegas[claveArreglos][1]
                
    # Corrección: Uso de formato solicitado y variables correctas
    print(f"El total de unidades disponibles es: {cont_similares}")            

# --- OPCIÓN 2 ---
def busqueda_precio(p_min, p_max, DiccionarioArreglos, DiccionarioBodegas):
    lista_similares = []
    
    for claveBodega, valorBodega in DiccionarioBodegas.items():
        if p_min <= valorBodega[0] <= p_max and valorBodega[1] > 0:
            if claveBodega in DiccionarioArreglos:
                nombre_arreglo = DiccionarioArreglos[claveBodega][0]
                lista_similares.append(f"{nombre_arreglo}--{claveBodega}")

    if len(lista_similares) == 0:
        print("No hay arreglos en ese rango de precios.")
    else:
        lista_similares.sort() 
        print(f"Los arreglos encontrados son: {lista_similares}")

# --- OPCIÓN 3 ---
def buscar_codigo(codigo, DiccionarioBodega):
    codigo_estandar = codigo.upper() # Insensible a mayúsculas
    if codigo_estandar in DiccionarioBodega:
        return True
    else:
        return False
    
def actualizar_precio(codigo, precio, DiccionarioBodega):
    codigo_estandar = codigo.upper()
    # Corrección: Evitar variables globales y usar los parámetros
    if buscar_codigo(codigo_estandar, DiccionarioBodega):
        DiccionarioBodega[codigo_estandar][0] = precio
        return True
    else:
        return False # Corrección: Faltaba el return explícito

# --- VALIDACIONES OPCIÓN 4 ---
def validador_codigo(codigo, DiccionarioBodega):
    if not codigo.strip():
        return False
    # El código no debe existir previamente
    if buscar_codigo(codigo, DiccionarioBodega):
        return False
    return True

def validador_nombre(nombre):
    if not nombre.strip():
        return False
    return True
    
def validador_tipo(tipo):
    if not tipo.strip():
        return False
    return True
    
def validador_colorprincipal(color):
    if not color.strip():
        return False
    return True

def validador_tamaño(tamaño):
    if tamaño in ["S", "M", "L"]:
        return True
    return False

def validor_incluye_tarejeta(tarjeta):
    if tarjeta in ["S", "N"]:
        return True
    return False

def validador_temporada(temporada):
    if not temporada.strip():
        return False
    return True
    
def validador_precio(precio):
    if isinstance(precio, int) and precio > 0:
        return True
    return False
                    
def validador_unidades(unidades):
    if isinstance(unidades, int) and unidades >= 0:
        return True
    return False

# --- AGREGAR Y ELIMINAR (OPCIÓN 4 Y 5) ---
def agregar_arreglo(codigo, nombre, tipo, color, tamaño, tarjeta_boolean, temporada, precio, unidades, DiccionarioArreglos, DiccionarioBodega):
    codigo_estandar = codigo.upper()
    # Corrección: Asignación directa como lista simple (no anidada con append)
    DiccionarioArreglos[codigo_estandar] = [nombre, tipo, color, tamaño, tarjeta_boolean, temporada]
    DiccionarioBodega[codigo_estandar] = [precio, unidades]
    return True

def eliminar_codigo(codigo, DiccionarioArreglo, DiccionarioBodega):
    codigo_estandar = codigo.upper()
    if buscar_codigo(codigo_estandar, DiccionarioBodega):
        del DiccionarioArreglo[codigo_estandar]
        del DiccionarioBodega[codigo_estandar]
        return True
    else:
        return False # Corrección: Faltaba el return explícito


# --- PROGRAMA PRINCIPAL ---
while True:
    mostrar_menu()
    opcion = leer_opcion()
    
    if opcion == 1:
        tipo_buscar = input("Ingrese tipo de arreglo a consultar: ")
        unidades_tipo(tipo_buscar, arreglos, bodega)
        
    elif opcion == 2:
        while True:
            try:
                precioMinimo = int(input("Ingrese precio minimo: "))
                precioMaximo = int(input("Ingrese precio maximo: "))
                if precioMinimo >= 0 and precioMaximo >= 0 and precioMinimo <= precioMaximo:
                    busqueda_precio(precioMinimo, precioMaximo, arreglos, bodega)
                    break
                else:
                    print("Los números deben ser mayores o iguales a 0, y el mínimo menor o igual al máximo.")
            except ValueError:
                print("Debe ingresar valores enteros")

    elif opcion == 3:
        while True:
            codigo_buscar = input("Ingrese código del arreglo: ")
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                precio_actualizado = actualizar_precio(codigo_buscar, nuevo_precio, bodega)
                if precio_actualizado:
                    print("Precio actualizado")
                else:
                    print("El código no existe")
            except ValueError:
                print("Debe ingresar un valor numérico entero.")
            
            pregunta = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
            if pregunta != "s":
                break
                
    elif opcion == 4:
        # Validación de datos ingresados uno por uno
        new_codigo = input("Ingrese código del arreglo: ").upper()
        if not validador_codigo(new_codigo, bodega):
            print("Código inválido o ya existe.")
            continue # Vuelve al menú si falla
            
        new_nombre = input("Ingrese nombre: ")
        if not validador_nombre(new_nombre):
            print("El nombre no puede estar vacío.")
            continue
            
        new_tipo = input("Ingrese tipo: ")
        if not validador_tipo(new_tipo):
            print("El tipo no puede estar vacío.")
            continue
            
        new_color = input("Ingrese color principal: ")
        if not validador_colorprincipal(new_color):
            print("El color no puede estar vacío.")
            continue
            
        new_tamaño = input("Ingrese tamaño (S/M/L): ").upper()
        if not validador_tamaño(new_tamaño):
            print("Tamaño inválido. Debe ser S, M o L.")
            continue
            
        new_tarjeta = input("¿Incluye tarjeta? (s/n): ").upper()
        if not validor_incluye_tarejeta(new_tarjeta):
            print("Debe ingresar 's' o 'n'.")
            continue
        # Convertir a booleano antes de guardar
        tarjeta_boolean = True if new_tarjeta == "S" else False
            
        new_temporada = input("Ingrese temporada: ")
        if not validador_temporada(new_temporada):
            print("La temporada no puede estar vacía.")
            continue
            
        try:
            new_precio = int(input("Ingrese precio: "))
            if not validador_precio(new_precio):
                print("El precio debe ser un número entero mayor a 0.")
                continue
        except ValueError:
            print("El precio debe ser numérico.")
            continue
            
        try:
            new_unidades = int(input("Ingrese unidades: "))
            if not validador_unidades(new_unidades):
                print("Las unidades deben ser un entero mayor o igual a 0.")
                continue
        except ValueError:
            print("Las unidades deben ser numéricas.")
            continue

        # Si llega aquí, todas las validaciones pasaron
        if agregar_arreglo(new_codigo, new_nombre, new_tipo, new_color, new_tamaño, tarjeta_boolean, new_temporada, new_precio, new_unidades, arreglos, bodega):
            print("Arreglo agregado")
            
    elif opcion == 5:
        codigo_eliminar = input("Ingrese código del arreglo a eliminar: ")
        validacion_eliminar = eliminar_codigo(codigo_eliminar, arreglos, bodega)
        if validacion_eliminar:
            print("Arreglo eliminado")
        else:
            print("El código no existe")
            
    elif opcion == 6:
        print("Programa finalizado.")
        break
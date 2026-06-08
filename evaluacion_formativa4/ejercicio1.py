usuarios={}

def menu():
    print("1 Ingresar usuario")
    print("2 Buscar usuario")
    print("3 Eliminar usuario")
    print("4 Salir")

def ingresar_usuario(usuarios):

    name_user=input("Nombre del usuario-->")
    if name_user in usuarios:
        print("El nombre esta repetido, ingrese uno nuevo")

    while True:
        sexo=input("sexo [M|F]").upper()
        if (sexo=="M") or (sexo=="F"):
            break 
        else:
            print("Solo se aceptan los valores M=Masculino o F=Femenino")  

    while True:  
        contraseña=input("Contraseña-->")
        if len(contraseña)<8:
            print("Minimo debe contener 8 caracteres")
            continue

        flag_letras=False
        flag_numeros=False


        for caracter in contraseña:
            if caracter.isdigit():
                flag_numeros=True
            if  caracter.isalpha():
                flag_letras=True
                
            if contraseña in " ":
                print("La contraseña no puede contener espacios ")
        if not flag_numeros:
            print("debe contener un numero")
        elif not flag_letras:
            print("debe contener letras ")
        else:
            # Si pasó todas las validaciones, rompemos el bucle 'while'
            print("¡Contraseña válida")
            usuarios[name_user]=[sexo, contraseña]
            break

def buscar_usuario(usuarios):
    for clave, valor  in usuarios.items():
        buscar=input("Nombre del usauario-->")
        if clave==buscar:
            print(f"Usuario {buscar} Sexo {valor[0]} contraseña{valor[1]} ")
        else:
            print("Usuario no encontrado")    

def eliminar_usuarios(alumnos):
    eliminar=input("nombre de usuario-->")
    if eliminar in alumnos:
        del alumnos[eliminar]
        print("el usuario eliminado")
    else:
        print("usuario no encontrado" )



while True:
    menu()
    op=int(input("-->"))

    if (op==1):
        ingresar_usuario(usuarios)
    elif(op==2):
        buscar_usuario(usuarios)   
    elif(op==3):
        eliminar_usuarios(usuarios)
    elif(op==4):
        break 
    else:
        print("la opcion ingresada esta fuera de rango ")


    

# Creamos la funcion para agregar los datos del usuario
def agregar_usuario():
    nombre = input("Ingrese el nombre del usuario:\n").lower().strip()
    edad = input("Ingrese la edad del usuario:\n").strip()
    correo = input("Ingrese el correo del usuario:\n").lower().strip()
    
    # Hacemos una validación sencilla para el correo
    if "@" not in correo or "." not in correo:
        print("Correo no valido.")
        return
    else:
        # Creamos la linea con los datos optenidos y la agregamos al archivo
        linea = f"{nombre},{edad},{correo}\n"
        with open("usuarios.txt", "a") as archivo:
            archivo.write(linea)
            print("Usuario agregado correctamente.")

# Una funcion para ver los usuarios ya guardados           
def ver_usuarios():
    with open("usuarios.txt", "r") as archivo:
        lineas = archivo.readlines()
        
        if not lineas:
            print("No hay usuarios a mostrar.")
            
        else:
            for linea in lineas:
                datos = linea.strip().split(",")
                nombre = datos[0]
                edad = datos[1]
                correo = datos[2]
            
                # Para imprimir en consola
                print("Nombre:", nombre)
                print("Edad:", edad)
                print("Correo:", correo)
                print("-" * 25)
        
           
# Una funcion para actualizar el usuario     
def actualizar_usuario():
    nombre_a_actualizar = input("\nIngrese el nombre del usuario que quiere actualizar:\n").lower().strip()
    try:
        with open("usuarios.txt", "r") as archivo:
            lineas = archivo.readlines()
        
            nuevas_lineas = []
            usuario_encontrado = False
        
            for linea in lineas:
                datos = linea.strip().split(",")
                nombre = datos[0]
                
                # si el nombre es igual al nombre a actualizar , pedimos los nuevos datos
                if nombre == nombre_a_actualizar:
                    nueva_edad = input("Ingrese la nueva edad del usuario:\n").strip()
                    nuevo_correo = input("Ingrese el nuevo correo del usuario:\n").lower().strip()
                    
                    # Hacemos otra validación para el nuevo correo
                    if "@" not in nuevo_correo or "." not in nuevo_correo:
                        print("Nuevo correo no valido")
                        
                    linea_nueva = f"{nombre},{nueva_edad},{nuevo_correo}\n"
                    nuevas_lineas.append(linea_nueva)
                    usuario_encontrado = True
                    
                else:
                    nuevas_lineas.append(linea)
        
            with open("usuarios.txt", "w") as archivo:
                archivo.writelines(nuevas_lineas)
        
            if usuario_encontrado:
                print("Usuario actualizado correctamente.")
            else:
                print("Usuario no encontrado.")

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")

# Una funcion para eliminar al usuario    
def eliminar_usuario():
    nombre_a_eliminar = input("\nIngrese el nombre del usuario que quiere eliminar:\n").lower().strip()
    try:
        with open("usuarios.txt", "r") as archivo:
            lineas = archivo.readlines()
        
            nuevas_lineas = []
            usuario_encontrado = False
        
            for linea in lineas:
                datos = linea.strip().split(",")
                nombre = datos[0]

                # Si encuentra al usuario no lo deja pasar y se guardan los otros en la lista
                if nombre == nombre_a_eliminar:
                    usuario_encontrado = True
                else:
                    nuevas_lineas.append(linea)
        
            with open("usuarios.txt", "w") as archivo:
                archivo.writelines(nuevas_lineas)
        
            if usuario_encontrado:
                print("Usuario eliminado correctamente.")
            else:
                print("Usuario no encontrado.")
    
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")

#Creamos el menu con bienvenida           
def menu():
    print("---BIENVENIDO AL GESTOR DE USUARIOS---\n")
    print("1. Agregar usuario")
    print("2. Ver usuarios")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Salir\n") 
          
# Usamos el bucle while para mostrar el menu hasta que el usuario decida salir   
if __name__ == "__main__":
    while True:
        menu()
        
        opcion = input("Ingrese un numero de opción para ejecutar:\n").strip()
    
        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            ver_usuarios()
        elif opcion == "3":
            actualizar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            print("Gracias por utilizar el Gestor de Usuarios.")
            break
        else:
            print("Opción no valida")      
            
                
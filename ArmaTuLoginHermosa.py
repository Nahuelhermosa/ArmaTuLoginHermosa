# Diccionario 
usuarios = {
     "Nahuel": "123",
    "Lazaro": "1234",
    "Yamila": "12345"
}

# Funcion 1
def registrar_usuario():
    usuario = input("Ingrese un nombre de usuario: ")
    if usuario in usuarios:
        print(" El usuario ya existe. Intente con otro nombre.")
        return
    
    contraseña = input("Ingrese una contraseña: ")
    usuarios[usuario] = contraseña
    print(f" Usuario '{usuario}' registrado con exito.")



# Funcion 2
def login_usuario():
    usuario = input("Ingrese su usuario: ")
    if usuario not in usuarios:
        print(" Usuario no se encuentra.")
        return
    
    contraseña = input("Ingrese su contraseña: ")
    if usuarios[usuario] == contraseña:
        print(f"Bienvenido {usuario}, sesion iniciada.")
    else:
        print("Contraseña incorrecta.")



# Funcion 3
def mostrar_usuarios():
    if not usuarios:
        print(" No hay usuarios registrados.")
        return
    
    print("\n Lista de usuarios registrados:")
    for nombre in usuarios.keys():
        print(f"- {nombre}")

        

# Bucle Menú
def menu():
 while True:
    print("\n=== MENU ===")
    print("1. Registrar usuario")
    print("2. Iniciar sesion")
    print("3. Mostrar usuarios")
    print("4. Salir")
        
    opcion = input("Seleccione una opcion: ")
        
    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        login_usuario()
    elif opcion == "3":
        mostrar_usuarios()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida, intente de nuevo.")

menu()

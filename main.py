import json
print("""
=========================
 INVENTARIO VIRTUAL
      
=========================
""")
def mostrar_menu():
    opcion=int(input("bienvenido" \
    "?que desea hacer?" \
    "(inicio de sesion (1)" \
    "registrarse (2)\n"))
    return opcion

    

correo_guardado = ""
contrasena_guardada = ""
while True:
    opcion=mostrar_menu()
    if opcion==1:
        correo_guardado=input("ingrese su correo guardado:-")
        contrasena_guardada=input("ingrese su contrase;a guardada:-")
        with open("usuarios.json", "r") as archivo:
           datos = json.load(archivo)
        print(datos)


        break
   
    else:
        correo_guardado=input( "ingrese su correo empresaria:-")
        contrasena_guardada=input('ingrese su contrase;a guardada:-')
        datos = {}
        datos["correo"] = correo_guardado
        datos["contrasena"] = contrasena_guardada
        with open("usuarios.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)
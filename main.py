import json
try:
    with open("materiales.json", "r") as archivo:
        materiales = json.load(archivo)
except FileNotFoundError:
    materiales = []

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

def agregar_material():
    material=input("ingrese el nombre del nuevo material")
    codigo=input("ingrese el codigo del nuevo material")
    nuevo_material={"material": material, "codigo": codigo, "existencias": 0}
    materiales.append(nuevo_material)
    with open("materiales.json", "w") as archivo:
        json.dump(materiales, archivo, indent=4)
    print(f"se agrego correctamente: {nuevo_material}")

def eliminar_materiales():
    codigo=input("ingrese el codigo del nuevo material")
    for i in range(len(materiales)):
        if codigo== materiales[i]["codigo"]:
            materiales.pop(i)
            break
    else:
        print("material no encontrado.-")
    with open("materiales.json", "w") as archivo:
        json.dump(materiales, archivo, indent=4)
    

def mostrar_materiales():
    if len(materiales) == 0:
        print("no hay materiales registrados")
    else:
        print("materiales registrados:")
        for material in materiales:
            print(f"material: {material['material']}, codigo: {material['codigo']}, existencias: {material['existencias']}")
            

def cambiar_existencias():
    mostrar_materiales()
    material_a_cambiar = input("ingrese el nombre del material cuyas existencias desea cambiar: ")
    for material in materiales:
        if material['material'] == material_a_cambiar:
            nuevas_existencias=int(input("ingrese la cantidad a a;adir: "))
            material['existencias'] = nuevas_existencias+material["existencias"]
            print("existencias actualizadas.")
            print(f"material: {material['material']}, codigo: {material['codigo']}, existencia: {material['existencias']}")
            with open("materiales.json", "w") as archivo:
                json.dump(materiales, archivo, indent=4)
            break
    else:
        print("material no encontrado")

while True:
    opcion=mostrar_menu()
    if opcion==1:
        correo_guardado=input("ingrese su correo guardado:-")
        contrasena_guardada=input("ingrese su contrase;a guardada:-")
        with open("usuarios.json", "r") as archivo:
           datos = json.load(archivo)
        if correo_guardado == datos["correo"] and contrasena_guardada == datos["contrasena"]:
            print("Bienvenido")
            break
        else:
            print("datos incorrectos, intente nuevamente")


   
    elif opcion==2:
        correo_guardado=input( "ingrese su correo empresaria:-")
        contrasena_guardada=input('ingrese su contrase;a guardada:-')
        datos = {}
        datos["correo"] = correo_guardado
        datos["contrasena"] = contrasena_guardada
        with open("usuarios.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)
        print ('login exitoso')
    else:
        print("opcion invalida")
    print('log fine')

while True:
    opcion_inv=int(input(f"BIENVENIDO AL INVENTARIO VIRTUAL {correo_guardado}"))
    print("¿que desea hacer?"
    "\nagregar/eliminar material (1)" \
    "mostrar materiales (2)" \
    "agregar/eliminar existencias (3)\n "
    "salir (4)")
    
    if opcion_inv==1:
        agregar_eliminar=int(input('desea agregar (1) o eliminar un material (2)?  '))
        if agregar_eliminar == 1:
            agregar_material()
        elif agregar_eliminar ==2:
            eliminar_materiales()
        else:
            print("opcion invalida")

    elif opcion_inv==2:
        mostrar_materiales()
    elif opcion_inv==3:
        cambiar_existencias()
    elif opcion_inv==4:
        print('vuelva pronto')
        break
    else:
        print('opcion invalida')
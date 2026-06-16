print("""
=========================
 INVENTARIO VIRTUAL
      
      
 CALDERAS LEÓN
=========================
""")

correo_guardado = ""
contrasena_guardada = ""



import json

with open("usuarios.json") as archivo:
    datos = json.load(archivo)

print(datos)
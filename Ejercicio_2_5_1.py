#Dado el nombre de un producto y una lista de productos se deberá
#buscar el producto en dicha lista y en caso de encontrar una o más
#coincidencias se deberá devolver los resultados como una nueva lista.

productos = [
    {"id": 1, "nombre": "Camiseta", "color": "rojo", "tipo": "ropa", "precio": 100},
    {"id": 2, "nombre": "Mesa", "color": "blanco", "tipo": "mueble", "precio": 300},
    {"id": 3, "nombre": "Silla", "color": "negro", "tipo": "mueble", "precio": 500},
    {"id": 4, "nombre": "Pantalón", "color": "azul", "tipo": "ropa", "precio": 200},
    {"id": 5, "nombre": "Cama", "color": "blanco", "tipo": "mueble", "precio": 10},
]



def buscar_producto(nombre_producto, lista_productos):
    resultados = {}
    for producto in lista_productos:
        if producto['nombre'] == nombre_producto or producto['color'] == nombre_producto or producto['tipo'] == nombre_producto or producto['precio'] == nombre_producto:
            resultados.append(producto)
    return resultados

resultados_busqueda = buscar_producto("Silla", productos)

if len(resultados_busqueda) > 0:
    print("Productos encontrados:")
    for producto in resultados_busqueda:
        print("ID:", producto["id"])
        print("Nombre:", producto["nombre"])
        print("Color:", producto["color"])
        print("Tipo:", producto["tipo"])
        print("Precio:", producto["precio"])
        print()
else:
    print("No se encontraron productos coincidentes.")

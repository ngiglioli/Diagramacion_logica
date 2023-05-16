#Dado el color de un producto, su tipo y una lista de productos, se
#deberá filtrar todos los resultados que coincidan. Se deberá devolver
#los resultados como una nueva lista.

productos = [
    {"id": 1, "nombre": "Camiseta", "color": "rojo", "tipo": "ropa", "precio": 100},
    {"id": 2, "nombre": "Mesa", "color": "blanco", "tipo": "mueble", "precio": 300},
    {"id": 3, "nombre": "Silla", "color": "negro", "tipo": "mueble", "precio": 500},
    {"id": 4, "nombre": "Pantalón", "color": "azul", "tipo": "ropa", "precio": 200},
    {"id": 5, "nombre": "Cama", "color": "blanco", "tipo": "mueble", "precio": 10},
]

def filtrar_productos(color, tipo, lista_productos):
    resultados = []
    for producto in lista_productos:
        if producto['color'] == color and producto['tipo'] == tipo:
            resultados.append(producto)
    return resultados



resultados_filtrados = filtrar_productos("blanco", "mueble", productos)

if len(resultados_filtrados) > 0:
    print("Productos encontrados:")
    for producto in resultados_filtrados:
        print("ID:", producto["id"])
        print("Nombre:", producto["nombre"])
        print("Color:", producto["color"])
        print("Tipo:", producto["tipo"])
        print("Precio:", producto["precio"])
       
else:
    print("No se encontraron productos.")

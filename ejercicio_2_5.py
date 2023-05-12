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

def nueva_lista(productos,nombre):
    lista1 = []
    i = 0
    while i > len(productos):
        producto = productos [i]
        if nombre == productos:
            lista1.append(producto)
        i += 1
    return lista1

print("lista que coincide con el nombre buscado: ")
print (nueva_lista(productos,"cama"))
#Dado el color de un producto, su tipo y una lista de productos, se
#deberá retornar si existe o no un producto con esas características en
#stock.

productos = [
    {"id": 1, "nombre": "Camiseta", "color": "rojo", "tipo": "ropa", "precio": 100},
    {"id": 2, "nombre": "Mesa", "color": "blanco", "tipo": "mueble", "precio": 300},
    {"id": 3, "nombre": "Silla", "color": "negro", "tipo": "mueble", "precio": 500},
    {"id": 4, "nombre": "Pantalón", "color": "azul", "tipo": "ropa", "precio": 200},
    {"id": 5, "nombre": "Cama", "color": "blanco", "tipo": "mueble", "precio": 10},
]

def verificar_existencia(color, tipo, lista_productos):
    for producto in lista_productos:
        if producto['color'] == color and producto['tipo'] == tipo:
            return True
    return False


existe_producto = verificar_existencia("blanco", "mueble", productos)

if existe_producto:
    print("Sí existe un producto con las características buscadas en stock.")
else:
    print("No existe un producto con las características buscadas en stock.")

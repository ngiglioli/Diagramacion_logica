#Dado un producto devolver el nombre del mismo, el color y su precio.
#producto={“nombre”: “Mesa”, “color”: “negro”, “precio”: “30000”}
#Por ejemplo, deberá devolver: “Mesa negro $30000”

productos = [
    {"id": 1, "nombre": "Camiseta", "color": "rojo", "tipo": "ropa", "precio": 100},
    {"id": 2, "nombre": "Mesa", "color": "blanco", "tipo": "mueble", "precio": 300},
    {"id": 3, "nombre": "Silla", "color": "negro", "tipo": "mueble", "precio": 500},
    {"id": 4, "nombre": "Pantalón", "color": "azul", "tipo": "ropa", "precio": 200},
    {"id": 5, "nombre": "Cama", "color": "blanco", "tipo": "mueble", "precio": 10},
]

def obtener_informacion_producto(productos, nombre):
    for producto in productos:
        if producto["nombre"] == nombre:
            informacion = {
                "nombre": producto["nombre"],
                "color": producto["color"],
                "tipo": producto["tipo"],
                "precio": producto["precio"]

            }
            return informacion

    return "No existe"  # Si no se encuentra el producto, se devuelve "No existe"

    


informacion = obtener_informacion_producto(productos, "Camiseta")
print(informacion)

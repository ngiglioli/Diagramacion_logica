#Dado un precio de un producto, la cantidad de productos a entregar y la
#cantidad de productos que deberá pagar nos calcule el precio unitario
#de cada producto. Ya que están implementando promociones del tipo
#3x2, 4x2, 2x1, etc y quieren saber a cuanto queda el precio por unidad.


def precio_unitario(cant, precio):
    unidad = round(precio / cant,2)
    return unidad

print ('El precio por unidad es: ')
print (precio_unitario(3, 500))



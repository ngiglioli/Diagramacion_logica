# 2.1. Dado un precio de un producto y un porcentaje variable, nos devuelva
# el precio aumentado en dicho porcentaje. Por ejemplo, si el valor es
# 100 y aumenta en un 15% nos debería devolver $115

def precio_aum(porcentaje, precio):
    aum_porcentaje = porcentaje / 100
    precio_aumentado = round(precio * (aum_porcentaje +1),2)

    return precio_aumentado

print('El precio aumentado es: ')
print(precio_aum(25, 679))

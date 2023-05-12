#Dado un precio y su respectivo IVA, deberá calcular el precio total más
#IVA del producto. Por ejemplo, si el producto vale $100 y el IVA es del
#10,5% nos deberá devolver $110,50

def precio_aum(precio,IVA):
    porcentaje_IVA = round(1 + (IVA / 100),2) 
    precio_mas_IVA = round(precio * porcentaje_IVA,2)

    return precio_mas_IVA

print('El precio con IVA es: ')
print(precio_aum(1000,21))

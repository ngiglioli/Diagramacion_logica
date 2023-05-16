def comparacion(num1, num2):
    if num1 == num2:
        return 0
    elif num1 > num2:
        return num1
    else:
        return num2

resultado = comparacion(20, 20)
if resultado == 0:
    print('son iguales')
else:
    print(resultado)
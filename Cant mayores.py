def mayores(num1, num2, num3, num4):
    Cantmayores = 0
    numero = 5 
    if num1 > numero:
        Cantmayores = Cantmayores + 1
    
    if num2 > numero:
        Cantmayores = Cantmayores + 1
    
    if num3 > numero:
        Cantmayores = Cantmayores + 1
    
    if num4 > numero:
        Cantmayores = Cantmayores + 1
    
    return Cantmayores

print('La cantidad de mayores es: ')
print(mayores(8, 5, 6, 1))



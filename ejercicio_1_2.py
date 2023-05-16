def aprobado(nota1, nota2, nota3, nota4):
    CantAprobados = 0
    nota = 7
    if nota1 >= nota:
        CantAprobados = CantAprobados + 1
    if nota2 >= nota:
        CantAprobados = CantAprobados + 1
    if nota3 >= nota:
        CantAprobados = CantAprobados + 1
    if nota4 >= nota:
        CantAprobados = CantAprobados + 1
    return CantAprobados

print('La cantidad de aprobados es:')
print(aprobado(8, 5, 6, 10))
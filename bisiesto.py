
	
	
def anio_bisiesto(anio):
       
    if (anio % 4) == 0:
        anio_4 = True
    else:
        anio_4 = False

    if anio_4 == True:
        bisiesto = True
    else:
        bisiesto = False

    return bisiesto

if anio_bisiesto(2024) == False:
    print('El año no es bisiesto')
else:
    print('El año es bisiesto')
		

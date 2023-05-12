def resto(num):
	div3 = num%3
	div5 = num%5
		
	if div3 == 0:
		divi3 = True
	else:
		divi3 = False
	
	if div5 == 0:
		divi5 = True
	else:
		divi5 = False
	
	if divi3 or divi5 == True:
		
		return  True
	

if resto(30) == True:
    print('El número es divisible')
else:
    print('El número no es divisible')

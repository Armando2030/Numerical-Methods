def binario_Decimal(binario):
    decimal, i = 0, 0
    while(binario != 0):
        dec = binario % 10
        decimal = decimal + dec * pow(2, i)
        binario = binario//10
        i += 1
    print(decimal)

def decimal_Binario(decimal):
    parte_entera = int(decimal)
    parte_fraccion = decimal - parte_entera

 
    if parte_entera == 0:
        binario_entero = "0"
    else:
        binario_entero = ""
        while parte_entera > 0:
            residuo = parte_entera % 2
            binario_entero = str(residuo) + binario_entero
            parte_entera = parte_entera // 2


    binario_fraccion = ""
    contador = 0  
    while parte_fraccion > 0 and contador < 10:  
        parte_fraccion *= 2 
        digito = int(parte_fraccion) 
        binario_fraccion += str(digito)
        parte_fraccion -= digito
        contador += 1


    if binario_fraccion:
        binario = binario_entero + "." + binario_fraccion
    else:
        binario = binario_entero

    print(binario)


binario_Decimal(11111111)
decimal_Binario(4.25)
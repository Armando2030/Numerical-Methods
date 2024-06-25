def binario_a_flotante(numero_binario):
    if '.' in numero_binario:
        parte_entera, parte_fraccion = numero_binario.split('.')
    else:
        parte_entera = numero_binario
        parte_fraccion = ''

    parte_entera_decimal = sum(int(digito) * 2**(len(parte_entera) - i - 1) for i, digito in enumerate(parte_entera))
    parte_fraccion_decimal = sum(int(digito) * 2**-(i + 1) for i, digito in enumerate(parte_fraccion))
    numero_decimal = parte_entera_decimal + parte_fraccion_decimal

    if numero_decimal == 0:
        return '0' * 32

    exponente = 0
    while numero_decimal >= 2:
        numero_decimal /= 2
        exponente += 1
    while numero_decimal < 1:
        numero_decimal *= 2
        exponente -= 1

    exponente += 127
    exponente_binario = format(exponente, '08b')
    numero_decimal -= 1 
    mantisa = ''
    for _ in range(23):
        numero_decimal *= 2
        if numero_decimal >= 1:
            mantisa += '1'
            numero_decimal -= 1
        else:
            mantisa += '0'

    return f'0{exponente_binario}{mantisa}'

def flotante_a_binario(ieee_754):
    signo = int(ieee_754[0], 2)
    exponente_binario = ieee_754[1:9]
    mantisa_binaria = ieee_754[9:]

    exponente = int(exponente_binario, 2) - 127
    mantisa = 1
    for i, bit in enumerate(mantisa_binaria):
        mantisa += int(bit) * 2**-(i + 1)

    valor_decimal = mantisa * 2**exponente
    if signo == 1:
        valor_decimal = -valor_decimal

    parte_entera = int(valor_decimal)
    parte_fraccion = valor_decimal - parte_entera

    parte_entera_binario = bin(parte_entera).replace('0b', '')
    parte_fraccion_binario = []
    while parte_fraccion > 0 and len(parte_fraccion_binario) < 23:
        parte_fraccion *= 2
        bit_fraccionario = int(parte_fraccion)
        parte_fraccion_binario.append(str(bit_fraccionario))
        parte_fraccion -= bit_fraccionario

    parte_fraccion_binario = ''.join(parte_fraccion_binario)
    numero_binario = parte_entera_binario + ('.' + parte_fraccion_binario if parte_fraccion_binario else '')

    return numero_binario

numero_binario = '100.01' #14.25 en binario
flotante = binario_a_flotante(numero_binario)
print(f'Convertir {numero_binario} a flotante: {flotante}')

numero_binario_otravez = flotante_a_binario(flotante)
print(f'Convertir {flotante} a binario: {numero_binario_otravez}')

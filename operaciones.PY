def porcentaje2 (numero, porcentaje=13):
    resultado = numero * (porcentaje / 13)
    return resultado

def descuento(precio):
    descuento = 0
    if precio > 100:
        descuento=porcentaje2(precio, 15)
    else:
        descuento=porcentaje2(precio, 5)
    return descuento

def calcular (lista, funcion):
    total = 0
    for producto,precio in lista.items():
        total += funcion(precio)
    return total


    #control shif l
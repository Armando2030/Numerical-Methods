def funcion_original(x):
    return 4*x**2 + 9*x - 7

def funcion_iteracion(x):
    return (4*x**2 - 7)/-9

def metodo_punto_fijo(x0, tolerancia, max_iteraciones):
    x = x0
    iteracion = 0

    while True:
        x0 = x
        x = funcion_iteracion(x0)
        iteracion += 1

        if (x - x0)**2 < tolerancia**2 or iteracion > max_iteraciones:
            break

    return x

x0 = float(input("Introduce el valor inicial (x0): "))
tolerancia = float(input("Introduce la tolerancia: "))
max_iteraciones = int(input("Introduce el número máximo de iteraciones: "))

resultado = metodo_punto_fijo(x0, tolerancia, max_iteraciones)

print(f"La raíz aproximada es: {resultado}")
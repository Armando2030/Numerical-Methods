def falsa_posicion(func, a, b, tol, max_iter):
    fa = func(a)
    fb = func(b)

    if fa * fb > 0:
        print("Debe tener signos opuestos")
    c = a
    for _ in range(max_iter):
        c = b - fb * (b - a) / (fb - fa)
        fc = func(c)
        if abs(fc) < tol:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return c

def funcion(x):
    return x**3 - x - 2

a = -5
b = 5
tolerancia = 1e-6
max_iteraciones = 100
raiz = falsa_posicion(funcion, a, b, tolerancia, max_iteraciones)
print(f"La raíz aproximada es: {raiz}")

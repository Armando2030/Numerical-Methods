def f(x):
    return x**3+4*(x**2)-10

def muller(x0, x1, x2, tolerancia, max_i):
    h1 = x1 - x0
    h2 = x2 - x1
    S1 = (f(x1) - f(x0)) / h1
    S2 = (f(x2) - f(x1)) / h2
    d = (S2 - S1) / (h2 + h1)
    i = 3

    while i <= max_i:
        b = S2 + h2 * d
        D = (b**2 - 4 * f(x2) * d)**0.5

        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D

        h = -2 * f(x2) / E
        p = x2 + h

        if abs(h) < tolerancia:
            return p

        x0, x1, x2 = x1, x2, p
        h1 = x1 - x0
        h2 = x2 - x1
        S1 = (f(x1) - f(x0)) / h1
        S2 = (f(x2) - f(x1)) / h2
        d = (S2 - S1) / (h2 + h1)
        i += 1

    print("El método falló después de", max_i, "iteraciones")
    return 0


x0 = 2.5
x1 = 2.0
x2 = 2.25
tolerancia = 1e-5
max_i = 1000
p = muller(x0, x1, x2, tolerancia, max_i)
print("El valor de la raíz es:", p)
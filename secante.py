def secante(f, x0, x1, tol=1e-5, max_iter=100):
    for _ in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if f_x1 == f_x0:
            print("División por cero")
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
    
        if abs(x2 - x1) < tol:
            return x2
        
        x0, x1 = x1, x2
    
    print("No se encontró la raíz")


def funcion(x):
    return x**2 + 2*x - 8


raiz = secante(funcion, 0, 5)
print(f"La raíz aproximada es: {raiz}")

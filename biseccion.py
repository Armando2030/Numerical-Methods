def biseccion(f, a, b, tol):    
    if f(a) * f(b) >= 0:
        print("Debe tener signos opuestos")
    
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0  
        if f(c) == 0:      
            return c
        elif f(a) * f(c) < 0:
            b = c         
        else:
            a = c          
    
    return (a + b) / 2.0  

def funcion(x):
    return x**3 - x**2 + 2

a = -200
b = 300
tolerancia = 1e-5
raiz = biseccion(funcion, a, b, tolerancia)
print(f"La raíz encontrada es: {raiz}")

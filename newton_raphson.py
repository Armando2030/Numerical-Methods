def funcion(x):
    return x**3+4*(x**2)-10
 

def derivFunc(x):
    return 3*x**2+8*x
 
def newtonRaphson(x):
    h = funcion(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = funcion(x)/derivFunc(x)
         
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
     
    print("La raíz es: ","%.4f"% x)
 

x0 = -20 
newtonRaphson(x0)
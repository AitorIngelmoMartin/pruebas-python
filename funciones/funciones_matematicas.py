
def suma(a,b):
    resultado = a + b
    return resultado

def conversionEntero(a):
    try:
        x = int(a)
    except:
     print("Tenemo un poblema")
    return x  

prueba = suma (5, 2)
print(prueba)

a = input("Escribe un numero:")
v = conversionEntero(a)
if v == 50:
    print("El resultado es",v)
else:
    print("No tiene nada que ver con 50, estas a salvo")




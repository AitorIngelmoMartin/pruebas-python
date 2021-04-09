print('hola amigos')

numero = 5
numero =str (numero)
print ("Tu número es: "+numero)

numero1 = input("Escribe tu número1 a continuación: ")
numero2 = input("Escribe tu número2 a continuación: ")
4
try:
    numero1 = int (numero1)
    numero2 = int (numero2) 
except:
    print("La conversión ha fallado....")


if (0>numero1 or numero1>11) or (0>numero2 or numero2>11):
    print("Alguno de tus números no está entre [0, 10]")


print (numero1)
print (numero2)
print("--------------------------------------------------------------------------------------------------")
#Este programa consiste en adivinar un número aleatorio entre el 0 y el 99.
#Según vayas introduciendo valores, el programa te dará una písta de si te has quedado corto o has excedido el valor que buscas.
#Tras adivinar el número, te devolverá el número de intentos y el valor del número que buscabas.


#Número generado aleatoriamente al entrar
import random
numeroAleatorio = random.randint(0, 100)
intentos = 0

#Conversión de string a int
numeroIntroducido = input("Teclea el número en el 0 y el 99: ")
try:
    numeroIntroducido = int (numeroIntroducido)        
except:
    print("La conversión del número inicial ha fallado....")

#Sistema para no salirte del rango
while not 0<= numeroIntroducido <= 99:
    numeroIntroducido = input("Por favor, introduce un número entre el 0 y el 99: ")
    try:
        numeroIntroducido = int (numeroIntroducido)        
    except:
        print("La conversión del número para identificar el rango ha fallado....")

#Bucle while para adivinar el valor [sólo funciona para el número inicial]
while numeroAleatorio != numeroIntroducido:
 
        if numeroIntroducido < numeroAleatorio :
            numeroIntroducido = input("FALLO!, prueba un valor más alto... :")
            intentos += 1
            try:
                 numeroIntroducido = int (numeroIntroducido)        
            except:
                print("La conversión del número introducido ha fallado....")
        else:
            numeroIntroducido = input("FALLO!, prueba un valor más bajo... :")
            intentos += 1
            try:
                 numeroIntroducido = int (numeroIntroducido)        
            except:
                print("La conversión del número introducido ha fallado....")


#Mensaje final, lo has logrado
if numeroIntroducido == numeroAleatorio :
    print("CORRECTO! el número era el", numeroAleatorio, "has utilizado",intentos,"intentos.")   
import random

def juego_adivinanza_con_vidas():
    #Generar numero aleatorio
    numero_aleatorio = random.randint(1,30)
    vidas = 4

    print('¡Bienvenido al juego de adivinanza de número!')
    print('Debes de adivinar el número entre el 1 y el 100')
    print('Intenta adivinarlo')

    while vidas > 0:
        print(f'Vidas: {vidas}')
        numero = input('Escribe el número que esta pensando el mago: ')
        if numero.isdigit():
            numero = int(numero)
            if numero < numero_aleatorio:
                print(f'El número secreto es mayor que {numero}')
                vidas-=1
            elif numero > numero_aleatorio:
                print(f'El número secreto es menor que {numero}')
                vidas-=1
            else:
                print(f'Excelente adivinaste el número{numero} = {numero_aleatorio}')
        else:
            print('Escribe un número valido entre el 1 y el 100')
    print('Fin del juego... Te quedaste sin vidas')


def juego_adivinanza_con_intentos():
    numero_aleatorio = random.randint(1,100)
    intentos = 0
    adivinado = False

    print('¡Bienvenido al juego de adivinanza de número!')
    print('Debes de adivinar el número entre el 1 y el 100')
    print('¡Intenta adivinarlo!')

    while not adivinado:
        #Solicitar un número
        numero = input('Escribe el número entre el 1 y el 100: ')

        #validar que se aun numero
        if numero.isdigit():
            numero = int(numero) #Lo estamos pasando de texto a numero entero
            intentos += 1

            if numero < numero_aleatorio:
                print(f'El número secreto es mayor que {numero}')
            elif numero > numero_aleatorio:
                print(f'El número secreto es menor que {numero}')
            else:
                print(f'¡FELICITACIONES has ganado!, el número secreto es el: {numero} y lo has logrado en {intentos} intentos')
                adivinado = True
        else:
            print('Introduzca un número valido entre el 1 y el 100')

# juego_adivinanza_con_vidas()

# juego_adivinanza_con_intentos()
"""
crear un programa que permita realizar las operaciones basicas +,-,*,/
utilizando las funciones para cada operacion y un menu principal para desplegar
y elegir que operacion realizaremos 
"""

def sum():
    num1 =int (input('numero1 :'))
    num2 = int (input('numero2 :'))
    resultado = num1 + num2
    print(resultado)


def res():
    num1 =int (input('numero1 :'))
    num2 = int (input('numero2 :'))
    resultado = num1 - num2
    print(resultado)


def multiplicacion():
    num1 =int (input('numero1 :'))
    num2 = int (input('numero2 :'))
    resultado = num1 * num2
    print(resultado)


def division():
    num1 =int (input('numero1 :'))
    num2 = int (input('numero2 :'))
    resultado = num1 / num2
    print(resultado)

def main():
    print('MENU:')
    print('1 SUMA:')
    print('2 RESTA:') 
    print('3 MULTIPLICACION:')
    print('4 DIVISION:')

    opcion = int(input('selecciona que opcion utilizaras: '))

    if opcion == 1:
        sum()
    elif opcion == 2:
        res()
    elif opcion == 3:
        multiplicacion()
    elif opcion == 4:
        division()
    else :
        print('la opcion no es valida, inserta una opcion valida')

if __name__=='__main__':
     main()

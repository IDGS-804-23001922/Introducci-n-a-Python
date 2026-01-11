"""
crear un programa que permita realizar las operaciones basicas +,-,*,/
utilizando las funciones para cada operacion y un menu principal para desplegar
y elegir que operacion realizaremos 
"""

def suma():
    num1 =int (input('numero1:'))
    num2 = int (input('numero2'))
    resultado = num1 + num2
print(resultado)
x<

def resta():
    num1 =int (input('numero1:'))
    num2 = int (input('numero2'))
    resultado = num1 - num2
print(resultado)


def multiplicacion():
    num1 =int (input('numero1:'))
    num2 = int (input('numero2'))
    resultado = num1 * num2
print(resultado)


def division():
    num1 =int (input('numero1:'))
    num2 = int (input('numero2'))
    resultado = num1 / num2
print(resultado)

def main():
    suma()
    resta()
    multiplicacion()
    division()

if __name__=='__main__':
     main()

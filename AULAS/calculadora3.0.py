def soma(numero1,numero2):
    return float(numero1) + float(numero2)

def subtração(numero1,numero2):
    return float(numero1) - float(numero2)

def multiplicação(numero1,numero2):
    return float(numero1) * float(numero2)

def divisão(numero1,numero2):
    if (num2 == '0'):
        global repetir
        repetir = False
        return 'Usuario não pode digitar 0'
    return float(numero1) / float(numero2)


def calculadora(n1,n2,op):

    if (op == '+'):
        print(soma(n1,n2))
    elif (op == '-'):
        print(subtração(n1,n2))
    elif(op == '*'):
        print(multiplicação(n1,n2))
    elif(op == '/'):
        print(divisão(n1,n2))
    else:
        print('Operação Invalida')
        global repetir
        repetir = False

repetir = False

while repetir == False:

    num1 = input('Escreva o número 1:')
    num2 = input('Escreva o número 2:')
    if num1.isnumeric() and num2.isnumeric():
        operador = input('Escreva o operador(+,-,*,/):')
        repetir = True
        calculadora(num1,num2,operador)
    else:
        print('Operacao Invalida')


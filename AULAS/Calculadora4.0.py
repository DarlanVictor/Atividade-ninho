def soma(num1,num2):
    return float(num1) + float(num2)

def subtração(num1,num2):
    return float(num1) - float(num2)

def divisão(num1,num2):
    if (num2 == '0'):
        global repetir
        repetir = True
        return 'O número 2 não pode dividir por 0, tente novamente'    
    return float(num1) / float(num2)

def multiplicação(num1,num2):
    return float(num1) * float(num2)


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


repetir = True
while (repetir == True):

    num1 = input('Escreva o número 1:')
    if (num1.isnumeric()):
        num2 = input('Escreva o número 2:')
        if (num2.isnumeric()):
            repetir = False
            operador = input('Escreva o operador(+,-,/,*):')
            calculadora(num1, num2, operador)
        else:
            print('O número 2 é invalido, tente novamente:')
              
    else:
        print('O número 1 é invalido, tente novamente')
        

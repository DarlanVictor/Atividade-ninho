def somar(numero1,numero2):
    return float(numero1) + float(numero2)

def subtrair(numero1,numero2):
    return float(numero1) - float(numero2)

def multiplicar(numero1,numero2):
    return float(numero1) * float(numero2)

def dividir(numero1,numero2):
    return float(numero1) / float(numero2)


num1 = input('Escreva o número 1:')
num2 = input('Escreva o número 2:')

operador = input('Escreva o operador(+,-,*,/):')
if (operador == '+'):
    print(somar(num1,num2))
elif (operador == '-'):
    print(subtrair(num1,num2))
elif(operador == '*'):
    print(multiplicar(num1,num2))
elif(operador == '/'):
    print(dividir(num1,num2))
else:
    print('Operação Invalida')

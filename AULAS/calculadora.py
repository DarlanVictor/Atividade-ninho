repetir = True
while(repetir):
    num1 = (input('Digite o primeiro número:'))
    if(num1.isnumeric()):
        num1 = float(num1)

        num2 = (input('Digite o segundo número:'))
        if(num2.isnumeric()):
            num2 = float(num2)

        operador = input('Digite a operação ([+ ou SOMAR],[- ou SUBTRAIR],[/ ou DIVIDIR],[* ou MULTIPLICAR]):')
        repetir = False

        if (operador == '+' or operador.lower() == 'somar'):
            print('A soma é: ',num1+num2)
        elif (operador == '-' or operador.lower() == 'subtrair'):
            print('A subtração é: ',num1-num2)
        elif (operador == '*' or operador.lower() == 'multiplicar'):
            print('A multiplicação é: ',num1*num2)
        elif (operador == '/' or operador.lower() == 'dividir'):
            if(num2 == 0):
                repetir = True
                print('Você tentou dividir por 0, operação invalida')
            else:        
                print('A divisão é: ',num1/num2)                     
        else:
            repetir = True
            print('O operador que você digitou é invalido')
    else:
        repetir = True
        print('O operador que você digitou é invalido')

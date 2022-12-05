while(True):
    num = input('digite um número inteiro: ')
    if(num.isnumeric()):
        print('O número que você digitou é inteiro')
        break    
    else:
        print('Você não digitou um número inteiro, digite novamente:')
        
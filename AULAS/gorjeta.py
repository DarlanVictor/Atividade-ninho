#Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta
#do garçom, considerando 10% do valor da conta.
#primeira forma

#def gorjeta_garcom(valorconta):
#    print('O valor da gorjeta é:',valorconta*0.1)

#gorjeta_garcom(500)

#2 forma

def gorjeta_garcom(valorconta):
    print('O valor da gorjeta é R$:',valorconta*0.1)

valor = float(input('Digite o valor da conta R$:'))
gorjeta_garcom(valor)

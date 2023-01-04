# palavra = str(input('Digite um palavra: '))
# letra = input('insira um caractere: ')

# print('A letra {} apareceu {} vezes'.format(letra,palavra.lower().count(letra)))
def checarletra(palavra,letra):
    contador = 0
    for caractere in palavra:
        if(caractere == letra):
            contador += 1

    return contador        

palavraEscolhida = str(input('Digite um palavra: '))
letraEscolhida = input('insira um caractere: ')
print(checarletra(palavraEscolhida,letraEscolhida))

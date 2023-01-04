def compararpalavra(pal1,pal2):
     if len(pal1) > len(pal2):
         print('A maior palavra é: {}'.format(pal1))
     elif len(pal1) == len(pal2):
         print('As duas palavras tem o mesmo tamanho:')
     else:
         print('A palavra maior é {}'.format(pal2))


while (True):
    palavra1 = input('Digite uma palavra: ')
    palavra2 = input('Digite outra palavra: ')

    compararpalavra(palavra1,palavra2)



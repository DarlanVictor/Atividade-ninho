# while(True):
#     senha = input('Digite uma senha númerica de 4 até 8 digitos: ')
#     if(senha.isnumeric()):
#         if(len(senha)>= 4 and len(senha)<= 8):
#             print('Sua senha é valida.')
#             break
#         else:
#             print('Sua senha tem {} digitos.Escreva uma senha entre 4 e 8 digitos'.format(len(senha)))
#     else:
#         print('Você usou caracteres que não são números')

def checarsenha(s):
    if(s.isnumeric()):
        if(len(s)>= 4 and len(s)<= 8):
            print('Sua senha é valida.')
            global repetir
            repetir = False
        else:
            print('Sua senha tem {} digitos.Escreva uma senha entre 4 e 8 digitos'.format(len(s)))
    else:
        print('Você usou caracteres que não são números')

repetir = True
while repetir:
    senha = input('Digite uma senha númerica de 4 até 8 digitos: ')
    checarsenha(senha)
    
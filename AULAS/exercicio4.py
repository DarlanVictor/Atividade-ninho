"""""
Escreva um programa Python para contar o número de caracteres em uma string. Ir para o editor
String de amostra: 'google.com'
Resultado esperado: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""
texto = input('Digite o texto: ')
contagem = {}
for letra in texto:
    contagem[letra] = texto.count(letra)
print(texto,contagem)

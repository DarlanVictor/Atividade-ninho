nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))
media = (nota1+nota2+nota3)/3
if media < 7 and media > 5:
    print('O aluno está de RECUPERAÇÃO com média', media)
elif media <= 5:
    print('O aluno está REPROVADO com média', media)
elif media >= 7:
    print('O aluno está APROVADO com média', media)
            
def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario = horas * taxa
    else:
        h_extra = horas - 40
        salario = 40 * taxa + h_extra*(1.5*taxa)

    return salario

horastrabalhadas = input('Quantas horas você trabalhou:')
valordahora = input('Digite o valor das horas:')
total_salario = calcular_pagamento(horastrabalhadas,valordahora)
print('O valor dos seus rendimentos é:',total_salario)

def potencia(a,b):
    resultado = 1
    for numero in range(b):
        resultado = resultado * a
    return resultado

base = input('Digite a base:') 

expoente = input('Digite o expoente:')

print(potencia(int(base),int(expoente))) 
       
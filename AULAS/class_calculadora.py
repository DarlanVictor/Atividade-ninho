class Calculadora:
    
    def __init__(self):
        self.valor = ""
    
    def calcular(self,numero2,operador):
        if(operador == "+"):
            print(self.soma(numero2))

        elif(operador == "-"):
            print(self.subtrair(numero2))

        elif(operador == "/"):
            print(self.dividir(numero2))

        elif(operador == "*"):
            print(self.multiplicar(numero2))

        else:
            print("O usuario digitou um operador invalido")


    def soma(self,numero2):
        soma = self.valor + numero2
        self.valor = soma
        return soma


    def subtrair(self,numero2):
        subtrair = self.valor - numero2
        self.valor = subtrair
        return subtrair            
        

    def dividir(self,numero2):
        if(numero2 == 0):
            return "O número não pode dividir por 0"
        dividir = self.valor / numero2
        self.valor = dividir
        return dividir


    def multiplicar(self,numero2):
        multiplicar = self.valor * numero2
        self.valor = multiplicar
        return multiplicar


calculadora = Calculadora()
while(True):
    if(calculadora.valor == ""):
        calculadora.valor = int(input('Insira o número 1: '))

    operador = input('Insira o operador: ')
    n2 = int(input('Insira o número 2: '))
    

    calculadora.calcular(n2, operador)

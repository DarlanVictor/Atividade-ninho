class Conta:

    def __init__(self,titular,saldo):
        self._titular = titular
        self._saldo = saldo
    
    def getSaldo(self):
        return self._saldo
    
    def setSaldo(self,novosaldo):
        self._saldo = novosaldo
    
    def getTitular(self):
        return self._titular
    
    def setTitular(self,novotitular):
        self._titular = novotitular

conta1 = Conta("Ana", 500)

print(conta1.getSaldo())
print(conta1.getTitular())

conta1.setSaldo(800)
conta1.setTitular("Maria")

print(conta1.getSaldo())
print(conta1.getTitular())



class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se depositaron {cantidad} unidades. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")
    
    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

# Probemos la clase
cuenta = CuentaBancaria(1000)
cuenta.consultar_saldo()
cuenta.depositar(500)
cuenta.consultar_saldo()
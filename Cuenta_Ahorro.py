class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de ${cantidad:.2f} realizado.")
        else:
            print("Cantidad no válida para depósito.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad:.2f} realizado.")
        else:
            print("Cantidad no válida para retiro o saldo insuficiente.")

    def consultar_saldo(self):
        return self.saldo

# Clase derivada: CuentaAhorro
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, interes_anual):
        super().__init__(titular, saldo_inicial)  # Llamamos al constructor de CuentaBancaria
        self.__interes_anual = interes_anual  # Atributo privado

    # Método para aplicar el interés al saldo
    def aplicar_interes(self):
        interes_ganado = self.saldo * (self.__interes_anual / 100)
        self.saldo += interes_ganado
        print(f"Interés de {self.__interes_anual}% aplicado. Interés ganado: ${interes_ganado:.2f}")

    # Método para consultar el interés actual
    def obtener_interes(self):
        return self.__interes_anual


# Ejemplo de uso
cuenta = CuentaAhorro("Ana Pérez", 1000, 5)  # 5% de interés anual

print(f"Saldo inicial: ${cuenta.consultar_saldo():.2f}")
cuenta.aplicar_interes()  # Aplica el interés al saldo
print(f"Saldo después de aplicar interés: ${cuenta.consultar_saldo():.2f}")
print(f"Porcentaje de interés actual: {cuenta.obtener_interes()}%")

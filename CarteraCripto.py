class CarteraCripto:
    def __init__(self, usuario, saldo_btc=0.0):
        
        self.__usuario = usuario
        self.__saldo_btc = saldo_btc  # Inicializa el saldo en BTC
    
    def consultar_saldo(self):        # Devuelve el saldo actual en BTC.
        
        return self.__saldo_btc
    
    def comprar_btc(self, monto_usd, precio_actual_btc):

        """ Convierte la cantidad en USD a BTC según el precio actual y suma el resultado al saldo. """
        
        if monto_usd <= 0:
            raise ValueError("El monto en USD debe ser positivo.")
        
        btc_comprados = monto_usd / precio_actual_btc  # Conversión de USD a BTC
        self.__saldo_btc += btc_comprados
        print(f"Compra realizada: {btc_comprados:.8f} BTC añadidos.")
    
    def vender_btc(self, monto_btc, precio_actual_btc):
        
        """Vende BTC y calcula cuánto recibe en USD."""
        if monto_btc <= 0:
            raise ValueError("La cantidad de BTC a vender debe ser positiva.")
        
        if monto_btc > self.__saldo_btc:
            raise ValueError("No puedes vender más BTC de los que tienes.")
        
        monto_usd = monto_btc * precio_actual_btc  # Conversión de BTC a USD
        self.__saldo_btc -= monto_btc
        print(f"Venta realizada: {monto_usd:.2f} USD recibidos.")
    
# Ejemplo de uso
if __name__ == "__main__":
    cartera = CarteraCripto("Juan Perez", 0.05)
    
    print(f"Saldo inicial: {cartera.consultar_saldo():.8f} BTC")
    
    cartera.comprar_btc(1000, 50000)  # Compra de BTC con 1000 USD a 50,000 USD/BTC
    print(f"Nuevo saldo: {cartera.consultar_saldo():.8f} BTC")
    
    cartera.vender_btc(0.02, 48000)  # Venta de 0.02 BTC a 48,000 USD/BTC
    print(f"Saldo final: {cartera.consultar_saldo():.8f} BTC")

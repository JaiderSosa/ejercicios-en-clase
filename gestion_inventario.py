class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        #Verifica si hay suficiente stock para vender la cantidad solicitada.
        return self.stock >= cantidad

    def vender(self, cantidad):
        #Reduce el stock si hay disponibilidad, o muestra un mensaje de falta de stock.
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f"Venta realizada: {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}")
        else:
            print(f"No hay suficiente stock para vender {cantidad} unidades de {self.nombre}. Stock disponible: {self.stock}")

    def reabastecer(self, cantidad):
        # Aumenta el stock del producto.
        self.stock += cantidad
        print(f"Reabastecido: {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")

# Creación del producto con valores iniciales
producto = Producto("Laptop", 1200, 10)

# Operaciones s
print("Verificar si hay 5 unidades disponibles:", producto.verificar_disponibilidad(5))  # True
producto.vender(3)  # Reduce el stock a 7
print("Verificar si hay 8 unidades disponibles:", producto.verificar_disponibilidad(8))  # False
producto.vender(8)  # Debería fallar por falta de stock
producto.reabastecer(10)  # Aumenta el stock a 17
print("Verificar si hay 8 unidades disponibles:", producto.verificar_disponibilidad(8))  # True
producto.vender(8)  # Reduce el stock a 9

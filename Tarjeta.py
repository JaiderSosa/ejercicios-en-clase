class TarjetaCredito:
    def __init__(self, numero):
        self.numero = numero

    @staticmethod
    def validar_tarjeta(numero):
        
        numero = numero.replace(" ", "")  # Eliminar espacios si existen

        if not numero.isdigit():
            return False

        suma = 0
        longitud = len(numero)
        es_doble = False  

        # Recorremos los dígitos de derecha a izquierda
        for i in range(longitud - 1, -1, -1):
            digito = int(numero[i])

            if es_doble:
                digito *= 2
                if digito > 9:
                    digito -= 9

            suma += digito
            es_doble = not es_doble  # Alternamos

        # Es válida si la suma total es múltiplo de 10
        return suma % 10 == 0


# Ejemplo de uso:

numero_valido = "4539 1488 0343 6467"  # Este es un ejemplo válido
numero_invalido = "1234 5678 9012 3456"

print("¿Número válido?", TarjetaCredito.validar_tarjeta(numero_valido))     # True
print("¿Número válido?", TarjetaCredito.validar_tarjeta(numero_invalido))   # False

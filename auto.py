class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
         #Constructor de la clase Vehiculo
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0  # Inicialmente en 0

    def acelerar(self, incremento):
         #Aumenta la velocidad sin superar el límite máximo
        if self.velocidad_actual + incremento > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
            print(f"Velocidad máxima alcanzada: {self.velocidad_maxima} km/h")
        else:
            self.velocidad_actual += incremento
            print(f"Acelerando... Velocidad actual: {self.velocidad_actual} km/h")

    def frenar(self, decremento):
         #Reduce la velocidad sin bajar de 0
        if self.velocidad_actual - decremento < 0:
            self.velocidad_actual = 0
            print("El vehículo se ha detenido.")
        else:
            self.velocidad_actual -= decremento
            print(f"Frenando... Velocidad actual: {self.velocidad_actual} km/h")

    def verificar_limite(self, velocidad_limite):
         #Muestra si el vehículo supera un límite de velocidad dado
        if self.velocidad_actual > velocidad_limite:
            print(f"Advertencia: Excediendo el límite de {velocidad_limite} km/h con {self.velocidad_actual} km/h.")
        else:
            print(f"Dentro del límite de {velocidad_limite} km/h. Velocidad actual: {self.velocidad_actual} km/h.")

# Creación del vehículo
vehiculo = Vehiculo("Toyota", "Corolla", 180)

# Menú interactivo
while True:
    print("\nMenú del vehículo:")
    print("1. Acelerar")
    print("2. Frenar")
    print("3. Verificar límite de velocidad")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        incremento = int(input("Ingrese la cantidad de km/h para acelerar: "))
        vehiculo.acelerar(incremento)

    elif opcion == "2":
        decremento = int(input("Ingrese la cantidad de km/h para frenar: "))
        vehiculo.frenar(decremento)

    elif opcion == "3":
        limite = int(input("Ingrese el límite de velocidad a verificar: "))
        vehiculo.verificar_limite(limite)

    elif opcion == "4":
        print("Saliendo del sistema de monitoreo... ¡Buen viaje!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")

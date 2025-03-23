class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def verificar_aprobacion(self):
        #Determina si el estudiante aprobó (nota mínima: 60)
        return "Aprobado" if self.calificacion >= 60 else "Reprobado"

# Ejemplo de uso
estudiante1 = Estudiante("Juan Pérez", 18, 75)
estudiante2 = Estudiante("María López", 20, 50)

print(f"{estudiante1.nombre} ({estudiante1.edad} años) - {estudiante1.verificar_aprobacion()}")
print(f"{estudiante2.nombre} ({estudiante2.edad} años) - {estudiante2.verificar_aprobacion()}")

class Empleado:
    
    def __init__(self, nombre, sueldo_base):   # Inicializa los atributos
        self.__nombre = nombre
        self.__sueldo_base = sueldo_base  # Uso del setter para validar

    @property
    def nombre(self):
        """Getter para obtener el nombre del empleado."""
        return self.__nombre

    @property
    def sueldo_base(self):
        """Getter para obtener el sueldo base del empleado."""
        return self.__sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, valor):
        """Setter para validar y asignar el sueldo base."""
        if valor < 0:
            raise ValueError("El sueldo base no puede ser negativo.")
        self.__sueldo_base = valor

    def calcular_salario(self):
        """Método genérico que será sobrescrito por las clases hijas."""
        return self.__sueldo_base


class EmpleadoFijo(Empleado):
    """Empleado con sueldo fijo mensual."""
    def calcular_salario(self):
        return self.sueldo_base


class EmpleadoPorHoras(Empleado):
    """Empleado que cobra por horas trabajadas."""
    def __init__(self, nombre, sueldo_base, horas_trabajadas):
        super().__init__(nombre, sueldo_base)
        self.horas_trabajadas = horas_trabajadas  # No es un atributo protegido

    def calcular_salario(self):
        return self.sueldo_base * self.horas_trabajadas


class EmpleadoTemporal(Empleado):
    """Empleado con contrato temporal y bonificaciones."""
    def __init__(self, nombre, sueldo_base, bonificacion):
        super().__init__(nombre, sueldo_base)
        self.bonificacion = bonificacion  # No es un atributo protegido

    def calcular_salario(self):
        return self.sueldo_base + self.bonificacion


# Ejemplo de uso 
if __name__ == "__main__":
    empleados = [
        EmpleadoFijo("Ana López", 2500),
        EmpleadoPorHoras("Carlos Pérez", 15, 160),  # 15 USD/hora, 160 horas trabajadas
        EmpleadoTemporal("María García", 1800, 500)  # 1800 USD base, 500 de bonificación
    ]

    for empleado in empleados:
        print(f"Empleado: {empleado.nombre}, Salario calculado: {empleado.calcular_salario():.2f} USD")

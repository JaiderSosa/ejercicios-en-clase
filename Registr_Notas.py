class Estudiante:
    def __init__(self, nombre, codigo):
        # Inicialización de atributos privados
        self.__nombre = None
        self.__codigo = None
        self.__notas = []  # Lista para almacenar las notas del estudiante
        
        # Uso de los setters para validar los valores antes de asignarlos
        self.nombre = nombre
        self.codigo = codigo

    @property
    def nombre(self):
        """Getter para obtener el nombre del estudiante."""
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        """Setter para validar y asignar el nombre del estudiante."""
        if not valor.strip():  # Verifica que el nombre no esté vacío o solo contenga espacios
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor

    @property
    def codigo(self):
        """Getter para obtener el código del estudiante."""
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        """Setter para validar y asignar el código del estudiante."""
        if not valor.isalnum():  # Verifica que el código sea alfanumérico
            raise ValueError("El código debe ser alfanumérico.")
        self.__codigo = valor

    def agregar_nota(self, nota):
        
        if 0.0 <= nota <= 5.0:  # Las notas deben estar entre 0.0 y 5.0
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")

    def calcular_promedio(self):
        """Calcula y devuelve el promedio de las notas almacenadas."""
        if not self.__notas:  # Si no hay notas registradas, el promedio es 0.0
            return 0.0
        return sum(self.__notas) / len(self.__notas)  # Promedio de notas

    def es_aprobado(self):
        """Determina si el estudiante está aprobado con un promedio de al menos 3.0."""
        return self.calcular_promedio() >= 3.0

# Ejemplo de uso
if __name__ == "__main__":
    
    estudiante = Estudiante("Juan Perez", "ABC123")
    
    estudiante.agregar_nota(4.5)
    estudiante.agregar_nota(3.8)
    estudiante.agregar_nota(2.9)

    print(f"Promedio: {estudiante.calcular_promedio():.2f}")
    
    # Verificar si el estudiante está aprobado
    if estudiante.es_aprobado():
        print("El estudiante está aprobado.")
    else:
        print("El estudiante no está aprobado.")

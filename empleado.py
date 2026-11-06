
class Empleado:
    def __init__(self, nombre, identificacion, salario_base):
        self.nombre = nombre
        self.identificacion = identificacion
        self.salario_base = salario_base

    def calcular_salario(self):
        raise NotImplementedError(
            "Este metodo debe implementarse en las clases hijas"
        )

    def mostrar_informacion(self, mostrar_salario=False, mostrar_detalles=False):
        informacion = (
            f"Nombre: {self.nombre}\n"
            f"Identificacion: {self.identificacion}\n"
            f"Salario base: ${self.salario_base:,.2f}"
        )

        if mostrar_salario:
            informacion += (
                f"\nSalario total: ${self.calcular_salario():,.2f}"
            )

        if mostrar_detalles:
            informacion += "\nTipo de empleado: " + self.__class__.__name__

        return informacion

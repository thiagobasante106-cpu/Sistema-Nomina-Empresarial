class Nomina:

    def __init__(self):
        self.empleados = []

    # Agregar empleados a la nomina
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nombre} agregado a la nomina.")

    # Calcular el total que debe pagar la empresa
    def calcular_total_nomina(self):
        total = 0

        for empleado in self.empleados:
            total += empleado.calcular_salario()

        return total

    # Mostrar la informacion de todos los empleados
    def mostrar_nomina(self):
        print("\n========== NOMINA MENSUAL ==========")

        for empleado in self.empleados:
            print(
                empleado.mostrar_informacion(
                    mostrar_salario=True,
                    mostrar_detalles=True
                )
            )
            print("-" * 40)

        print(
            f"TOTAL A PAGAR: "
            f"${self.calcular_total_nomina():,.2f}"
        )
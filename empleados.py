
from empleado import Empleado
from bonificable import Bonificable


# Empleado con salario fijo y bonificacion por desempeno
class EmpleadoTiempoCompleto(Empleado):

    def __init__(self, nombre, identificacion, salario_base, bonificacion_desempeno):
        super().__init__(nombre, identificacion, salario_base)
        self.bonificacion_desempeno = bonificacion_desempeno

    def calcular_salario(self):
        return self.salario_base + self.bonificacion_desempeno


# Empleado que cobra segun las horas trabajadas
class EmpleadoPorHoras(Empleado):

    def __init__(self, nombre, identificacion, tarifa_hora, horas_trabajadas):
        super().__init__(nombre, identificacion, tarifa_hora)
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return self.salario_base * self.horas_trabajadas


# Empleado que recibe salario base mas comisiones por ventas
class EmpleadoComision(Empleado):

    def __init__(self, nombre, identificacion, salario_base, ventas, porcentaje_comision):
        super().__init__(nombre, identificacion, salario_base)
        self.ventas = ventas
        self.porcentaje_comision = porcentaje_comision

    def calcular_salario(self):
        comision = self.ventas * (self.porcentaje_comision / 100)
        return self.salario_base + comision


# Empleado que hereda de dos clases
class EmpleadoTiempoCompletoBonificado(EmpleadoTiempoCompleto, Bonificable):

    def __init__(self, nombre, identificacion, salario_base, bonificacion_desempeno):
        EmpleadoTiempoCompleto.__init__(
            self, nombre, identificacion, salario_base, bonificacion_desempeno
        )
        Bonificable.__init__(self)

    def calcular_salario(self):
        salario = super().calcular_salario()
        return salario + self.obtener_bonificaciones()

    def mostrar_informacion(self, mostrar_salario=False,
                             mostrar_detalles=False,
                             mostrar_bonificaciones=False):

        informacion = super().mostrar_informacion(
            mostrar_salario, mostrar_detalles
        )

        if mostrar_bonificaciones:
            informacion += (
                f"\nBonificaciones adicionales: "
                f"${self.obtener_bonificaciones():,.2f}"
            )

        return informacion

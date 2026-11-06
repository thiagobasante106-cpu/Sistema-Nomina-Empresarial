
from empleado import Empleado


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

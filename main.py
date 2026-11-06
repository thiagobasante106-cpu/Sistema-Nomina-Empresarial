from empleados import (
    EmpleadoTiempoCompleto,
    EmpleadoPorHoras,
    EmpleadoComision,
    EmpleadoTiempoCompletoBonificado
)

from nomina import Nomina


# Crear el sistema de nomina
nomina = Nomina()


# 1. Empleado de tiempo completo
empleado1 = EmpleadoTiempoCompleto(
    "Carlos Perez", "1001", 2500000, 300000
)


# 2. Empleado por horas
empleado2 = EmpleadoPorHoras(
    "Maria Lopez", "1002", 15000, 160
)


# 3. Empleado por comision
empleado3 = EmpleadoComision(
    "Juan Rodriguez", "1003", 1800000, 5000000, 5
)


# 4. Empleado de tiempo completo bonificado
empleado4 = EmpleadoTiempoCompletoBonificado(
    "Andres Gomez", "1004", 2500000, 200000
)

empleado4.agregar_bonificacion(150000)
empleado4.agregar_bonificacion(100000)


# Agregar empleados a la nomina
nomina.agregar_empleado(empleado1)
nomina.agregar_empleado(empleado2)
nomina.agregar_empleado(empleado3)
nomina.agregar_empleado(empleado4)


# Mostrar la nomina completa
nomina.mostrar_nomina()
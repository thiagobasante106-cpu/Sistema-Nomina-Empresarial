
class Bonificable:

    def __init__(self):
        self.bonificaciones = []

    def agregar_bonificacion(self, monto):
        if monto > 0:
            self.bonificaciones.append(monto)
            print(f"Bonificacion de ${monto:,.2f} agregada correctamente.")
        else:
            print("El monto de la bonificacion debe ser positivo.")

    def obtener_bonificaciones(self):
        return sum(self.bonificaciones)

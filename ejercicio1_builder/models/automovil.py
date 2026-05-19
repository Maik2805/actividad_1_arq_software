class Automovil:
    """
    Producto final.
    Clase inmutable que representa un automóvil.
    """

    def __init__(self, builder):

        self._motor = builder._motor
        self._color = builder._color
        self._llantas = builder._llantas
        self._interior = builder._interior
        self._sistema_sonido = builder._sistema_sonido
        self._gps = builder._gps
        self._techo_solar = builder._techo_solar

    # =========================
    # GETTERS
    # =========================

    @property
    def motor(self):
        return self._motor

    @property
    def color(self):
        return self._color

    @property
    def llantas(self):
        return self._llantas

    @property
    def interior(self):
        return self._interior

    @property
    def sistema_sonido(self):
        return self._sistema_sonido

    @property
    def gps(self):
        return self._gps

    @property
    def techo_solar(self):
        return self._techo_solar

    # =========================
    # MÉTODO UTILITARIO
    # =========================

    def mostrar_configuracion(self):

        print("\n=== CONFIGURACIÓN DEL AUTOMÓVIL ===")

        print(f"Motor: {self.motor}")
        print(f"Color: {self.color}")
        print(f"Llantas: {self.llantas}")
        print(f"Interior: {self.interior}")
        print(f"Sistema de sonido: {self.sistema_sonido}")
        print(f"GPS: {'Sí' if self.gps else 'No'}")
        print(f"Techo solar: {'Sí' if self.techo_solar else 'No'}")
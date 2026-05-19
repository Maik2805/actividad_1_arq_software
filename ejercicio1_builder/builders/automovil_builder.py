from interfaces.ibuilder_automovil import IBuilderAutomovil
from models.automovil import Automovil


class AutomovilBuilder(IBuilderAutomovil):
    """
    Builder concreto.
    Implementa la interfaz IBuilderAutomovil.
    """

    def __init__(self):

        # Valores por defecto
        self._motor = "Gasolina"
        self._color = "Blanco"
        self._llantas = "Estándar"
        self._interior = "Tela"
        self._sistema_sonido = "Básico"
        self._gps = False
        self._techo_solar = False

    # =========================
    # MÉTODOS DE CONFIGURACIÓN
    # =========================

    def set_motor(self, motor):
        self._motor = motor
        return self

    def set_color(self, color):
        self._color = color
        return self

    def set_llantas(self, llantas):
        self._llantas = llantas
        return self

    def set_interior(self, interior):
        self._interior = interior
        return self

    def set_sistema_sonido(self, sistema):
        self._sistema_sonido = sistema
        return self

    def set_gps(self, gps):
        self._gps = gps
        return self

    def set_techo_solar(self, techo):
        self._techo_solar = techo
        return self

    # =========================
    # CREACIÓN FINAL DEL OBJETO
    # =========================

    def build(self):
        return Automovil(self)
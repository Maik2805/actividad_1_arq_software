from abc import ABC, abstractmethod


class IBuilderAutomovil(ABC):
    """
    Interfaz Builder.
    Define el contrato que deben cumplir
    todos los builders de automóviles.
    """

    @abstractmethod
    def set_motor(self, motor):
        pass

    @abstractmethod
    def set_color(self, color):
        pass

    @abstractmethod
    def set_llantas(self, llantas):
        pass

    @abstractmethod
    def set_interior(self, interior):
        pass

    @abstractmethod
    def set_sistema_sonido(self, sistema):
        pass

    @abstractmethod
    def set_gps(self, gps):
        pass

    @abstractmethod
    def set_techo_solar(self, techo):
        pass

    @abstractmethod
    def build(self):
        pass
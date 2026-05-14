"""
Interfaz IAutomovilBuilder.

Define el contrato que debe cumplir cualquier builder de automóviles.
Permite el principio de inversión de dependencias: los clientes (Director,
main) dependen de esta abstracción, no de implementaciones concretas.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ejercicio1_builder.domain.automovil import Automovil


class IAutomovilBuilder(ABC):
    """Contrato para construir un Automovil paso a paso."""

    @abstractmethod
    def con_motor(self, motor: str) -> "IAutomovilBuilder": ...

    @abstractmethod
    def con_color(self, color: str) -> "IAutomovilBuilder": ...

    @abstractmethod
    def con_llantas(self, llantas: str) -> "IAutomovilBuilder": ...

    @abstractmethod
    def con_sistema_sonido(self, sistema: str) -> "IAutomovilBuilder": ...

    @abstractmethod
    def con_interiores(self, interiores: str) -> "IAutomovilBuilder": ...

    @abstractmethod
    def con_techo_solar(self, valor: bool = True) -> "IAutomovilBuilder": ...

    @abstractmethod
    def con_gps(self, valor: bool = True) -> "IAutomovilBuilder": ...

    @abstractmethod
    def con_asientos_calefactados(self, valor: bool = True) -> "IAutomovilBuilder": ...

    @abstractmethod
    def con_camara_reversa(self, valor: bool = True) -> "IAutomovilBuilder": ...

    @abstractmethod
    def construir(self) -> "Automovil":
        """Materializa el objeto Automovil final."""
        ...

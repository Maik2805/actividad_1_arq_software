"""
Interfaz IDirectorAutomovil.

Un director conoce un orden o "receta" de construcción. Permite reutilizar
configuraciones predefinidas (económico, deportivo, lujo, etc.) sin
acoplar al cliente con los detalles de construcción.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ejercicio1_builder.domain.automovil import Automovil


class IDirectorAutomovil(ABC):
    """Contrato de un director que produce automóviles preconfigurados."""

    @abstractmethod
    def economico(self, modelo: str) -> "Automovil": ...

    @abstractmethod
    def deportivo(self, modelo: str) -> "Automovil": ...

    @abstractmethod
    def lujo(self, modelo: str) -> "Automovil": ...

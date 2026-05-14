"""
NotificacionBase (Abstraction del patrón Bridge).

Es la clase abstracta de la cual heredan los distintos tipos de
notificación (mensaje, alerta, advertencia, confirmación). Mantiene
una referencia al Implementor (IPlataformaNotificacion) — el puente
que permite que la jerarquía de tipos varíe independientemente de
la jerarquía de plataformas.
"""
from __future__ import annotations
from abc import ABC, abstractmethod

from ejercicio2_bridge.interfaces.i_plataforma_notificacion import IPlataformaNotificacion


class NotificacionBase(ABC):
    """Abstracción raíz: define la interfaz de alto nivel."""

    def __init__(self, plataforma: IPlataformaNotificacion) -> None:
        self._plataforma: IPlataformaNotificacion = plataforma

    def cambiar_plataforma(self, plataforma: IPlataformaNotificacion) -> None:
        """Permite cambiar la plataforma en tiempo de ejecución."""
        self._plataforma = plataforma

    @abstractmethod
    def enviar(self, titulo: str, mensaje: str) -> None:
        """Cada subclase decide cómo formatea y delega al implementor."""
        ...

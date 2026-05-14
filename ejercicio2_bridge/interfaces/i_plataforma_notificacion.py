"""
IPlataformaNotificacion (Implementor del patrón Bridge).

Define el contrato que debe cumplir toda plataforma capaz de mostrar
notificaciones. Las clases concretas (escritorio, móvil, web)
implementan este contrato; la abstracción Notificacion se comunica
con ellas a través de este puente.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class IPlataformaNotificacion(ABC):
    """Interfaz del Implementor: cómo se renderiza una notificación."""

    @abstractmethod
    def mostrar(self, titulo: str, mensaje: str, nivel: str) -> None:
        """Renderiza la notificación en la plataforma concreta.

        Args:
            titulo: título visible de la notificación.
            mensaje: cuerpo del mensaje.
            nivel: 'info', 'alerta', 'advertencia' o 'confirmacion'.
        """
        ...

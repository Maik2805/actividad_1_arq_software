"""Concrete Implementor: notificaciones móviles (push)."""
from __future__ import annotations

from ejercicio2_bridge.interfaces.i_plataforma_notificacion import IPlataformaNotificacion


class PlataformaMovil(IPlataformaNotificacion):
    """Renderiza notificaciones en la barra de notificaciones del móvil."""

    def mostrar(self, titulo: str, mensaje: str, nivel: str) -> None:
        print(f"[MÓVIL]      📱 Push '{titulo}' ({nivel.upper()}): {mensaje}")

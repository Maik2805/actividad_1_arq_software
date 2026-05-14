"""Refined Abstraction: notificación de advertencia."""
from __future__ import annotations

from ejercicio2_bridge.interfaces.notificacion_base import NotificacionBase


class NotificacionAdvertencia(NotificacionBase):
    """Notificación de severidad media: previene de un problema."""

    def enviar(self, titulo: str, mensaje: str) -> None:
        self._plataforma.mostrar(
            f"⚠ ADVERTENCIA: {titulo}", mensaje, nivel="advertencia"
        )

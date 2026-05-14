"""Refined Abstraction: notificación informativa simple."""
from __future__ import annotations

from ejercicio2_bridge.interfaces.notificacion_base import NotificacionBase


class NotificacionMensaje(NotificacionBase):
    """Notificación tipo "información"."""

    def enviar(self, titulo: str, mensaje: str) -> None:
        self._plataforma.mostrar(titulo, mensaje, nivel="info")

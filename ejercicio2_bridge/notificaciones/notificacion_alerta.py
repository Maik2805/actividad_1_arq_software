"""Refined Abstraction: notificación tipo alerta."""
from __future__ import annotations

from ejercicio2_bridge.interfaces.notificacion_base import NotificacionBase


class NotificacionAlerta(NotificacionBase):
    """Notificación que llama la atención del usuario."""

    def enviar(self, titulo: str, mensaje: str) -> None:
        self._plataforma.mostrar(f"[ALERTA] {titulo}", mensaje, nivel="alerta")

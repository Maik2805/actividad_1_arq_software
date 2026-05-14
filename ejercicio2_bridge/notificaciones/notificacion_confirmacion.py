"""Refined Abstraction: notificación de confirmación de éxito."""
from __future__ import annotations

from ejercicio2_bridge.interfaces.notificacion_base import NotificacionBase


class NotificacionConfirmacion(NotificacionBase):
    """Notificación que confirma que una operación se completó."""

    def enviar(self, titulo: str, mensaje: str) -> None:
        self._plataforma.mostrar(
            f"✔ {titulo}", f"{mensaje} (operación exitosa)", nivel="confirmacion"
        )

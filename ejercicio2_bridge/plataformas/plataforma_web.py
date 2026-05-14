"""Concrete Implementor: notificaciones en navegador web (toast/banner)."""
from __future__ import annotations

from ejercicio2_bridge.interfaces.i_plataforma_notificacion import IPlataformaNotificacion


class PlataformaWeb(IPlataformaNotificacion):
    """Renderiza notificaciones como toasts o banners en el DOM."""

    def mostrar(self, titulo: str, mensaje: str, nivel: str) -> None:
        print(f"[WEB]        🌐 Toast <{nivel}> {titulo} — {mensaje}")

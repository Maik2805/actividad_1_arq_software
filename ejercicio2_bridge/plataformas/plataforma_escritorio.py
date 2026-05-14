"""Concrete Implementor: notificaciones de escritorio."""
from __future__ import annotations

from ejercicio2_bridge.interfaces.i_plataforma_notificacion import IPlataformaNotificacion


class PlataformaEscritorio(IPlataformaNotificacion):
    """Renderiza notificaciones como ventanas emergentes del SO."""

    _ICONOS = {
        "info": "💬",
        "alerta": "🔔",
        "advertencia": "⚠️",
        "confirmacion": "✅",
    }

    def mostrar(self, titulo: str, mensaje: str, nivel: str) -> None:
        icono = self._ICONOS.get(nivel, "•")
        print(f"[ESCRITORIO] {icono}  Ventana emergente: '{titulo}' -> {mensaje}")

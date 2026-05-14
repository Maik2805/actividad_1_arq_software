"""
Usuario (Colega del patrón Mediator).

El usuario SOLO conoce al mediador (vía la interfaz IChatMediator) y
nunca mantiene referencias directas a otros usuarios. Esto reduce el
acoplamiento y simplifica añadir/eliminar participantes.
"""
from __future__ import annotations
from typing import Optional

from ejercicio3_mediator.interfaces.i_chat_mediator import IChatMediator


class Usuario:
    """Participante de una sala de chat."""

    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self._mediador: Optional[IChatMediator] = None

    def set_mediador(self, mediador: Optional[IChatMediator]) -> None:
        """Asocia al usuario con un mediador (o lo desasocia con None)."""
        self._mediador = mediador

    def enviar(self, mensaje: str, destinatario: Optional[str] = None) -> None:
        """Envía un mensaje a través del mediador."""
        if self._mediador is None:
            print(f"{self.nombre}: no estoy en ninguna sala.")
            return
        self._mediador.enviar(self, mensaje, destinatario)

    def recibir(self, emisor: str, mensaje: str, privado: bool = False) -> None:
        """Callback invocado por el mediador cuando llega un mensaje."""
        etiqueta = "(privado)" if privado else ""
        print(f"   📩 [{self.nombre}] recibe de {emisor} {etiqueta}: {mensaje}")

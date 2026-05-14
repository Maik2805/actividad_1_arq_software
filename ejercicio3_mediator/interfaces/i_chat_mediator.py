"""
IChatMediator (interfaz del mediador).

Define el contrato que toda sala de chat (mediador concreto) debe
respetar. Los usuarios dependen únicamente de esta abstracción, lo
que cumple el principio de inversión de dependencias.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ejercicio3_mediator.domain.usuario import Usuario


class IChatMediator(ABC):
    """Contrato del mediador: gestiona usuarios y enrutado de mensajes."""

    @abstractmethod
    def registrar(self, usuario: "Usuario") -> None: ...

    @abstractmethod
    def eliminar(self, nombre: str) -> None: ...

    @abstractmethod
    def enviar(
        self,
        emisor: "Usuario",
        mensaje: str,
        destinatario: Optional[str] = None,
    ) -> None: ...

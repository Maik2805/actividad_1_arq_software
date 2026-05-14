"""
SalaDeChat (Concrete Mediator del patrón Mediator).

Centraliza toda la lógica de comunicación: gestión de participantes,
broadcasting, mensajes privados e historial. Los usuarios no necesitan
conocerse entre sí: el mediador resuelve a quién entregar cada mensaje.
"""
from __future__ import annotations
from datetime import datetime
from typing import Dict, List, Optional

from ejercicio3_mediator.interfaces.i_chat_mediator import IChatMediator
from ejercicio3_mediator.domain.usuario import Usuario


class SalaDeChat(IChatMediator):
    """Mediador concreto: una sala que enruta mensajes entre usuarios."""

    def __init__(self, nombre: str) -> None:
        self._nombre: str = nombre
        self._usuarios: Dict[str, Usuario] = {}
        self._historial: List[str] = []

    # ---------- Gestión de participantes ----------
    def registrar(self, usuario: Usuario) -> None:
        if usuario.nombre in self._usuarios:
            print(f"[{self._nombre}] {usuario.nombre} ya está en la sala.")
            return
        self._usuarios[usuario.nombre] = usuario
        usuario.set_mediador(self)
        self._registrar_evento(f"-- {usuario.nombre} se ha unido a {self._nombre} --")

    def eliminar(self, nombre: str) -> None:
        usuario = self._usuarios.pop(nombre, None)
        if usuario:
            usuario.set_mediador(None)
            self._registrar_evento(f"-- {nombre} ha salido de {self._nombre} --")

    # ---------- Comunicación ----------
    def enviar(
        self,
        emisor: Usuario,
        mensaje: str,
        destinatario: Optional[str] = None,
    ) -> None:
        timestamp = datetime.now().strftime("%H:%M:%S")

        if destinatario is None:
            # Difusión a todos los demás (broadcast)
            registro = f"[{timestamp}] {emisor.nombre} -> TODOS: {mensaje}"
            self._registrar_evento(registro)
            for nombre, usuario in self._usuarios.items():
                if nombre != emisor.nombre:
                    usuario.recibir(emisor.nombre, mensaje)
        else:
            # Mensaje privado
            target = self._usuarios.get(destinatario)
            if target is None:
                print(f"[{self._nombre}] El usuario '{destinatario}' no existe.")
                return
            registro = (
                f"[{timestamp}] {emisor.nombre} -> {destinatario} (privado): {mensaje}"
            )
            self._registrar_evento(registro)
            target.recibir(emisor.nombre, mensaje, privado=True)

    # ---------- Utilidades ----------
    def listar_usuarios(self) -> List[str]:
        return list(self._usuarios.keys())

    def mostrar_historial(self) -> None:
        print(f"\n--- Historial de '{self._nombre}' ---")
        for linea in self._historial:
            print("   " + linea)
        print("-" * 40)

    def _registrar_evento(self, evento: str) -> None:
        self._historial.append(evento)

"""
Punto de entrada (cliente) — Ejercicio 3: Patrón Mediator.

Ejecutar desde la carpeta raíz Diplmado:
    python -m ejercicio3_mediator.main
"""
from __future__ import annotations

from ejercicio3_mediator.domain.usuario import Usuario
from ejercicio3_mediator.mediator.sala_de_chat import SalaDeChat


def main() -> None:
    print("=" * 70)
    print("DEMOSTRACIÓN PATRÓN MEDIATOR — Sala de Chat Grupal")
    print("=" * 70)

    sala = SalaDeChat("Diplomado-Arq Software")

    # Los usuarios NO se conocen entre sí — solo conocen al mediador.
    juan = Usuario("Juan")
    maria = Usuario("María")
    carlos = Usuario("Carlos")
    laura = Usuario("Laura")

    for u in (juan, maria, carlos, laura):
        sala.registrar(u)

    print(f"\nUsuarios actuales: {sala.listar_usuarios()}\n")

    print(">> Juan envía un mensaje a TODOS:")
    juan.enviar("¡Hola equipo! ¿Listos para la entrega?")
    print("\n>> María responde a TODOS:")
    maria.enviar("Sí, estoy revisando el patrón Builder")

    print("\n>> Carlos envía un mensaje PRIVADO a Laura:")
    carlos.enviar("Pásame tus notas del Bridge, por favor", destinatario="Laura")
    print("\n>> Laura responde en PRIVADO a Carlos:")
    laura.enviar("Listo, te las envío en un momento", destinatario="Carlos")

    print("\n>> Carlos abandona la sala...\n")
    sala.eliminar("Carlos")
    print(f"Usuarios actuales: {sala.listar_usuarios()}\n")

    print(">> Juan vuelve a escribir, Carlos ya no recibe nada:")
    juan.enviar("¿Alguien ya terminó el ejercicio del Mediator?")

    sala.mostrar_historial()
    print("=" * 70)
    print("Los usuarios NUNCA referencian a otros usuarios. Todo va por el mediador.")
    print("=" * 70)


if __name__ == "__main__":
    main()

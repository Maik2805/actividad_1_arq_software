"""
Punto de entrada (cliente) — Ejercicio 2: Patrón Bridge.

Ejecutar desde la carpeta raíz Diplmado:
    python -m ejercicio2_bridge.main
"""
from __future__ import annotations

from ejercicio2_bridge.plataformas import (
    PlataformaEscritorio,
    PlataformaMovil,
    PlataformaWeb,
)
from ejercicio2_bridge.notificaciones import (
    NotificacionMensaje,
    NotificacionAlerta,
    NotificacionAdvertencia,
    NotificacionConfirmacion,
)


def main() -> None:
    print("=" * 70)
    print("DEMOSTRACIÓN PATRÓN BRIDGE — Sistema de Notificaciones")
    print("=" * 70)

    # Plataformas (Implementors)
    escritorio = PlataformaEscritorio()
    movil = PlataformaMovil()
    web = PlataformaWeb()

    print("\n--- Mismas plataformas, distintos tipos de notificación ---")
    NotificacionMensaje(web).enviar("Bienvenida", "Hola, gracias por entrar al portal")
    NotificacionAlerta(movil).enviar("Inicio de sesión", "Nuevo acceso desde Bogotá")
    NotificacionAdvertencia(escritorio).enviar("Disco lleno", "Quedan 200 MB libres")
    NotificacionConfirmacion(web).enviar("Pago realizado", "Tu transacción quedó registrada")

    print("\n--- Misma notificación, cambia de plataforma en runtime ---")
    notif = NotificacionAlerta(escritorio)
    notif.enviar("Servidor caído", "El servicio de pagos no responde")
    notif.cambiar_plataforma(movil)
    notif.enviar("Servidor caído", "El servicio de pagos no responde")
    notif.cambiar_plataforma(web)
    notif.enviar("Servidor caído", "El servicio de pagos no responde")

    print("\n" + "=" * 70)
    print("La combinación tipo × plataforma es libre y dinámica.")
    print("=" * 70)


if __name__ == "__main__":
    main()

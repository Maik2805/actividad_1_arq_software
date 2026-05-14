"""
Punto de entrada (cliente) — Ejercicio 1: Patrón Builder.

Ejecutar desde la carpeta raíz Diplmado:
    python -m ejercicio1_builder.main
"""
from __future__ import annotations

from ejercicio1_builder.builders.automovil_builder import AutomovilBuilder
from ejercicio1_builder.directors.director_automovil import DirectorAutomovil


def main() -> None:
    print("=" * 70)
    print("DEMOSTRACIÓN PATRÓN BUILDER — Configurador de Automóviles")
    print("=" * 70)

    # 1) Construcción totalmente personalizada (fluent interface)
    auto_personalizado = (
        AutomovilBuilder("Mazda CX-5")
        .con_motor("2.5L Turbo")
        .con_color("Gris titanio")
        .con_llantas("Aleación 19''")
        .con_sistema_sonido("Bose 10 parlantes")
        .con_interiores("Cuero Nappa")
        .con_techo_solar()
        .con_gps()
        .con_camara_reversa()
        .construir()
    )
    print("\n[1] Automóvil PERSONALIZADO:")
    print("   " + auto_personalizado.describir())

    # 2-4) Recetas a través del Director
    director = DirectorAutomovil()

    auto_economico = director.economico("Renault Kwid")
    print("\n[2] Automóvil ECONÓMICO (Director):")
    print("   " + auto_economico.describir())

    auto_deportivo = director.deportivo("Subaru WRX")
    print("\n[3] Automóvil DEPORTIVO (Director):")
    print("   " + auto_deportivo.describir())

    auto_lujo = director.lujo("BMW Serie 7")
    print("\n[4] Automóvil de LUJO (Director):")
    print("   " + auto_lujo.describir())

    # 5) Verificación de inmutabilidad
    print("\n[5] Verificación de INMUTABILIDAD:")
    try:
        auto_lujo.color = "Azul"  # type: ignore[misc]
    except Exception as e:
        print(f"   Objeto inmutable: no se puede modificar ({type(e).__name__})")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()

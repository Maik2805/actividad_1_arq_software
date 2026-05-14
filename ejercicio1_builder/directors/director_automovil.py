"""
DirectorAutomovil.

Encapsula configuraciones predefinidas reutilizables. El cliente solo
pide "un económico" o "un deportivo" sin conocer los detalles concretos
de construcción. El director depende únicamente de la interfaz
IAutomovilBuilder (no del builder concreto), lo que cumple el principio
de inversión de dependencias.
"""
from __future__ import annotations

from ejercicio1_builder.interfaces.i_director import IDirectorAutomovil
from ejercicio1_builder.interfaces.i_automovil_builder import IAutomovilBuilder
from ejercicio1_builder.builders.automovil_builder import AutomovilBuilder
from ejercicio1_builder.domain.automovil import Automovil


class DirectorAutomovil(IDirectorAutomovil):
    """Director con tres recetas estándar: económico, deportivo, lujo."""

    def _nuevo_builder(self, modelo: str) -> IAutomovilBuilder:
        """Fábrica interna del builder. Aislada para facilitar pruebas."""
        return AutomovilBuilder(modelo)

    def economico(self, modelo: str) -> Automovil:
        return (
            self._nuevo_builder(modelo)
            .con_motor("1.4L Gasolina")
            .con_color("Blanco")
            .con_llantas("Acero 14''")
            .construir()
        )

    def deportivo(self, modelo: str) -> Automovil:
        return (
            self._nuevo_builder(modelo)
            .con_motor("2.0L Turbo")
            .con_color("Rojo")
            .con_llantas("Aleación 18''")
            .con_sistema_sonido("Bose Premium")
            .con_interiores("Cuero deportivo")
            .con_camara_reversa()
            .construir()
        )

    def lujo(self, modelo: str) -> Automovil:
        return (
            self._nuevo_builder(modelo)
            .con_motor("3.0L V6")
            .con_color("Negro perla")
            .con_llantas("Aleación 19''")
            .con_sistema_sonido("Bang & Olufsen")
            .con_interiores("Cuero italiano")
            .con_techo_solar()
            .con_gps()
            .con_asientos_calefactados()
            .con_camara_reversa()
            .construir()
        )

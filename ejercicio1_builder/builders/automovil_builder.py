"""
Implementación concreta de IAutomovilBuilder.

Sigue el patrón fluent interface: cada método de configuración devuelve
self, lo que permite encadenar llamadas. La construcción final del
producto inmutable se realiza en construir().
"""
from __future__ import annotations
from typing import Optional

from ejercicio1_builder.interfaces.i_automovil_builder import IAutomovilBuilder
from ejercicio1_builder.domain.automovil import Automovil


class AutomovilBuilder(IAutomovilBuilder):
    """Builder concreto para crear instancias de Automovil."""

    def __init__(self, modelo: str) -> None:
        # Atributo obligatorio
        self._modelo: str = modelo
        # Valores por defecto razonables
        self._motor: str = "1.6L Gasolina"
        self._color: str = "Blanco"
        self._llantas: str = "Aluminio 16''"
        # Opcionales
        self._sistema_sonido: Optional[str] = None
        self._interiores: Optional[str] = None
        self._techo_solar: bool = False
        self._gps: bool = False
        self._asientos_calefactados: bool = False
        self._camara_reversa: bool = False

   
    def con_motor(self, motor: str) -> "AutomovilBuilder":
        self._motor = motor
        return self

    def con_color(self, color: str) -> "AutomovilBuilder":
        self._color = color
        return self

    def con_llantas(self, llantas: str) -> "AutomovilBuilder":
        self._llantas = llantas
        return self

    def con_sistema_sonido(self, sistema: str) -> "AutomovilBuilder":
        self._sistema_sonido = sistema
        return self

    def con_interiores(self, interiores: str) -> "AutomovilBuilder":
        self._interiores = interiores
        return self

    def con_techo_solar(self, valor: bool = True) -> "AutomovilBuilder":
        self._techo_solar = valor
        return self

    def con_gps(self, valor: bool = True) -> "AutomovilBuilder":
        self._gps = valor
        return self

    def con_asientos_calefactados(self, valor: bool = True) -> "AutomovilBuilder":
        self._asientos_calefactados = valor
        return self

    def con_camara_reversa(self, valor: bool = True) -> "AutomovilBuilder":
        self._camara_reversa = valor
        return self

    
    def construir(self) -> Automovil:
        """Crea y devuelve el Automovil inmutable."""
        return Automovil(
            modelo=self._modelo,
            motor=self._motor,
            color=self._color,
            llantas=self._llantas,
            sistema_sonido=self._sistema_sonido,
            interiores=self._interiores,
            techo_solar=self._techo_solar,
            gps=self._gps,
            asientos_calefactados=self._asientos_calefactados,
            camara_reversa=self._camara_reversa,
        )

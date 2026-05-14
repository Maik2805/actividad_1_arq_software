"""
Entidad de dominio: Automovil.

Es el "Producto" del patrón Builder. Se modela como dataclass congelada
(frozen=True) para garantizar inmutabilidad: una vez construido, sus
atributos no pueden modificarse.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Automovil:
    """Producto inmutable construido por un IAutomovilBuilder."""
    modelo: str
    motor: str
    color: str
    llantas: str
    sistema_sonido: Optional[str] = None
    interiores: Optional[str] = None
    techo_solar: bool = False
    gps: bool = False
    asientos_calefactados: bool = False
    camara_reversa: bool = False

    def describir(self) -> str:
        partes = [
            f"Modelo: {self.modelo}",
            f"Motor: {self.motor}",
            f"Color: {self.color}",
            f"Llantas: {self.llantas}",
        ]
        if self.sistema_sonido:
            partes.append(f"Sistema de sonido: {self.sistema_sonido}")
        if self.interiores:
            partes.append(f"Interiores: {self.interiores}")
        if self.techo_solar:
            partes.append("Techo solar: Sí")
        if self.gps:
            partes.append("GPS: Sí")
        if self.asientos_calefactados:
            partes.append("Asientos calefactados: Sí")
        if self.camara_reversa:
            partes.append("Cámara de reversa: Sí")
        return " | ".join(partes)

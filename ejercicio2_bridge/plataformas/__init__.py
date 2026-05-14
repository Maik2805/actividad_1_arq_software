"""Concrete Implementors: plataformas de despliegue."""
from .plataforma_escritorio import PlataformaEscritorio
from .plataforma_movil import PlataformaMovil
from .plataforma_web import PlataformaWeb

__all__ = ["PlataformaEscritorio", "PlataformaMovil", "PlataformaWeb"]

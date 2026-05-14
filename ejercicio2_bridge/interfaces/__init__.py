"""Contratos abstractos del módulo Bridge."""
from .i_plataforma_notificacion import IPlataformaNotificacion
from .notificacion_base import NotificacionBase

__all__ = ["IPlataformaNotificacion", "NotificacionBase"]

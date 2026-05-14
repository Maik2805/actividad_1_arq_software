"""
Ejercicio 2 - Patrón Bridge (Estructural).

Estructura del paquete:
    interfaces/        -> Abstraction (Notificacion) e Implementor (IPlataformaNotificacion)
    plataformas/       -> Concrete Implementors (escritorio, móvil, web)
    notificaciones/    -> Refined Abstractions (mensaje, alerta, advertencia, confirmación)
    main.py            -> punto de entrada / cliente
"""

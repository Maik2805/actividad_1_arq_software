# actividad_1_arq_software

## Equipo de trabajo:
- Michael Stevens Cardenas Urbano
- Juan Diego Camacho Parra
- Miguel Angel Rozo Fonseca
- Jampier Santiago Moreno Arenas
- Cesar Armando Heredia Londoño

# Escenario 1
Compañía automotriz que permite a los clientes personalizar y ordenar un automóvil.

### Típo de patrón: **Patrón Creacional**
El problema descrito corresponde a la construcción de objetos complejos, con muchos atributos opcionales, por lo que una buena forma de organizar el código para mejorar el mantenimiento y legibilidad es utilizando el patrón creacional.

### Patrón a utilizar: **Builder (Patrón Constructor)**
El patrón builder es ideal debido a que un objeto automóvil tiene muchas configuraciones (atributos) opcionales.

### Diagrama de Clases Base:
``` mermaid
  classDiagram

class Automovil {
    -modelo : String
    -motor : String
    -color : String
    -llantas : String
    -sistema_sonido : String
    -interiores : String
    -techo_solar : boolean
    -gps : boolean
    -asientos_calefactados : boolean
    -camara_reversa : boolean

    +get_modelo() String
    +get_motor() String
    +get_color() String
    +get_llantas() String
    +get_sistema_sonido() String
    +get_interiores() String
    +tiene_techo_solar() boolean
    +tiene_GPS() boolean
    +tiene_asientos_calefactados() boolean
    +tiene_camara_reversa() boolean
}

class AutomovilBuilder {
    -modelo : String
    -motor : String
    -color : String
    -llantas : String
    -sistema_sonido : String
    -interiores : String
    -techo_solar : boolean
    -gps : boolean
    -asientos_calefactados : boolean
    -camara_reversa : boolean

    +con_motor(motor : String) AutomovilBuilder
    +con_color(color : String) AutomovilBuilder
    +con_llantas(llantas : String) AutomovilBuilder
    +con_sistema_sonido(sistema : String) AutomovilBuilder
    +con_interiores(interiores : String) AutomovilBuilder
    +con_techo_solar(techo : boolean) AutomovilBuilder
    +con_gps(gps : boolean) AutomovilBuilder
    +con_asientos_calefactados(gps : boolean) AutomovilBuilder
    +con_camara_reversa(gps : boolean) AutomovilBuilder

    +construir() Automovil
}

class Main

Main --> AutomovilBuilder : usa
AutomovilBuilder --> Automovil : construye   
```

### Diagrama de Clases Extendido:
``` mermaid
  classDiagram

class Automovil {
    -modelo : String
    -motor : String
    -color : String
    -llantas : String
    -sistema_sonido : String?
    -interiores : String?
    -techo_solar : boolean
    -gps : boolean
    -asientos_calefactados : boolean
    -camara_reversa : boolean

    +describir() String
}

class IAutomovilBuilder {
    +con_motor(motor : String) IAutomovilBuilder
    +con_color(color : String) IAutomovilBuilder
    +con_llantas(llantas : String) IAutomovilBuilder
    +con_sistema_sonido(sistema : String) IAutomovilBuilder
    +con_interiores(interiores : String) IAutomovilBuilder
    +con_techo_solar(valor : boolean) IAutomovilBuilder
    +con_gps(valor : boolean) IAutomovilBuilder
    +con_asientos_calefactados(valor : boolean) IAutomovilBuilder
    +con_camara_reversa(valor : boolean) IAutomovilBuilder
    +construir() Automovil
}

class IDirectorAutomovil {
    +economico(modelo : String) Automovil
    +deportivo(modelo : String) Automovil
    +lujo(modelo : String) Automovil
}

class AutomovilBuilder {
    -_modelo : String
    -_motor : String
    -_color : String
    -_llantas : String
    -_sistema_sonido : String?
    -_interiores : String?
    -_techo_solar : boolean
    -_gps : boolean
    -_asientos_calefactados : boolean
    -_camara_reversa : boolean

    +con_motor(motor : String) AutomovilBuilder
    +con_color(color : String) AutomovilBuilder
    +con_llantas(llantas : String) AutomovilBuilder
    +con_sistema_sonido(sistema : String) AutomovilBuilder
    +con_interiores(interiores : String) AutomovilBuilder
    +con_techo_solar(valor : boolean) AutomovilBuilder
    +con_gps(valor : boolean) AutomovilBuilder
    +con_asientos_calefactados(valor : boolean) AutomovilBuilder
    +con_camara_reversa(valor : boolean) AutomovilBuilder
    +construir() Automovil
}

class DirectorAutomovil {
    +economico(modelo : String) Automovil
    +deportivo(modelo : String) Automovil
    +lujo(modelo : String) Automovil
}

class Main

IAutomovilBuilder <|.. AutomovilBuilder
IDirectorAutomovil <|.. DirectorAutomovil
Main --> AutomovilBuilder : usa
Main --> DirectorAutomovil : usa
DirectorAutomovil ..> IAutomovilBuilder : depende
DirectorAutomovil --> Automovil : construye
AutomovilBuilder --> Automovil : construye
```

Se incluyen interfaces para cumplir con el principio de inversión de dependencias, como valor añadido, se implementa un "Director de Automoviles" que incluye modelos de vehiculos preconstruidos como "plantillas".

### Ejecución del escenario:
```cmd
python -m ejercicio1_builder.main
```

# Escenario 2
Aplicación que gestiona la visualización de notificaciones en diferentes plataformas (por ejemplo: escritorio, móvil web).

### Típo de patrón: **Patrón Estructural**
El escenario indica un problema de acoplamiento entre dos dimensiones (tipos de notificación y plataformas de implementación) que evolucionan independientemente.

### Patrón a utilizar: **Bridge (Patrón Puente)**
El patrón **Bridge** es ideal debido a que permite separar la abstracción de su implementación para que ambas puedan variar de forma independiente.


### Diagrama de clases:
``` mermaid
classDiagram

class IPlataformaNotificacion {
    <<interface>>
    +mostrar(titulo : String, mensaje : String, nivel : String)
}

class PlataformaWeb {
    +mostrar(titulo : String, mensaje : String, nivel : String)
}

class PlataformaMovil {
    +mostrar(titulo : String, mensaje : String, nivel : String)
}

class PlataformaEscritorio {
    -_ICONOS : dict
    +mostrar(titulo : String, mensaje : String, nivel : String)
}

IPlataformaNotificacion <|.. PlataformaWeb
IPlataformaNotificacion <|.. PlataformaMovil
IPlataformaNotificacion <|.. PlataformaEscritorio

class NotificacionBase {
    -_plataforma : IPlataformaNotificacion
    +NotificacionBase(plataforma : IPlataformaNotificacion)
    +cambiar_plataforma(plataforma : IPlataformaNotificacion)
    +enviar(titulo : String, mensaje : String)
}

class NotificacionMensaje {
    +enviar(titulo : String, mensaje : String)
}

class NotificacionAlerta {
    +enviar(titulo : String, mensaje : String)
}

class NotificacionAdvertencia {
    +enviar(titulo : String, mensaje : String)
}

class NotificacionConfirmacion {
    +enviar(titulo : String, mensaje : String)
}

NotificacionBase <|-- NotificacionMensaje
NotificacionBase <|-- NotificacionAlerta
NotificacionBase <|-- NotificacionAdvertencia
NotificacionBase <|-- NotificacionConfirmacion

NotificacionBase --> IPlataformaNotificacion : usa
```

### Ejecución del escenario:
```cmd
python -m ejercicio2_bridge.main
```

# Escenario 3
Aplicación de chat grupal donde los usuarios pueden enviarse mensajes entre sí dentro de una sala de chat.

### Típo de patrón: **Patrón de Comportamiento**
El escenario indica un problema enfocado en cómo interactuan los objetos (usuarios), distribuir responsabilidades y reducir dependencias entre componentes.
Se necesita controlar y centralizar las interacciones.

### Patrón a utilizar: **Mediator (Patrón Mediador)**
El patrón **Mediator** es ideal debido a que su propósito es reducir las dependencias directas entre objetos que se comunican, centralizando la interacción en un objeto mediador. Esto facilita el mantenimiento, mejora la modularidad y promueve un acoplamiento débil.


### Diagrama de clases:
``` mermaid
classDiagram

class IChatMediator {
    <<interface>>
    +registrar(usuario : Usuario) : None
    +eliminar(nombre : String) : None
    +enviar(emisor : Usuario, mensaje : String, destinatario : String?) : None
}

class SalaDeChat {
    -_nombre : String
    -_usuarios : Dict[String, Usuario]
    -_historial : List[String]
    +SalaDeChat(nombre : String)
    +registrar(usuario : Usuario) : None
    +eliminar(nombre : String) : None
    +enviar(emisor : Usuario, mensaje : String, destinatario : String?) : None
    +listar_usuarios() : List[String]
    +mostrar_historial() : None
    -_registrar_evento(evento : String) : None
}

class Usuario {
    -nombre : String
    -_mediador : IChatMediator?
    +Usuario(nombre : String)
    +set_mediador(mediador : IChatMediator?) : None
    +enviar(mensaje : String, destinatario : String?) : None
    +recibir(emisor : String, mensaje : String, privado : boolean = False) : None
}

IChatMediator <|.. SalaDeChat : Implementa
Usuario --> IChatMediator : usa
SalaDeChat --> Usuario : gestiona
```

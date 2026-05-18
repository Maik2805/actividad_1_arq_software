# actividad_1_arq_software

## Equipo de trabajo:
- Michael Stevens Cardenas Urbano
- Juan Diego Camacho Parra
- Miguel Angel Rozo Fonseca
- Jampier Santiago Moreno Arenas
- Cesar Armando Heredia Londoño

# Actividad 1 
## Escenario
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
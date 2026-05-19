# actividad_1_arq_software
# Escenario 1
Compañía automotriz que permite a los clientes personalizar y ordenar un automóvil.

### Típo de patrón: **Patrón Creacional**
El problema descrito corresponde a la construcción de objetos complejos, con muchos atributos opcionales, por lo que una buena forma de organizar el código para mejorar el mantenimiento y legibilidad es utilizando el patrón creacional.

### Patrón a utilizar: **Builder (Patrón Constructor)**
El patrón builder es ideal debido a que un objeto automóvil tiene muchas configuraciones (atributos) opcionales.

Se incluye interfaz que permite el contrato con el bulder al momento de la creacion del objeto automovil y cumplir con el principio de inversión de dependencias.

✅ Legibilidad y claridad
Cada configuración del automóvil se define mediante métodos claros y descriptivos, mejorando la comprensión del código, mantenimiento y reduce errores.
Ejemplo:
.set_color("Rojo")
.set_motor("Eléctrico")

✅ Inmutabilidad
Una vez creado el objeto Automovil, sus datos no pueden modificarse porque no existen métodos set dentro de la clase final.

✅ Flexibilidad
El Builder permite agregar únicamente las configuraciones necesarias sin crear múltiples constructores o subclases.

✅ Separación de construcción y representación
La construcción se delega al AutomovilBuilder, mientras que la clase Automovil solo representa el objeto final.

### Ejecución del escenario:
python -m ejercicio1_builder.main


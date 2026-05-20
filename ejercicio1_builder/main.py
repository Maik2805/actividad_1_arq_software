from builders.automovil_builder import AutomovilBuilder


def main():

    auto_personalizado = (
        AutomovilBuilder()
        .set_motor("Eléctrico")
        .set_color("Rojo")
        .set_llantas("Deportivas")
        .set_interior("Cuero")
        .set_sistema_sonido("Bose")
        .set_gps(True)
        .set_techo_solar(True)
        .build()
    )

    auto_personalizado.mostrar_configuracion()


if __name__ == "__main__":
    main()
def estado_inicial():
    return {}

def obtener_respuesta_asistente(mensaje, estado):
    pedido = mensaje.lower().strip()

    if pedido == "lugares turisticos" or pedido == "1":
        texto = (
            "Puedes visitar de la estación 1 hasta la 9.\n"
            "También puedes visitar casas de vinos repartidas en toda La Rioja.\n"
            "Entre las más famosas: La Riojana, Valle de Las Puertas, Chañarmuyo ubicada en Chilecito, La Rioja.\n"
            "Y no te pierdas: El Cristo en Chilecito, Parque Nacional Talampaya, Dique Los Sauces y estación 1 a 9 aguas negras y una gran serie de campings."
        )
        return texto, estado

    elif pedido == "lugares para comer" or pedido == "2":
        texto = (
            "Te recomiendo:\n"
            "- Para desayunar: Rober A, Infinito y Borrusia.\n"
            "- Para merendar: Cultivo, Ciccio.\n"
            "- Para la cena: Ferrito, Como lo Como, Meztizo.\n"
            "- Opción juvenil y comidas rápidas: Gorilla, Yuli Comidas y El Manhar."
        )
        return texto, estado

    elif pedido == "lugares para pasar el rato" or pedido == "3":
        texto = "Puedes ir a: Plaza Principal, El Cristo, El Parque de la Ciudad, El Dique Los Sauces."
        return texto, estado

    elif pedido == "salir" or pedido == "4":
        texto = (
            "¡Gracias por visitar nuestra hermosa provincia! "
            "Este proyecto fue hecho por alumnos de 5to año de la escuela privada Jean Piaget: "
            "Irina González, Aldana Gallardo, Luján Morales, Ramiro González, Bruno Olivera. "
            "¡Que disfrutes Chilecito, La Rioja!"
        )
        return texto, estado

    else:
        return "Pregunta errónea, intentá de nuevo escribiendo 1, 2, 3 o 4.", estado
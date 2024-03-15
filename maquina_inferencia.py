class MaquinaInferencia:
    def __init__(self):
        self.base_conocimientos = {
            "Asma": [
                ("¿Ha tenido tos persistente?", 0.1),
                ("¿Ha presentado dificultad para respirar?", 0.1),
                ("¿Ha tenido episodios recurrentes de tos?", 0.1),
                ("¿Ha presentado una opresión en el pecho?", 0.1),
                ("¿Ha observado tener dificultad para realizar actividades físicas?", 0.1),
                ("¿Ha presentado fatiga extrema sin razón aparente?", 0.1),
                ("¿Ha observado cambios en la voz o ronquera persistente?", 0.1),
                ("¿Tiene familiares con antecedentes  de enfermedades respiratorias?", 0.1),
                ("¿Ha tenido exposición frecuente a alérgenos como polen o ácaros?", 0.1),
                ("¿Ha observado que tiene dificultad respiratoria después de exposición al humo?", 0.1),
            ]
        }

    # Método para realizar las preguntas del objeto
    def hacer_preguntas(self):
        # Objeto para guardar la respuesta del usuario
        respuestas = {}

        # Obtener la única enfermedad en la base de conocimientos
        enfermedad = list(self.base_conocimientos.keys())[0]

        # Recorrer las preguntas
        for pregunta, probabilidad in self.base_conocimientos[enfermedad]:
            respuesta = input(f"{pregunta}: Sí o No? ").lower()
            # Si la respuesta es sí, guardar la probabilidad; de lo contrario, 0
            respuestas[pregunta] = probabilidad if respuesta == "sí" else 0

        # Calcular la probabilidad total
        probabilidad_total = sum(respuestas.values())

        return enfermedad, probabilidad_total


if __name__ == "__main__":
    maquina = MaquinaInferencia()

    print("Por favor, responde las siguientes preguntas con Sí o No:")

    enfermedad_diagnosticada, probabilidad = maquina.hacer_preguntas()

    if enfermedad_diagnosticada:
        print(
            f"\nBasado en tus respuestas, hay un {probabilidad * 100}% de probabilidad de tener {enfermedad_diagnosticada}"
        )
    else:
        print(
            "\nNo se pudo determinar la enfermedad. Consulta a un profesional de la salud para un diagnóstico preciso."
        )

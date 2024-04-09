from openai import OpenAI


def generative_ai_question(question_date):
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
              "role": "system",
              "content": "Tu role es un experto periodista e historiador que sabe sobre todos los acontecimientos históricos del mundo, más especializado en el campo tecnológico."
            },
            {
                "role": "user",
                "content": f'''
                Sabrías decirme un hecho histórico tecnológico que sucediera el {question_date}.
                
                Si no existe ningún acontecimiento historico tecnológico, muestrame uno genérico que pasara
                en el mundo.

                Necesot del acontecimiento historico, un titular descriptivo y una pequeña descripción de 200 palabras.
                Añade también que me añadas algunos tags (mínimo 5) para así poderlo tratar en redes sociales como hashtags (no quiero el #!!).

                Me lo podrías devolver en formato JSON? Quiero que me devuelvas los datos en formato JSON, siguiendo la estructura:
                {{
                  "titular": "EL TITULAR",
                  "hecho": "DESCRIPCIÓN DEL HECHO HISTÓRICO",
                  "tipo": "INDICA SI ES TECNOLOGICO O NO",
                  "fecha": "FECHA DEL HECHO",
                  "tags": "['TAG1', 'TAG2', 'TAG3', 'TAG4', 'TAG5']"
                }}

                Repito, e insisto mucho en este punto! la fecha tiene que ser para el {question_date}!!, no te
                inventes el dato, tiene que ser PRECISO, si no te sabes una noticia no te preocupes, dame otra genérica.

                Importante: Unicamente quiero que me devuelvas una respuesta en formato JSON! sin nada más, JSON puro! 
                escupeme el resultado directo, sin json por delante ni nada!
              '''
            },
        ],
    )

    return response.choices[0].message.content
from utils.login import openai_client

def generate_caption(prompt):
    '''generate caption'''
    try:
        chat_completion = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Estás generando un pie de foto con temática cyberpunk."
                },
                {
                    "role": "user",
                    "content": f"""Genera un pie de foto con temática cyberpunk
                    para una imagen que {prompt}.
                    Genera la misma frase en español, y en un segundo párrafo en inglés.
                    Agrega en untercer párrafo 7 hashtags en inglés sobre la temática de la foto"""
                }
            ],
            max_tokens=500,
            temperature=0.7,
        )
        caption = chat_completion.choices[0].message.content.strip()
        return caption
    except Exception as e:
        print(f"Error al generar el pie de foto: {e}")

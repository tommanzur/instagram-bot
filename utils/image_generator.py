import requests
import os
from PIL import Image
from io import BytesIO
from utils.login import openai_client

def generate_image(prompt, filename):
    '''Generate image'''
    filename = f"{filename}.jpg"
    try:
        response = openai_client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        download_image(image_url, filename)
    except Exception as e:
        print(f"Error al generar la imagen: {e}")
        return None

def download_image(url_image, filename):
    '''Download image and save as JPG'''
    try:
        os.makedirs("./data", exist_ok=True)
        response = requests.get(url_image)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content))
        filepath = os.path.join("./data", filename)
        image.save(filepath, "JPEG")

    except Exception as e:
        print(f"Error al descargar la imagen: {e}")

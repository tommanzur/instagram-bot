from utils.login import bot
from utils.generate_prompt import generate_image_prompt
from utils.caption_generator import generate_caption
from utils.image_generator import generate_image

image_name, prompt = generate_image_prompt()
caption = generate_caption(prompt)
generate_image(prompt, image_name)

try:
    bot.upload_photo(
        f"./data/{image_name}.jpg",
        caption=caption,
        )
except Exception as e:
    print(e)

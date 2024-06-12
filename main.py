import eel
import base64
import io
import os
from mainapp import *


eel.init('web')

@eel.expose
def encrypt_image(data_url, text, key):
    # Extract the base64-encoded image data from the data URL
    _, encoded_image = data_url.split(",", 1)
    image_bytes = base64.b64decode(encoded_image)

    # Use BytesIO to convert the bytes to a file-like object
    image_file = io.BytesIO(image_bytes)

    # Generate a unique filename for the temporary image
    temp_image_filename = f"temp_image.png"
    temp_image_path = os.path.join(os.path.dirname(__file__), "web/static", temp_image_filename)

    try:
        with open(temp_image_path, "wb") as temp_image_file:
            temp_image_file.write(image_file.read())

        print(f"Temp image saved: {temp_image_path}")
        print("Encrypting image...")
        result_data = Encryption(image_file, text, key)

        # Convert the Image object to bytes
        result_bytes = io.BytesIO()
        result_data.save(result_bytes, format="PNG")
        result_bytes = result_bytes.getvalue()

        # Encode the result image data as base64
        result_base64 = base64.b64encode(result_bytes).decode('utf-8')

        print("Encryption complete.")
        return result_base64
    finally:
        # # Delete the temporary files after processing
        # os.remove(temp_image_path)
        # print(f"Temp image deleted: {temp_image_path}")
        # os.remove(temp_image_path)
        # print(f"Temp image deleted: {temp_image_path}")
        pass

@eel.expose
def decrypt_image(data_url, key):
    # Extract the base64-encoded image data from the data URL
    _, encoded_image = data_url.split(",", 1)
    image_bytes = base64.b64decode(encoded_image)

    # Use BytesIO to convert the bytes to a file-like object
    image_file = io.BytesIO(image_bytes)

    # Generate a unique filename using uuid
    temp_filename = f"temp_stego_image.png"
    temp_filepath = os.path.join(os.path.dirname(__file__), temp_filename)

    try:
        with open(temp_filepath, "wb") as temp_stego_image:
            temp_stego_image.write(image_file.read())

        print(f"Temp stego image saved: {temp_filepath}")
        print("Decrypting image...")
        return Decryption(temp_filepath, key)
        print("Decryption complete.")
    finally:
        # Delete the temporary file after processing
        os.remove(temp_filepath)
        print(f"Temp stego image deleted: {temp_filepath}")

eel.start('home.html')
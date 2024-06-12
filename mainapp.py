from AESCryptography import AESencrypt,AESdecrypt
from LSBSteganography.Steganography_Encryption import StegoEncryption
from LSBSteganography.Steganography_Decryption import StegoDecryption

import os

def Encryption(coverimage, data, key=0):
    ciphertext = AESencrypt.encrypt(data, key)
    newimage = StegoEncryption.encode(coverimage, *ciphertext)


    result_filename = f"result_image.png"
    # result_image_path = os.path.join(os.path.dirname(__file__), 'web', 'static', result_filename)
    result_image_path = os.path.join(os.path.dirname(__file__), 'static', 'images', result_filename)

    newimage.save(result_image_path)

    # return newimage
    return result_image_path

def Decryption(stegoimage, key=0):

    ciphertext = StegoDecryption.decode(stegoimage)

    print(ciphertext)
    data = AESdecrypt.decrypt(ciphertext, key)

    return data

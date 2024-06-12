# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,send_file
from mainapp import Encryption, Decryption
import os
import io

# Initialize Flask application
app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling encryption

@app.route('/encrypt', methods=['POST'])
def encrypt():
    if request.method == 'POST':
        # Get the file data from the form
        coverimage = request.files['coverimage']
        data = request.form['data']
        key = request.form['key']
        
        # Read the file data into memory
        coverimage_data = coverimage.read()
        
        # Encrypt the data and save the encrypted image to a file
        encrypted_image_path = Encryption(io.BytesIO(coverimage_data), data, key)
        
        # Send the encrypted image file to the client
        return send_file(encrypted_image_path, mimetype='image/png', as_attachment=True)

    
# Route for handling decryption
@app.route('/decrypt', methods=['POST'])
def decrypt():
    if request.method == 'POST':
        stego_image = request.files['stegoImage']
        key = request.form['key']

        # Assuming your Decryption class requires stegoimage and key
        decryption = Decryption(stego_image, key)
        decrypted_data = decryption

        # Simply return the decrypted data as a response
        return decrypted_data

    else:
        return 'Method Not Allowed', 405


if __name__ == '__main__':
    app.run(debug=True)

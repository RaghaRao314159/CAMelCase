from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
from model import gen_voice, allowed_file
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload_file():
    if 'text' not in request.form:
        print('No text part')
        return 'error, No text part'

    text = request.form['text']

    if text == '': 
        print('Empty notification')
        return 'error, Empty notification'

    if 'file' not in request.files:
        print('No file part')
        return 'No file part'

    file = request.files['file']
    
    if file.filename == '': 
        print('No selected file')
        return 'No selected file'

    print(allowed_file(file.filename))
    if file and allowed_file(file.filename):
        # Save the file to a desired location
        #latest_message = handle_android_post()
        #Call AI
        #audio = gen_voice(path, "latest_message")

        file_path = os.path.join('/Users/ragharao/Desktop/CAMelCase/Web_Innovatio/', file.filename)
        print(file_path)
        file.save(file_path)

        gen_voice(file_path, text, file_path)


        # Return the uploaded file as a response
        return send_file(file_path, as_attachment=True)
        #return send_file(file, as_attachment=True)
    print('Invalid file format')
    return 'Invalid file format'

    
if __name__ == "__main__":
    app.run(debug=True)
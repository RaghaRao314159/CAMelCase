from flask import Flask, render_template, request, redirect, url_for, send_file
from model import gen_voice, allowed_file
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def upload_file():
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

        file_path = os.path.join('/Users/ragharao/Desktop/CAMelCase/Web_Innovatio', file.filename)
        print(file_path)

        file.save(file_path)
        # Return the uploaded file as a response
        return send_file(file_path, as_attachment=True)
        #return send_file(file, as_attachment=True)
    print('Invalid file format')
    return 'Invalid file format'


def allowed_file(filename):
    # Check if the file has an allowed extension (e.g., MP3)
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp3'}








'''

@app.route('/',methods=['POST','GET'])
def contactpage():
    if  request.method == 'POST':
        if request.form.get('name'):
            name = request.form.get('name')
            number = request.form.get('number')
            description = request.form.get('description')
            audio_file = request.files['audio_file']
            # Save the uploaded file to the 'uploads' directory
            audio_file.save(audio_file.filename)

            contact = f"{audio_file.filename}"

            #print("ptint everything: ",name, number, description, mp3_path)

            return render_template('contactpage.html', name = name, contact = contact)
        
        elif request.form.get('friend_box'):
            global friend
            friend = request.form.get('friend_box')
            print("this is what you typoed into the box: ", friend)
            global friend_convo
            global me_convo
            friend_convo = []
            me_convo = []
            return render_template('me.html', friend = friend, me_convo = me_convo, friend_convo = friend_convo)

        elif request.form.get('clear_audio'):
            print ('Request has been met!')
            for filename in os.listdir('/'):
                print (filename)
                if filename.endswith(".mp3"):
        
                    os.remove(filename)

    return render_template('contactpage.html')


@app.route('/me',methods=['POST','GET'])
def me():
    global friend
    global me_convo
    global friend_convo
    if 'value' in request.form:
        global path
        if request.form['value']:
            path = request.form['value']

        print("initial set: ", path)

    
    if request.method == 'POST':

        if request.form.get('back'):
            print("Run this ")
            return render_template('contactpage.html')
        
        if request.form.get('me_message'):
            me_message = request.form.get('me_message')
            me_convo.append(me_message)
            return render_template('me.html', me_convo = me_convo, friend_convo = friend_convo, friend = friend)

    if request.method == 'GET':
        if len(friend_convo) != 0:
            latest_message = friend_convo[-1]
            print("final check: ",path)
            gen_voice(path, latest_message)
        return render_template('me.html', me_convo = me_convo, friend_convo = friend_convo, friend = friend)

    return render_template('me.html', friend = friend)


@app.route('/friend',methods=['POST','GET'])
def friend():
    global friend_convo
    global me_convo
    if request.method == 'POST':
        if request.form.get('friend_message'):
            friend_message = request.form.get('friend_message')
            friend_convo.append(friend_message)
            return render_template('friend.html', me_convo = me_convo, friend_convo = friend_convo)
    
    if request.method == 'GET':
        return render_template('friend.html', me_convo = me_convo, friend_convo = friend_convo)

    return render_template('friend.html', me_convo = me_convo, friend_convo = friend_convo)

'''

@app.route('/audio')
def serve_audio():
    return send_file("Gen_voice.mp3", as_attachment=True)

@app.route('/favicon')
def favicon():
    return send_file("templates/favicon.ico", as_attachment=True)

    
if __name__ == "__main__":
    path = ""
    friend = ""
    me_convo, friend_convo = [], []
    app.run(debug=True)
from elevenlabs import generate, play, set_api_key, clone


def allowed_file(filename):
    # Check if the file has an allowed extension (e.g., MP3)
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp3'}


def gen_voice(abs_path, text, save_path):
    set_api_key("1c1780f87b362547e1dab31485e76afb")

    kash_sound_url = abs_path.replace('\\', '/')

    voice = clone(
        name="Alex",
        description="An indian student who lives in Singapore", # Optional
        files=[kash_sound_url]
    )

    audio = generate(text=text, voice=voice)

    
    with open(save_path, 'wb') as f:
        f.write(audio)

from flask import Flask, request, jsonify
from flask_cors import CORS
from speech_to_text import SpeechToText
from phrase_handler import PhraseHandler

app = Flask(__name__)
CORS(app)  # Enable CORS

videos_directory = "path/to/Videos"
alphabet_directory = "path/to/Alphabet"
stt = SpeechToText()
handler = PhraseHandler(videos_directory, alphabet_directory)

@app.route('/listen', methods=['GET'])
def listen():
    audio_data = stt.listen()
    return jsonify({"message": "Audio received, processing...", "status": "success"}), 200

@app.route('/recognize', methods=['GET'])
def recognize():
    audio_data = stt.listen()
    phrase = stt.recognize_speech(audio_data)
    if phrase:
        handler.search_and_play(phrase)
        handler.clear_cache()
        return jsonify({"phrase": phrase, "status": "success"}), 200
    else:
        return jsonify({"message": "Sorry, I couldn't understand. Please try again.", "status": "error"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

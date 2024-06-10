from flask import Flask, jsonify
from flask_cors import CORS
from speech_to_text import SpeechToText
from phrase_handler import PhraseHandler

app = Flask(__name__)
CORS(app)  # Enable CORS

videos_directory = "Data-Set/Videos"
alphabet_directory = "Data-Set/Alphabet"
stt = SpeechToText()
handler = PhraseHandler(videos_directory, alphabet_directory)

@app.route('/recognize', methods=['GET'])
def recognize():
    stt.listen()
    return jsonify({"message": "Listening started, say something...", "status": "listening"}), 200

@app.route('/stop', methods=['GET'])
def stop():
    stt.stop()
    phrase = stt.recognize_speech()
    if phrase:
        video_path, gif_path = handler.search_and_return_paths(phrase)
        handler.clear_cache()
        return jsonify({"phrase": phrase, "video": video_path, "gif": gif_path, "status": "success"}), 200
    else:
        return jsonify({"message": "Sorry, I couldn't understand. Please try again.", "status": "error"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

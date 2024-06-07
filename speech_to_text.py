import speech_recognition as sr

class SpeechToText:
    def __init__(self, recognizer=None, microphone=None):
        self.recognizer = recognizer if recognizer else sr.Recognizer()
        self.microphone = microphone if microphone else sr.Microphone()

    def listen(self):
        with self.microphone as source:
            print("Adjusting for ambient noise, please wait...")
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)
        return audio

    def recognize_speech(self, audio):
        try:
            print("Recognizing...")
            text = self.recognizer.recognize_google(audio)
            print(f"Google Speech Recognition thinks you said: {text}")
            return text.lower()  # Convert to lowercase for easier comparison
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

if __name__ == "__main__":
    stt = SpeechToText()
    audio_data = stt.listen()
    text = stt.recognize_speech(audio_data)
    print(text)

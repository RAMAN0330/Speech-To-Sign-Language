import os
import random
import cv2
from PIL import Image
import diskcache as dc
import time

class PhraseHandler:
    def __init__(self, videos_dir, alphabet_dir):
        self.videos_dir = videos_dir
        self.alphabet_dir = alphabet_dir
        self.cache = dc.Cache('cache_directory')  # Cache directory

    def search_and_play(self, phrase):
        phrase_dir = os.path.join(self.videos_dir, phrase.lower())
        if os.path.exists(phrase_dir) and os.path.isdir(phrase_dir):
            video_files = [f for f in os.listdir(phrase_dir) if f.endswith(('.mp4', '.avi', '.mov'))]
            if video_files:
                selected_video = random.choice(video_files)
                video_path = os.path.join(phrase_dir, selected_video)
                self.cache.set('video', video_path)
                self.play_video(video_path)
                return
        self.cache.set('phrase', phrase)
        self.display_alphabet_images(phrase)

    def play_video(self, video_path):
        print(f"Playing video: {video_path}")
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"Error opening video file: {video_path}")
            return

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow('Video', frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def display_alphabet_images(self, phrase):
        images = []
        for char in phrase:
            char_dir = os.path.join(self.alphabet_dir, char.upper())
            if os.path.exists(char_dir):
                for root, _, files in os.walk(char_dir):
                    if files:
                        file_path = os.path.join(root, files[0])
                        image = cv2.imread(file_path)
                        images.append(image)
                        self.cache.set(f'image_{char}', image)
                        break

        for img in images:
            cv2.imshow('Alphabet Image', img)
            cv2.waitKey(1000)  # Display each image for 1 second
        cv2.destroyAllWindows()

    def clear_cache(self):
        print("Clearing cache")
        self.cache.clear()

if __name__ == "__main__":
    videos_directory = "path/to/Videos"
    alphabet_directory = "path/to/Alphabet"
    handler = PhraseHandler(videos_directory, alphabet_directory)
    handler.search_and_play("example")
    handler.clear_cache()

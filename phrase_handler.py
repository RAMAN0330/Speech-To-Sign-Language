import os
import random
import diskcache as dc
import imageio
from PIL import Image


class PhraseHandler:
    def __init__(self, videos_dir, alphabet_dir):
        self.videos_dir = videos_dir
        self.alphabet_dir = alphabet_dir
        self.cache = dc.Cache('cache_directory')  # Cache directory

    def search_and_return_paths(self, phrase):
        phrase_dir = os.path.join(self.videos_dir, phrase.lower())
        video_path = None
        gif_path = None

        if os.path.exists(phrase_dir) and os.path.isdir(phrase_dir):
            video_files = [f for f in os.listdir(phrase_dir) if f.endswith(('.mp4', '.avi', '.mov'))]
            if video_files:
                selected_video = random.choice(video_files)
                video_path = f"static/{os.path.join(phrase_dir, selected_video)}"
                self.cache.set('video', video_path)

        if not video_path:
            self.cache.set('phrase', phrase)
            gif_path = self.create_alphabet_gif(phrase)

        return video_path, gif_path

    def create_alphabet_gif(self, phrase):
        images = []
        for char in phrase:
            char_dir = os.path.join(self.alphabet_dir, char.upper())
            if os.path.exists(char_dir):
                for root, _, files in os.walk(char_dir):
                    if files:
                        file_path = os.path.join(root, files[0])
                        images.append(imageio.imread(file_path))
                        self.cache.set(f'image_{char}', file_path)
                        break

        if images:
            gif_path = f"static/gifs/{phrase}.gif"
            os.makedirs(os.path.dirname(gif_path), exist_ok=True)
            imageio.mimsave(gif_path, images, duration=1)  # Save as GIF with 1 second duration per image
            return gif_path

        return None

    def clear_cache(self):
        print("Clearing cache")
        self.cache.clear()

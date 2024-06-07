# Speech to Text Video/Image Search Application

## Description

This project involves creating a speech-to-text application that integrates with a video and image dataset. The application listens to a user's speech, converts it to text, and then searches for corresponding phrases in a predefined video dataset. If a matching phrase is found, the application plays a video from the phrase's directory. If the phrase is not found, it displays images representing each character in the phrase.

The application is built using Python, leveraging Flask to create an API that can be called from a JavaScript front-end. The speech-to-text conversion is handled using the `speech_recognition` library, while videos and images are processed using OpenCV. Caching is used to ensure memory efficiency and real-time performance.

## Prerequisites

- Python 3.x
- `speech_recognition` library
- `opencv-python` library
- `Pillow` library
- `diskcache` library
- Flask
- Flask-Cors

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/speech-to-text-video-search.git
    cd speech-to-text-video-search
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set the paths for your video and alphabet directories:**

    Edit the `videos_directory` and `alphabet_directory` variables in both `phrase_handler.py` and `app.py` to point to your respective directories.

## Usage

1. **Run the Flask API:**

    ```bash
    python app.py
    ```

2. **Open the HTML file:**

    Open `index.html` in a web browser.

3. **Interact with the application:**

    - Click the "Listen" button to start listening for speech.
    - Click the "Recognize" button to process the recorded speech and display the corresponding video or images.

## Project Structure

- `app.py`: Flask API for handling speech-to-text and phrase search requests.
- `speech_to_text.py`: Handles speech recognition using the `speech_recognition` library.
- `phrase_handler.py`: Handles searching for phrases in the video dataset and displaying videos or images.
- `index.html`: Simple JavaScript client to interact with the Flask API.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

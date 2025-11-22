# Simple-Python-Voice-to-Text
Using speech_recognition and pyttsx3, it converts speech to text and saves it to a file.
Voice to Text Project

This project uses Python to convert spoken words into written text. It listens through the system microphone, processes the audio, and saves the transcribed text to a file. It also includes basic text-to-speech so the program can speak simple responses.

Features

• Converts speech to text
• Uses text-to-speech for feedback
• Saves each transcription in a text file
• Simple and easy to run on any machine with Python

Technologies Used

• Python
• speech_recognition
• pyttsx3

How It Works

The program activates the microphone and waits for the user to speak.

The audio is processed through the speech recognition library.

The recognized text is printed and added to a file.

The program uses pyttsx3 to respond with a spoken message.

Installation

Install Python

Install the required libraries

pip install speechrecognition pyttsx3 pyaudio


Note: You may need additional steps to install PyAudio depending on your system.

Running the Program

Run the Python file from your terminal

python main.py


Speak when prompted. The text will appear on screen and be added to the output file.

File Output

All transcribed text is stored in a simple text file. Each new line in the file represents a new recorded phrase.

Future Improvements

• Add noise reduction
• Add support for multiple languages
• Add a small interface

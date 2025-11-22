# Voice to Text Python Project

This is a small Python program that listens through the microphone, converts speech to text, and saves the output in a text file. It also uses a basic text-to-speech engine to give short voice feedback.

## Features

* Converts spoken audio into text
* Speaks simple responses
* Saves each transcription to a file
* Easy to run on any machine with Python installed

## Requirements

* Python 3
* speech_recognition
* pyttsx3
* pyaudio

Install the required libraries:

```
pip install speechrecognition pyttsx3 pyaudio
```

## How to Run

```
python speechtotext.py
```

Speak when the program is ready. Your words will appear in the terminal and will also be written to a text file.

## File Output

All recognized text is saved in a single text file. Each entry is added on a new line.

## How It Works

The program waits for microphone input, sends the audio to the speech recognition engine, prints the result, and appends it to a file. It uses pyttsx3 to give short voice prompts.

## Possible Improvements

* Better noise handling
* Option for different languages
* A small graphical interface    

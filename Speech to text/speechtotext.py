import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()

def record_text():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.listen(source2)

                text = r.recognize_google(audio2)

                text = text.lower()

                return text

         
        except sr.RequestError:
            print("Network error. Please check your internet connection.")
        
        except sr.UnknownValueError:
            print("Could not understand the audio. Please try again.")
    return

def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")
    return

while True:
    text=record_text()
    output_text(text)

    print("Text recorded and outputted.")
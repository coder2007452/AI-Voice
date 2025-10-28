import speech_recognition as sr
import pyttsx3
import os
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen to the user's command and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("🧠 Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"👉 You said: {query}\n")
    except sr.UnknownValueError:
        print("❌ Sorry, I didn’t catch that. Please say again.")
        return ""
    return query.lower()

def run_assistant():
    speak("Hello! I am your AI voice assistant. How can I help you?")

    while True:
        query = take_command()

        if 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")

        elif 'open notepad' in query:
            speak("Opening Notepad...")
            os.system("notepad.exe")

        elif 'open calculator' in query:
            speak("Opening Calculator...")
            os.system("calc.exe")

        elif 'time' in query:
            time_str = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time_str}")

        elif 'date' in query:
            date_str = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {date_str}")

        elif 'hello' in query:
            speak("Hello there! How are you?")

        elif 'thank you' in query:
            speak("You're welcome!")

        elif 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye! Have a nice day.")
            break

        elif query != "":
            speak("Sorry, I didn't understand that. Please try again.")

# Run the assistant
if __name__ == "__main__":
    run_assistant()

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak out the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice commands
def recognize_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        command = None

    return command

# Function to execute commands based on user input
def execute_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")

    elif "search image" in command:
        search_query = command.split("search image")[-1].strip()
        url = f"https://www.google.com/search?tbm=isch&q={search_query}"
        webbrowser.open(url)
        speak(f"Here are the image search results for {search_query}")

    elif "search" in command:
        if "Google" in command:
            search_query = command.split("Google")[-1].strip()
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}")
        elif "youtube" in command:
            search_query = command.split("youtube")[-1].strip()
            url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}")
        elif "wikipedia" in command:
            search_query = command.split("wikipedia")[-1].strip()
            url = f"https://en.wikipedia.org/wiki/{search_query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}")
        elif "gmail" in command:
            search_query = command.split("gmail")[-1].strip()
            url = f"https://mail.google.com/mail/u/0/#search/{search_query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}")

    elif "bye" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")

# Main function to continuously listen for commands
def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = recognize_command()
        if command:
            execute_command(command)

if __name__ == "__main__":
    main()

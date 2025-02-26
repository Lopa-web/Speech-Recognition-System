import speech_recognition as sr

def speech_to_text_from_microphone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for audio...")
        audio = recognizer.listen(source)

    try:
    
        print("Transcribing...")
        text = recognizer.recognize_google(audio)
        print("Text: ", text)

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        
speech_to_text_from_microphone()

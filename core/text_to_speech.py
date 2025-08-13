import pyttsx3

# Initialize the TTS engine once to avoid delay
engine = pyttsx3.init()

# Optional: Set voice properties (speed, volume, voice)
engine.setProperty('rate', 170)   # Speed (words per minute)
engine.setProperty('volume', 1.0) # Volume (0.0 to 1.0)

def speak(text):
    """Speak the given text aloud."""
    print(f"🗣️ Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

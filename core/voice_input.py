import speech_recognition as sr
import pyaudio

def get_preferred_microphone():
    recognizer = sr.Recognizer()
    mic_list = sr.Microphone.list_microphone_names()

    for idx, name in enumerate(mic_list):
        if any(keyword in name.lower() for keyword in ["headset", "usb", "bluetooth", "mic", "microphone"]):
            return sr.Microphone(device_index=idx)
    # fallback
    return sr.Microphone()

def listen_to_voice():
    recognizer = sr.Recognizer()
    mic = get_preferred_microphone()

    with mic as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "[Could not understand audio]"
    except sr.RequestError as e:
        return f"[Speech Recognition error: {e}]"

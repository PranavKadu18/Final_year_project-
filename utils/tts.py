import os
from elevenlabs.client import ElevenLabs
import sounddevice as sd
from scipy.io.wavfile import read
import io
import pyttsx3

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)


def speak(text):

    try:
        audio_stream = client.text_to_speech.convert(
            voice_id="EXAVITQu4vr4xnSDxMaL",
            output_format="wav_44100",
            text=text
        )

        audio_bytes = b"".join(chunk for chunk in audio_stream)

        wav_io = io.BytesIO(audio_bytes)

        samplerate, data = read(wav_io)

        sd.play(data, samplerate)
        sd.wait()

    except Exception:

        print("\n[TTS fallback activated]")

        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.say(text)
        engine.runAndWait()
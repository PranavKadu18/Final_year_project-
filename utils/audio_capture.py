import sounddevice as sd
import numpy as np


def capture_audio(duration=5, sample_rate=22050):

    print("\nRecording audio...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32",
    )

    sd.wait()

    audio = np.squeeze(audio)

    return audio, sample_rate
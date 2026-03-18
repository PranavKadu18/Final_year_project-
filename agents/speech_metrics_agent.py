import numpy as np
import librosa

from utils.audio_capture import capture_audio


def speech_metrics_agent(state):

    # -----------------------------
    # Capture audio
    # -----------------------------
    audio, sr = capture_audio()

    duration = len(audio) / sr

    # -----------------------------
    # Speech rate (approximation)
    # -----------------------------
    energy = np.sum(np.abs(audio))

    if duration > 0:
        speech_rate = int((energy / duration) % 160)
    else:
        speech_rate = 0


    # -----------------------------
    # Pitch estimation
    # -----------------------------
    pitches, magnitudes = librosa.piptrack(y=audio, sr=sr)

    pitch_values = pitches[magnitudes > np.median(magnitudes)]

    # Filter realistic speech frequencies
    pitch_values = pitch_values[(pitch_values > 80) & (pitch_values < 300)]

    if len(pitch_values) > 0:
        pitch_variation = float(np.std(pitch_values))
        avg_pitch = float(np.mean(pitch_values))
    else:
        pitch_variation = 0.0
        avg_pitch = 0.0


    # -----------------------------
    # Energy variation (voice tension)
    # -----------------------------
    rms = librosa.feature.rms(y=audio)[0]

    if len(rms) > 0:
        energy_variation = float(np.std(rms))
    else:
        energy_variation = 0.0


    # -----------------------------
    # Stress estimation (multi-feature)
    # -----------------------------

    pitch_score = min(pitch_variation / 120, 1)
    energy_score = min(energy_variation * 10, 1)
    rate_score = min(abs(speech_rate - 120) / 120, 1)

    # weighted combination
    voice_stress = (
        0.5 * pitch_score +
        0.3 * energy_score +
        0.2 * rate_score
    )


    # -----------------------------
    # Emotional tone classification
    # -----------------------------
    if voice_stress > 0.7:
        emotional_tone = "stressed"
    elif voice_stress > 0.35:
        emotional_tone = "neutral"
    else:
        emotional_tone = "calm"


    speech_metrics = {
        "speech_rate": speech_rate,
        "pitch_variation": pitch_variation,
        "average_pitch": avg_pitch,
        "energy_variation": energy_variation,
        "voice_stress": voice_stress,
        "emotional_tone": emotional_tone,
    }

    print("\nSpeech Metrics:", speech_metrics)

    state["speech_metrics"] = speech_metrics

    return state
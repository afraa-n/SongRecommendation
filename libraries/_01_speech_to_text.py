"""
Voice Transcription Script

This script provides functions for recording audio from a microphone, loading the audio data,
and transcribing the speech using a pre-trained Whisper ASR (Automatic Speech Recognition) model.
"""
import os
import speech_recognition as sr
import numpy as np

def recordingVoice(save_path="data/output.wav"):
    """
    Records audio from the microphone for a specified duration and saves it to a WAV file.

    Args:
    save_path (str): The path to save the recorded audio file.

    Returns:
    bytes: The recorded audio data as bytes.
    """
    # Create the "data" folder if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Parameters
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 10

    with sr.Microphone(sample_rate=RATE, chunk_size=CHUNK) as source:
        print("Recording...")

        # Adjust for ambient noise before recording
        recognizer.adjust_for_ambient_noise(source)

        # Record for 10 seconds
        audio_data = recognizer.record(source, duration=RECORD_SECONDS)

    print("Finished recording.")

    # Save the recorded audio to a WAV file
    with open(save_path, "wb") as wf:
        wf.write(audio_data.get_wav_data())

    return audio_data.get_wav_data()  # Return the audio data as bytes


def transcribe_audio(audio_data):
    """
    Transcribes audio data using a speech recognition service.

    Args:
    audio_data (bytes): The audio data to transcribe.

    Returns:
    str: The transcribed text.
    """
    recognizer = sr.Recognizer()

    # Load the audio using the new function
    audio = load_audio(audio_data)

    try:
        # Transcribe the audio using Google's speech recognition service
        result = recognizer.recognize_google(audio)
        return result
    except sr.UnknownValueError:
        return "Speech Recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Error with the speech recognition service; {e}"


def load_audio(audio_data):
    """
    Converts audio data from bytes to a NumPy array.

    Args:
    audio_data (bytes): The audio data in bytes.

    Returns:
    numpy.ndarray: The audio data as a NumPy array.
    """
    return np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32767.0

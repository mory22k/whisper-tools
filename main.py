"""Transcribe audio files using OpenAI's Whisper model.

This script loads the Whisper model, transcribes an audio file, and saves the transcription to a text file.
It requires the `whisper` library and an audio file in the `./audio` directory.
"""

import os
from pathlib import Path

import whisper

MODEL = os.getenv("MODEL", "turbo")
LANGUAGE = os.getenv("LANGUAGE", None)


def main() -> None:
    """Transcribe audio files."""
    print("Loading the Whisper model...")
    model = whisper.load_model(MODEL)
    print("Model loaded successfully.")

    audio_path = Path(__file__).parent / "audio"
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio directory not found: {audio_path}")

    audio_file = audio_path.glob("*.mp3")
    if not audio_file:
        raise FileNotFoundError(f"No audio files found in {audio_path}")

    audio_file = list(audio_file)[0]  # Get the first audio file
    if not audio_file.is_file():
        raise FileNotFoundError(f"Audio file not found: {audio_file}")

    print(f"Transcribing audio file: {audio_file}")
    result = model.transcribe(str(audio_file), verbose=True, language=LANGUAGE)

    transcription_file = audio_path / f"{audio_file.stem}_transcription.txt"
    with open(transcription_file, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print(f"Transcription saved to: {transcription_file}")


if __name__ == "__main__":
    main()

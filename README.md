# Whisper Tools

A supersimple tool for transcribing audio files using OpenAI's Whisper model.

## Installation

```bash
# Clone the repository
git clone https://github.com/mory22k/whisper-tools.git
cd whisper-tools

# Install dependencies
mise trust
mise install
```

## Usage

Specify language and model in the mise.toml file. For example:

```toml
[env]
language = "Japanese"
model = "turbo"
```

Remove all audio files from the audio directory.

Place your MP3 files in the audio directory. The tool will only process files with the ".mp3" extension.

Run the tool:

```bash
uv run main
```

The transcription will be saved as a text file in the same audio directory.

## Requirements

- Python 3.11
- Dependencies listed in pyproject.toml

## License

MIT

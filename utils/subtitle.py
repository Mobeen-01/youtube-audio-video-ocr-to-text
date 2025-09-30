import whisper
import subprocess, shlex
from pathlib import Path

MODEL = "small"

def _load_model():
    return whisper.load_model(MODEL)

def transcribe_youtube(youtube_url, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(exist_ok=True)

    audio_cmd = f'yt-dlp -f 18 -x --audio-format mp3 -o "{out_dir}/%(id)s.%(ext)s" "{youtube_url}"'
    subprocess.run(shlex.split(audio_cmd), check=True)

    files = list(out_dir.glob("*.mp3"))
    if not files:
        return "❌ Failed to download audio."
    audio_path = files[0]

    model = _load_model()
    result = model.transcribe(str(audio_path), task="translate", language=None)
    text = result.get("text", "")
    (out_dir / "transcription.txt").write_text(text, encoding="utf-8")
    return text


def transcribe_local(file_path, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(exist_ok=True)

    model = _load_model()
    result = model.transcribe(str(file_path), task="translate", language=None)
    text = result.get("text", "")
    (out_dir / "transcription.txt").write_text(text, encoding="utf-8")
    return text

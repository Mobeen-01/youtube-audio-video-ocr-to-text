# 🎥 Media-to-Text / Subtitle Generator (Flask App)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=flat&logo=python)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg?style=flat&logo=flask)](https://flask.palletsprojects.com/)
[![Whisper](https://img.shields.io/badge/OpenAI-Whisper-orange.svg?style=flat)](https://github.com/openai/whisper)
[![EasyOCR](https://img.shields.io/badge/OCR-EasyOCR-yellow.svg?style=flat)](https://github.com/JaidedAI/EasyOCR)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Overview

The **Media-to-Text / Subtitle Generator** is a **Flask-based web app** that converts:

- 🎥 **YouTube videos** → text / subtitles  
- 📂 **Local audio & video files** → text  
- 🖼 **Images (OCR)** → extracted text  

It combines **OpenAI Whisper** (speech-to-text) and **EasyOCR** (image-to-text) into a single, user-friendly application. Ideal for making subtitles, extracting notes, or digitizing scanned documents.

---



## 📸 Screenshot

Here’s a quick look at the **Media-to-Text / Subtitle Generator** in action:

![App Screenshot](https://github.com/Mobeen-01/youtube-audio-video-ocr-to-text/blob/main/Screenshot_OCR.jpg)

---

## 🚀 Features

✅ **YouTube Video Transcription** — paste a YouTube URL, download audio, and transcribe it to text.  
✅ **Audio/Video Upload** — upload `.mp3`, `.wav`, `.mp4`, etc., and extract speech.  
✅ **OCR for Images** — extract text from `.jpg`, `.png`, `.jpeg` using EasyOCR.  
✅ **Custom Save Path** — specify where to save generated text files.  
✅ **Real-Time Status Updates** — progress bar showing `Processing → Completed ✅ / Error ❌ / Cancelled ⛔`.  
✅ **Cancel Button** — stop individual tasks (YouTube / File / OCR) anytime.  
✅ **Download Option (planned)** — download processed text as `.txt` or `.srt`.  
✅ **Modern UI** — built with **Bootstrap 5 + FontAwesome**.  

---

## ⚙️ Tech Stack

- **Backend:** Flask (Python)  
- **Frontend:** HTML5, Bootstrap 5, FontAwesome  
- **Speech-to-Text:** [OpenAI Whisper](https://github.com/openai/whisper)  
- **OCR:** [EasyOCR](https://github.com/JaidedAI/EasyOCR)  
- **Video/Audio Handling:** yt-dlp, ffmpeg-python  

---

## 📂 Project Structure

```
flask_app/
│
├── app.py                # Main Flask application
├── requirements.txt      # Project dependencies
│
├── utils/
│   ├── subtitle.py       # Whisper transcription functions
│   ├── ocr.py            # EasyOCR functions
│
├── templates/
│   └── index.html        # Frontend (Bootstrap UI)
│
├── static/
│   └── style.css         # Custom styles
│
└── output/               # Folder for generated text/subtitle files
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/media-to-text-subtitle-generator.git
cd media-to-text-subtitle-generator/flask_app
```

### 2. Create virtual environment & install dependencies
```bash
# Create and activate virtual environment
py -3.12 -m venv venv
.env\Scriptsctivate   # On Windows
# source venv/bin/activate # On macOS/Linux

# Install requirements
pip install -r requirements.txt
```

> ⚠️ Make sure **ffmpeg** and **yt-dlp** are installed on your system and available in PATH.

### 3. Run the Flask app
```bash
python app.py
```

Then open in browser:  
👉 `http://127.0.0.1:5000`

---

## 🔄 Workflow

1. Choose input method (YouTube / File Upload / OCR).  
2. Click **Convert/Extract**.  
3. Progress bar updates status in real-time.  
4. Extracted text appears in **Output Box**.  
5. Optionally save text to the specified path in `output/`.  

---

## 📌 Use Cases

- 🎬 Generate subtitles for YouTube videos & lectures  
- 🎙 Convert podcasts, interviews, or sermons to text  
- 📖 OCR scanned notes & documents  
- 📝 Create editable notes from audio/video sources  

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  

---

## 🤝 Contributing

Contributions are welcome! Feel free to **fork** the repo, submit a PR, or open an issue.  

---

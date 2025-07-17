import yt_dlp
import ffmpeg
import wave
import json
from vosk import Model, KaldiRecognizer
import os
#import streamlit as st
from PIL import Image
import time
from PIL import Image, ImageDraw


SIGN_DICT = {
    "I": "signs/I.gif",
    "GO": "signs/GO.gif",
    "SCHOOL": "signs/SCHOOL.gif",
    # Add more signs as needed
}

def download_audio_from_youtube(url, out_file="audio.mp3"):
    print("📥 Downloading audio from YouTube...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'yt_audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("✅ Audio downloaded: audio.mp3")

def convert_mp3_to_wav(mp3_file, wav_file):
    print("🔄 Converting MP3 to WAV...")
    ffmpeg.input(mp3_file).output(wav_file, ac=1, ar='16000').run(overwrite_output=True)
    print("✅ Converted to WAV:", wav_file)

def transcribe_audio_vosk(wav_file, model_path="models/vosk-model-small-en-us-0.15"):
    print("🗣️ Transcribing audio with Vosk...")
    wf = wave.open(wav_file, "rb")
    model_path = os.path.abspath("models/vosk-model-small-en-us-0.15")
    model = Model(model_path)

    rec = KaldiRecognizer(model, wf.getframerate())

    text = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            text += res.get("text", "") + " "
    print("✅ Transcription complete:")
    print(text.strip())
    return text.strip()

def glossify_text(text):
    print("🔤 Glossifying text...")
    words = text.upper().split()
    gloss = [word for word in words if word in SIGN_DICT]
    print("🧠 Gloss:", gloss)
    return gloss

def get_sign_paths(gloss):
    print("🖐️ Mapping gloss to signs...")
    return [SIGN_DICT[word] for word in gloss]

def run_pipeline(youtube_url):
    download_audio_from_youtube(youtube_url, "audio.mp3")
    convert_mp3_to_wav("yt_audio.mp3", "audio.wav")
    text = transcribe_audio_vosk("audio.wav")
    gloss = glossify_text(text)
    sign_paths = get_sign_paths(gloss)
    print("🎬 Final Sign Paths:", sign_paths)
    return sign_paths


'''sign_paths = ['signs/I.gif'] * 8

#st.title("Sign Language Visualizer")

for path in sign_paths:
    img = Image.open(path)
    st.image(img, caption=path)
    time.sleep(1)'''

# Example use
if __name__ == "__main__":
    yt_url = input("🎯 Enter YouTube video URL: ")
    signs = run_pipeline(yt_url)
    print("✅ Pipeline completed. Signs ready for display.")


from src.preprocessing import load_audio
from src.beat_detection import get_onsets
from src.chart_generator import write_chart
from src.song_packager import generate_song_folder
from pydub import AudioSegment
import librosa
import os

def find_uploaded_song():
    audio_files = [
        f for f in os.listdir("audio")
        if f.endswith('.mp3') and f != "sample_song.mp3"
    ]
    if not audio_files:
        raise FileNotFoundError("No audio files found in the 'audio' directory.")

    return os.path.join("audio", audio_files[0])

def convert_to_ogg(input_song_mp3, output_path=None):
    if output_path is None:
        output_path = os.path.splitext(input_song_mp3)[0] + ".ogg"

    audio = AudioSegment.from_mp3(input_song_mp3)
    audio.export(output_path, format="ogg")
    print(f"Converted {input_song_mp3} to {output_path}")
    return output_path

input_song_mp3 = find_uploaded_song()
input_song = convert_to_ogg(input_song_mp3)
print(f"Processing song: {input_song}")

# Load audio and detect onsets
y, sr = load_audio(input_song)
onsets = get_onsets(y, sr)

# Estimate BPM using librosa
bpm = librosa.beat.tempo(y=y, sr=sr)[0]
print(f"Estimated BPM: {bpm}")

# Generate chart with bpm
chart_output = "charts/output_chart.chart"
write_chart(onsets, chart_output, song_name="Generated Song", audio_path=input_song, bpm=bpm)

# Package the song into a folder
generate_song_folder(chart_output, input_song)
print(f"Chart generated and saved to {chart_output}")
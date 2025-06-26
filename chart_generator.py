import os
import random
import librosa
import numpy as np
import joblib

# Load trained classifier model once
clf = joblib.load("rf_fret_classifier.pkl")

# Updated chart writer using ML predictions
def write_chart(onsets, output_path, song_name="Generated Song", audio_path="audio/song.ogg", bpm=120):
    # Load audio for ML feature extraction
    y, sr = librosa.load(audio_path, sr=22050)

    with open(output_path, 'w') as f:
        # [Song] metadata block
        f.write("[Song]\n{")
        f.write(f"\n  Name = \"{song_name}\"")
        f.write("\n  Artist = \"AI Generator\"")
        f.write("\n  Charter = \"ML Project\"")
        f.write("\n  Offset = 0")
        f.write("\n  Resolution = 192")
        f.write("\n  Player2 = bass")
        f.write("\n  Difficulty = 0")
        f.write("\n  PreviewStart = 0")
        f.write("\n  PreviewEnd = 0")
        f.write("\n  Genre = \"Test\"")
        f.write("\n  MediaType = \"cd\"")
        f.write("\n  MusicStream = \"song.ogg\"")
        f.write("\n}\n\n")

        # [SyncTrack] block
        f.write("[SyncTrack]\n{")
        f.write("\n  0 = TS 4")
        f.write("\n  0 = B 120000")  # Defalt 120 BPM for metadata
        f.write("\n}\n\n")

        # [ExpertSingle] block
        f.write("[ExpertSingle]\n{")
        for t in onsets:
            if t > librosa.get_duration(y=y, sr=sr):
                continue
            
            tick = int(t * (192 * bpm / 60))  # Convert seconds to ticks
            start = max(t - 0.25, 0)
            end = t + 0.25
            y_segment = y[int(start * sr):int(end * sr)]

            if len(y_segment) == 0:
                continue

            mel = librosa.feature.melspectrogram(y=y_segment, sr=sr, n_mels=64)
            mel_db = librosa.power_to_db(mel, ref=np.max)
            mel_flat = np.mean(mel_db, axis=1)

            try:
                fret = int(clf.predict([mel_flat])[0])
                if fret not in [0, 1, 2, 3, 4]:
                    continue
                # Dynamic duration based on BPM: 0.5 second hold
                duration_seconds = 0.5
                duration = int(duration_seconds * (bpm / 60) * 192 )  
                f.write(f"\n  {tick} = N {fret} {duration}")
            except Exception as e:
                print(f"Error predicting fret at t={t:.2f}s: {e}")
                continue

        f.write("\n}\n")

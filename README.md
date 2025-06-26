# Automated Chart Generator for Clone Hero

This project provides a Python-based pipeline to automatically generate playable Clone Hero chart packages from raw audio tracks. By leveraging audio processing libraries (Librosa, Pydub) for onset detection and a trained Random Forest model for fret prediction, it produces valid `.chart` files and packages them alongside converted audio and metadata into song folders compatible with Clone Hero.

---

## Project Structure

```text
clonehero_chart_generator/
├── audio/                    # Raw input audio files (.mp3, .wav)
├── charts/                   # Generated .chart files
├── data/                     # Intermediate data (onsets, segments)
├── songs/                    # Packaged Clone Hero song folders
├── src/                      # Source code modules
│   ├── beat_detection.py     # Beat and Onset detection logic
│   ├── chart_generator.py    # .chart note file generator
│   ├── preprocessing.py      # Audio loading and conversion
│   └── song_packager.py      # Song folder packaging
├── main.py                   # Entry point script
├── rf_fret_classifier.pkl    # Trained Random Forest fret classifier (too large to upload)
├── requirements.txt          # Python dependencies
└── README.md                 # This documentation
``` 

---

## Overview

The pipeline consists of five main stages:

1. **Audio Input**  
   - User places an audio track in `audio/`.  
   - Optionally, the track is converted to OGG format via Pydub.

2. **Preprocessing**  
   - Librosa loads and normalizes the waveform.  
   - Onset detection extracts key pulsation times.

3. **Chart Generation**  
   - Onset times are converted to tick indices using estimated BPM and resolution.  
   - A Random Forest model predicts fret positions for each onset.  
   - A valid `.chart` file is assembled with `[Song]`, `[SyncTrack]`, and `[ExpertSingle]` sections.

4. **Packaging**  
   - Audio renamed to `song.ogg`, chart to `notes.chart`, plus a `song.ini` metadata file.  
   - All files copied into a new folder under `songs/`, ready for Clone Hero.

5. **Machine Learning Enhancements**  
   - Optional separation of stems (guitar, bass) using Demucs.  
   - Future integration of supervised models to refine difficulty levels and note durations.

---

## Installation

1. Clone the repository and navigate in:
   ```bash
   git clone https://github.com/yourusername/clonehero_chart_generator.git
   cd clonehero_chart_generator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the main script to process all audio files in `audio/`:
```bash
python main.py --input_dir audio/ --output_dir songs/
```

To process a single file:
```bash
python main.py --input audio/song.mp3 --output songs/MyChart
```

---

## Results

- Generates a playable Clone Hero song folder containing:
  - `song.ogg` (converted audio)
  - `notes.chart` (game chart)
  - `song.ini` (metadata)
- The generated charts align onsets to detected beats; machine-learning-based fret assignments improve playability.

---

## Future Work

- Add dynamic BPM detection and tempo tracking.  
- Integrate supervised learning to predict durations and difficulty tiers.  
- Support multiple instruments by leveraging separated stems.  
- Build a GUI for easier user interaction.

---

## References

- **Clone Hero**: https://clonehero.net/  
- **Librosa**: https://librosa.org/  
- **Pydub / FFmpeg**: https://github.com/jiaaro/pydub, https://ffmpeg.org/  
- **Demucs**: https://github.com/facebookresearch/demucs  
- **Random Forest**: scikit-learn implementation for fret prediction

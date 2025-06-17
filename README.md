# Clone Hero Chart Generator using Machine Learning

This project generates playable `.chart` files for [Clone Hero](https://clonehero.net/) directly from audio using a machine learning pipeline. It leverages beat detection, instrument separation (Demucs), and fret classification using CNNs and transfer learning with PANNs.

---

## Overview

The goal is to automate the creation of rhythm game charts that align closely with a song’s musical structure, reducing manual charting effort while maintaining musical accuracy and playability.

---

## Project Structure

    clone-hero-chart-ml/
    ├── data/           # Processed dataset samples or features
    ├── notebooks/      # Training, testing, and EDA notebooks
    ├── src/            # Scripts: chart generation, feature extraction, prediction
    ├── models/         # Trained classifiers (.pt or .pkl)
    ├── assets/         # Spectrograms, video demos, chart screenshots
    ├── requirements.txt
    ├── README.md
    └── .gitignore

---

## Pipeline Steps

1. **Input**: Raw audio file (`.ogg`, `.wav`, or `.mp3`)
2. **Demucs**: Separate stems (e.g., guitar, bass, drums)
3. **Beat Detection**: Extract onsets using `librosa`
4. **Feature Extraction**: Use mel spectrograms or CNN14 embeddings
5. **ML Prediction**: Classify fret positions from audio segments
6. **Chart Writing**: Generate `.chart` file for Clone Hero

---

## How to Use

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the chart generator
python main.py --audio "song.ogg" --output "output.chart"


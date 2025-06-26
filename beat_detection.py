import librosa

def get_onsets(y, sr):
    """
    Detect onsets in an audio signal using the onset strength envelope.
    
    Parameters:
    - y (ndarray): Audio time series.
    - sr (int): Sample rate of the audio file.
    
    Returns:
    - onset_frames (ndarray): Indices of detected onsets in frames.
    """

    # Detect onsets
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
    
    # Convert frames to time
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)
   
    return onset_times
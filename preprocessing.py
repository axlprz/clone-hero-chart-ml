import librosa

def load_audio(file_path):
    """
    Load an audio file and return the audio time series and sample rate.
    
    Parameters:
    - file_path (str): Path to the audio file.
    
    Returns:
    - y (ndarray): Audio time series.
    - sr (int): Sample rate of the audio file.
    """
    y, sr = librosa.load(file_path, sr=22050, mono=True)
    # Convert to mono if stereo
    return y, sr
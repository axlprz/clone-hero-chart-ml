import os
import shutil
                
def generate_song_folder(chart_path, audio_path, output_dir="songs"):
    # Extract base name without extension
    song_name = os.path.splitext(os.path.basename(audio_path))[0]

    # Create the song-specific folder
    song_folder = os.path.join(output_dir, song_name)
    os.makedirs(song_folder, exist_ok=True)

    # Generate song.ini
    ini_path = os.path.join(song_folder, "song.ini")
    with open(ini_path, 'w') as f:
        f.write("[song]\n")
        f.write(f"name = {song_name}\n")
        f.write("artist = AI Generator\n")
        f.write("charter = ML Project\n")
        f.write("audio = song.ogg\n")
        f.write("offset = 0\n")
        f.write("preview_start_time = 0\n")
        f.write("preview_end_time = 30\n")
        f.write("genre = ML\n")
        f.write("year = 2025\n")
        f.write("diff_band = 0\n")
        f.write("diff_guitar = 1\n")
        f.write("diff_drums = 0\n")
        f.write("diff_keys = 0\n")
        f.write("diff_vocals = 0\n")
        f.write("icon = \n")

    # Copy chart and audio to song folder
    shutil.copy2(chart_path, os.path.join(song_folder, "notes.chart"))
    shutil.copy2(audio_path, os.path.join(song_folder, os.path.basename(audio_path)))

    print(f"Generated song folder at: {song_folder}")
    return song_folder
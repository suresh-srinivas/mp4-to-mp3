import os
from moviepy.editor import *

def convert_mp4_to_mp3(directory):
    # Check if the provided directory exists
    if not os.path.isdir(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    files = os.listdir(directory)
    if not files:
        print(f"No files found in the directory '{directory}'.")
        return

    for file in files:
        if file.endswith(".mp4"):
            mp4_path = os.path.join(directory, file)
            mp3_path = os.path.join(directory, os.path.splitext(file)[0] + '.mp3')
            
            print(f"Processing file: {mp4_path}")
            try:
                video_clip = VideoFileClip(mp4_path)
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(mp3_path)
                audio_clip.close()
                video_clip.close()
                print(f"Successfully converted '{file}' to MP3.")
            except Exception as e:
                print(f"Error converting file '{file}': {e}")
        else:
            print(f"Skipping non-MP4 file: {file}")

# Replace 'path_to_your_directory' with the path to the directory containing your MP4 files
directory_path = '/Users/ssuresh/edg/mp4-to-mp3/test-dir/'
convert_mp4_to_mp3(directory_path)



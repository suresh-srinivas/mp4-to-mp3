
# MP4 to MP3 Converter

This Python script converts MP4 video files to MP3 audio files using the `moviepy` library.

## Prerequisites

Before running this script, you need to have Python installed on your computer. Additionally, you need the `moviepy` library, which can be installed using pip:

```bash
pip install moviepy
```

## Usage

1. Place the script in a directory that contains the MP4 files you want to convert or specify the path to the directory containing your MP4 files in the script.
2. Open the script with a text editor and replace `'path_to_your_directory'` with the actual path to the directory containing your MP4 files.
3. Run the script using a Python interpreter:

```bash
python mp4_to_mp3_converter.py
```

The script will automatically find all MP4 files in the specified directory, convert them to MP3 format, and save them in the same directory with the same name.

## Features

- Batch conversion: Converts all MP4 files found in the specified directory.
- Error handling: Provides clear messages if any errors occur during the conversion process.
- Debug information: Outputs detailed information about the conversion process, helping diagnose any potential issues.

## Note

This script is intended for offline use and does not require an internet connection. Make sure you have the necessary permissions to read from and write to the directory containing your MP4 files.

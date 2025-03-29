import subprocess
import os
import glob

def download_full_audio(youtube_url, output_path_template, audio_quality='44k', cookies_file=None):
    """
    Download the full YouTube video as an audio file (mp3) without clipping.
    """
    command = [
        'yt-dlp',
        '--extract-audio',
        '--audio-format', 'mp3',
        '--audio-quality', audio_quality,
        '-o', output_path_template,
        '--force-overwrites'
    ]
    
    # Add cookies file if specified
    if cookies_file:
        command.extend(['--cookies', cookies_file])
    
    # Add User-Agent for better compatibility
    command.extend([
        '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/58.0.3029.110 Safari/537.36'
    ])
    
    command.append(youtube_url)
    
    print("Downloading full audio file...")
    subprocess.run(command, check=True)
    print("Download complete.")

def find_downloaded_file(download_dir):
    """
    Locate the downloaded mp3 file in the specified directory.
    Assumes that the directory contains the downloaded file.
    """
    files = glob.glob(os.path.join(download_dir, "*.mp3"))
    if not files:
        raise FileNotFoundError("No mp3 file found in the download directory.")
    # Get the most recent file (assuming it's the one we just downloaded)
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

def generate_trimmed_filename(original_file):
    """
    Generate a new filename for the trimmed file based on the original filename.
    For example, if original_file is "Title.mp3", return "Title_trimmed.mp3".
    """
    base, ext = os.path.splitext(original_file)
    return f"{base}_trimmed{ext}"

def trim_audio(input_file, output_file, start_time, end_time):
    """
    Use ffmpeg to trim the audio file from start_time to end_time.
    """
    command = [
        'ffmpeg', '-y',        # Overwrite output file if it exists
        '-i', input_file,
        '-ss', start_time,     # Start time for the trim
        '-to', end_time,       # End time for the trim
        '-c', 'copy',          # Copy streams without re-encoding
        output_file
    ]
    print(f"Trimming audio from {start_time} to {end_time}...")
    subprocess.run(command, check=True)
    print(f"Trimmed file saved as {output_file}")

# --- Main script execution ---

# Define variables
youtube_url = 'https://www.youtube.com/watch?'
download_dir = '/workspaces/youtube-downloader'
# Use yt-dlp placeholder for title; the downloaded file will be named using the YouTube title.
output_path_template = os.path.join(download_dir, '%(title)s.%(ext)s')
cookies_file = os.path.join(download_dir, 'cookies.txt')  # if needed

# Parameters for audio quality and trimming (in hh:mm:ss)
audio_quality = '44k'
start_time = '00:00:00'
end_time = '00:29:22'

# Step 1: Download the full audio file with specified quality
download_full_audio(youtube_url, output_path_template, audio_quality=audio_quality, cookies_file=cookies_file)

# Step 2: Locate the downloaded file
downloaded_file = find_downloaded_file(download_dir)
print(f"Downloaded file: {downloaded_file}")

# Step 3: Generate output filename based on downloaded file title
trimmed_output_file = generate_trimmed_filename(downloaded_file)
print(f"Trimmed output file will be: {trimmed_output_file}")

# Step 4: Trim the audio using ffmpeg
trim_audio(downloaded_file, trimmed_output_file, start_time, end_time)

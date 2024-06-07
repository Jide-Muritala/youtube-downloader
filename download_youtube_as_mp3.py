import subprocess

def download_youtube_as_mp3(youtube_url, output_path, audio_quality='48k', start_time=None, end_time=None):
    """
    Download a YouTube video as an MP3 file with specified audio quality and time segment.

    Args:
    youtube_url (str): URL of the YouTube video.
    output_path (str): Path to save the downloaded MP3 file.
    audio_quality (str): Audio quality for the MP3 file (e.g., '48k', '128k').
    start_time (str): Start time for clipping (e.g., '00:00:10' for 10 seconds).
    end_time (str): End time for clipping (e.g., '00:00:20' for 20 seconds).
    """
    # Construct the yt-dlp command
    command = [
        'yt-dlp',
        '-x', '--audio-format', 'mp3',
        '--audio-quality', audio_quality,
        '-o', output_path
    ]
    
    # Add start time and end time if specified
    if start_time:
        command.extend(['--postprocessor-args', f"-ss {start_time}"])
    if end_time:
        command.extend(['--postprocessor-args', f"-to {end_time}"])

    command.append(youtube_url)

    # Run the yt-dlp command
    try:
        subprocess.run(command, check=True)
        print(f"File downloaded and saved as {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

# Define the YouTube URL and output file path
youtube_url = 'https://www.youtube.com/watch?'
output_path = '/workspaces/youtube-downloader/%(title)s.%(ext)s'

# Define start and end times for clipping
# start_time = '00:00:10'  # Start at 10 seconds
# end_time = '00:00:30'    # End at 30 seconds

# Download the YouTube video as an MP3 file with specified audio quality and time segment
# download_youtube_as_mp3(youtube_url, output_path, audio_quality='48k', start_time=start_time, end_time=end_time)

# Download the entire YouTube video as an MP3 file with specified audio quality
download_youtube_as_mp3(youtube_url, output_path, audio_quality='48k')

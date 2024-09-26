import subprocess

def download_youtube_as_mp3(youtube_url, output_path_template, audio_quality='44k', cookies_file=None, start_time=None, end_time=None):
    """
    Download a YouTube video as an MP3 file with specified audio quality and time segment.

    Args:
    youtube_url (str): URL of the YouTube video.
    output_path_template (str): Template path to save the downloaded MP3 file, using yt-dlp placeholders.
    audio_quality (str): Audio quality for the MP3 file (e.g., '44k', '128k').
    cookies_file (str): Path to the cookies file for authentication.
    start_time (str): Start time for clipping (e.g., '00:03:25' for 3 minutes and 25 seconds).
    end_time (str): End time for clipping (e.g., '00:35:40' for 35 minutes and 40 seconds).
    """
    # Construct the yt-dlp command
    command = [
        'yt-dlp',
        '--extract-audio', '--audio-format', 'mp3',
        '--audio-quality', audio_quality,
        '-o', output_path_template
    ]
    
    # Add cookies file if specified
    if cookies_file:
        command.extend(['--cookies', cookies_file])
    
    # Add start time and end time if specified
    if start_time or end_time:
        if start_time:
            command.extend(['--download-sections', f"*{start_time}-"])
        if end_time:
            command[-1] += f"{end_time}"

    command.append(youtube_url)

    # Run the yt-dlp command
    try:
        subprocess.run(command, check=True)
        print(f"File downloaded and saved as {output_path_template}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

# Define the YouTube URL and output file path
youtube_url = 'https://www.youtube.com/watch?'
output_path_template = '/workspaces/youtube-downloader/%(title)s.%(ext)s'

# Define the path to your cookies file
cookies_file = '/workspaces/youtube-downloader/youtube_cookies.txt'

# Define start and end times for clipping
start_time = '00:03:25'  # Start at 3 minutes and 25 seconds
end_time = '00:35:40'    # End at 35 minutes and 40 seconds

# Download the YouTube video as an MP3 file with specified audio quality and time segment
download_youtube_as_mp3(youtube_url, output_path_template, audio_quality='44k', cookies_file=cookies_file, start_time=start_time, end_time=end_time)

# Download the entire YouTube video as an MP3 file with specified audio quality
# download_youtube_as_mp3(youtube_url, output_path_template, audio_quality='44k', cookies_file=cookies_file)

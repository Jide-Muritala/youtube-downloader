import subprocess

def download_youtube_as_mp3(
    youtube_url,
    output_path_template,
    audio_quality="0",
    cookies_file=None,
    start_time=None,
    end_time=None
):
    """
    Download a YouTube video as an MP3 file with specified audio quality and time segment.

    Args:
    youtube_url (str): URL of the YouTube video.
    output_path_template (str): Template path to save the downloaded MP3 file, using yt-dlp placeholders.
    audio_quality (str): Audio quality for the MP3 file (e.g., '0' [Best], '5' [Medium], '9' [Lowest]).
    cookies_file (str): Path to the cookies file for authentication.
    start_time (str): Start time for clipping (e.g., '00:03:25' for 3 minutes and 25 seconds).
    end_time (str): End time for clipping (e.g., '00:35:40' for 35 minutes and 40 seconds).
    """
    command = [
        "yt-dlp",
        "-f", "251", 
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", audio_quality,
        "--js-runtimes", "node",
        "--remote-components", "ejs:github",
        "-o", output_path_template,
        "--force-overwrites",
    ]

    if cookies_file:
        command += ["--cookies", cookies_file]

    if start_time or end_time:
        ffmpeg_args = []
        if start_time:
            ffmpeg_args.append(f"-ss {start_time}")
        if end_time:
            ffmpeg_args.append(f"-to {end_time}")
        command += ["--postprocessor-args", " ".join(ffmpeg_args)]

    command.append(youtube_url)

    subprocess.run(command, check=True)


# Usage
download_youtube_as_mp3(
    youtube_url="https://www.youtube.com/watch?",
    output_path_template="/workspaces/youtube-downloader/%(title)s.%(ext)s",
    audio_quality="9",
    cookies_file="cookies.txt"
)

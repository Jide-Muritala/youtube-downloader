import subprocess
import os

def download_audio_section(
    youtube_url,
    output_path_template,
    audio_quality="0",
    cookies_file=None,
    start_time=None,
    end_time=None
):
    """
    Download a specific section of a YouTube video as an MP3 file.
    """

    command = [
        "yt-dlp",
        "-f", "91",                 
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", audio_quality,
        "--force-overwrites",
        "--js-runtimes", "node",
        "--remote-components", "ejs:github",
        "-o", output_path_template
    ]

    if cookies_file:
        command.extend(["--cookies", cookies_file])

    # Trim during post-processing using ffmpeg
    if start_time or end_time:
        ffmpeg_args = []
        if start_time:
            ffmpeg_args.append(f"-ss {start_time}")
        if end_time:
            ffmpeg_args.append(f"-to {end_time}")

        command.extend([
            "--postprocessor-args",
            " ".join(ffmpeg_args)
        ])

    command.append(youtube_url)

    print("Downloading trimmed audio section...")
    subprocess.run(command, check=True)
    print("Download complete.")

youtube_url = "https://www.youtube.com/watch?"
download_dir = "/workspaces/youtube-downloader"

output_path_template = os.path.join(
    download_dir,
    "%(title)s_%(section_start)s-%(section_end)s.%(ext)s"
)

cookies_file = os.path.join(download_dir, "cookies.txt")

download_audio_section(
    youtube_url=youtube_url,
    output_path_template=output_path_template,
    audio_quality="9",
    cookies_file=cookies_file,
    start_time="00:00:00",
    end_time="00:29:22"
)

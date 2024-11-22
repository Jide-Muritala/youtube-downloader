# Youtube downloader

Ensure you have yt-dlp and FFmpeg installed (you can verify that both tools are installed correctly by running `yt-dlp --version` and `ffmpeg -version` in the terminal):
- `sudo apt update`
- `sudo apt install -y python3-pip ffmpeg`
- `pip3 install yt-dlp`


Specify Youtube URL and output file:
- youtube_url: Replace 'https://www.youtube.com/watch?v=YOUR_VIDEO_ID' with the actual URL of the YouTube video you want to download.
- output_path: Specify the path where you want to save the MP3 file. /workspaces/youtube-downloader/output.mp3 saves the file in the root directory of your Codespace.


Run the script:
- `python download_youtube_as_mp3.py`



Audio Quality: The audio quality is set to 48 kbps by default. You can change this by modifying the audio_quality parameter when calling the function.


Uncomment appropriate part of script to specify start and end time

Combine MP3
- Ensure you have ffmpeg and pydub installed
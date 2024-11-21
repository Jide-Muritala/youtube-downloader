from pydub import AudioSegment

def combine_mp3_files(mp3_files, output_file="combined.mp3", target_size_mb=10):
    try:
        # Initialize an empty AudioSegment
        combined = AudioSegment.empty()

        for mp3_file in mp3_files:
            print(f"Processing: {mp3_file}")
            audio = AudioSegment.from_file(mp3_file)

            # Ensure all files have the same properties
            audio = audio.set_frame_rate(44100).set_channels(2)
            combined += audio

        # Calculate the target bitrate to fit the desired file size
        duration_seconds = combined.duration_seconds
        target_bitrate = (target_size_mb * 8 * 1024 * 1024) / duration_seconds  # Bits per second
        
        # Cap bitrate to MP3 standards (320 kbps max for high-quality MP3)
        target_bitrate = min(target_bitrate, 320000)  # 320 kbps = 320,000 bps

        print(f"Target bitrate: {target_bitrate / 1000:.1f} kbps")

        # Export with specified bitrate
        combined.export(output_file, format="mp3", bitrate=f"{int(target_bitrate / 1000)}k")
        print(f"Combined MP3 saved as: {output_file}")
    
    except Exception as e:
        print(f"Error: {e}")

# Example usage
mp3_files = ["file1.mp3", "file2.mp3"]  # Replace with your MP3 file paths
combine_mp3_files(mp3_files, output_file="combined.mp3", target_size_mb=10)

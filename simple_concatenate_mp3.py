from pydub import AudioSegment

def combine_mp3_files(mp3_files, output_file="combined.mp3"):
    try:
        # Load the first file
        combined = AudioSegment.from_file(mp3_files[0])

        # Append the rest of the files
        for mp3_file in mp3_files[1:]:
            audio = AudioSegment.from_file(mp3_file)
            combined += audio

        # Export the combined file using the default settings (no re-encoding)
        combined.export(output_file, format="mp3")
        print(f"Combined MP3 saved as: {output_file}")
    
    except Exception as e:
        print(f"Error: {e}")

# Example usage
mp3_files = ["file1.mp3", "file2.mp3"]  # Replace with your file paths
combine_mp3_files(mp3_files, output_file="combined.mp3")

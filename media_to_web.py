from pathlib import Path
from PIL import Image
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import sys
import shutil

# Configuration
if len(sys.argv) < 2:
    print("Usage: python3 media_to_web.py <folder_path>")
    sys.exit(1)

folder_path = Path(sys.argv[1]).expanduser().resolve()

# Supported Extensions
image_exts = [".png", ".jpg", ".jpeg"]
video_exts = [".mp4", ".mov", ".avi", ".mkv"]
audio_exts = [".mp3", ".wav"]

# Target converted extensions
converted_image_ext = ".webp"
converted_video_ext = ".webm"
converted_audio_ext = ".ogg"


# Functions
def backup_file(file_path, backup_folder):
    try:
        backup_folder.mkdir(exist_ok=True)
        shutil.copy2(str(file_path), str(backup_folder / file_path.name))
        print(f"[BACKUP] {file_path.name} → {backup_folder.name}/{file_path.name}")
    except Exception as e:
        print(f"[BACKUP-ERROR] {file_path.name}: {e}")


def convert_image(file_path):
    target_file = file_path.with_suffix(converted_image_ext)
    try:
        with Image.open(file_path) as img:
            img.save(target_file, "WEBP")
        print(f"[IMG] {file_path.name} → {target_file.name}")
        file_path.unlink()  # Remove original
    except Exception as e:
        print(f"[IMG-ERROR] {file_path.name}: {e}")


def convert_video(file_path):
    target_file = file_path.with_suffix(converted_video_ext)
    try:
        clip = VideoFileClip(str(file_path))
        clip.write_videofile(
            str(target_file),
            codec="libvpx",
            audio_codec="libvorbis",
            verbose=False,
            logger=None,
        )
        clip.close()
        print(f"[VID] {file_path.name} → {target_file.name}")
        file_path.unlink()  # Remove original
    except Exception as e:
        print(f"[VID-ERROR] {file_path.name}: {e}")


def convert_audio(file_path):
    target_file = file_path.with_suffix(converted_audio_ext)
    try:
        audio = AudioFileClip(str(file_path))
        audio.write_audiofile(str(target_file))
        audio.close()
        print(f"[AUD] {file_path.name} → {target_file.name}")
        file_path.unlink()  # Remove original
    except Exception as e:
        print(f"[AUD-ERROR] {file_path.name}: {e}")


def process_folder(current_folder):
    backup_folder = current_folder / "old_media"
    for file_path in current_folder.iterdir():
        if file_path.is_file():
            ext = file_path.suffix.lower()
            # Skip files already converted
            if ext in [converted_image_ext, converted_video_ext, converted_audio_ext]:
                continue

            if ext in image_exts:
                # Backup original before conversion
                backup_file(file_path, backup_folder)
                convert_image(file_path)
            elif ext in video_exts:
                backup_file(file_path, backup_folder)
                convert_video(file_path)
            elif ext in audio_exts:
                backup_file(file_path, backup_folder)
                convert_audio(file_path)
            else:
                # Ignore other files
                continue

        elif file_path.is_dir() and file_path.name != "old_media":
            # Recursively process subfolders
            process_folder(file_path)


# Main process
process_folder(folder_path)
print("✅ Conversion completed. Originals are saved in 'old_media' folders.")

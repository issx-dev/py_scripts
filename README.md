# Python Automation Scripts

A collection of Python utilities designed to automate common daily tasks such as file organization and media conversion for web optimization.

## 🚀 Features

### File Organizer (`file_organizer.py`)
- Automatically organizes files in a directory by their extensions
- Creates organized folder structure within an "OrganizedFiles" subdirectory
- Groups files by file type (e.g., all `.pdf` files go into a `pdf` folder)
- Perfect for cleaning up cluttered download folders or project directories

### Media to Web Converter (`media_to_web.py`)
- Batch converts media files to web-optimized formats
- **Images**: Converts PNG, JPG, JPEG → WebP format
- **Videos**: Converts MP4, MOV, AVI, MKV → WebM format
- **Audio**: Converts MP3, WAV → OGG format
- Creates automatic backups of original files in `old_media` folders
- Recursively processes subdirectories
- Significantly reduces file sizes while maintaining quality

## 📋 Requirements

- Python 3.6+
- Dependencies listed in `requirements.txt`

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd py_scripts
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

### File Organizer

Organize files in a specific folder:
```bash
python file_organizer.py <folder_path>
```

**Example:**
```bash
python file_organizer.py Downloads
```

This will create an "OrganizedFiles" folder inside your Downloads directory and sort all files into subfolders based on their extensions.

### Media to Web Converter

Convert media files to web-optimized formats:
```bash
python3 media_to_web.py <folder_path>
```

**Example:**
```bash
python3 media_to_web.py ~/Pictures/vacation-photos
```

This will:
- Convert all images to WebP format
- Convert all videos to WebM format  
- Convert all audio files to OGG format
- Create backups of original files in `old_media` folders
- Process all subdirectories recursively

## 🔧 Supported File Types

### File Organizer
- Works with any file extension
- Creates folders based on file extensions automatically

### Media to Web Converter

| Media Type | Input Formats | Output Format |
|------------|---------------|---------------|
| Images     | PNG, JPG, JPEG | WebP         |
| Videos     | MP4, MOV, AVI, MKV | WebM     |
| Audio      | MP3, WAV      | OGG          |

## ⚠️ Important Notes

- **Backup Safety**: The media converter automatically creates backups before conversion
- **File Removal**: Original files are removed after successful conversion (backups remain)
- **Error Handling**: Failed conversions are logged and original files are preserved
- **Web Optimization**: Converted formats are optimized for web use with smaller file sizes

## 📁 Example Directory Structure

### After running File Organizer:
```
Downloads/
├── OrganizedFiles/
│   ├── pdf/
│   │   ├── document1.pdf
│   │   └── document2.pdf
│   ├── jpg/
│   │   ├── photo1.jpg
│   │   └── photo2.jpg
│   └── txt/
│       └── notes.txt
└── (other unorganized files remain here)
```

### After running Media to Web Converter:
```
Photos/
├── old_media/          # Backup folder
│   ├── IMG_001.jpg
│   └── video.mp4
├── IMG_001.webp        # Converted image
└── video.webm          # Converted video
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Issa El Mokadem

---

*These scripts are designed to make file management and web optimization tasks more efficient and automated.*

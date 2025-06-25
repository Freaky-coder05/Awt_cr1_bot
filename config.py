# config.py
import os

# Telegram bot token (from BotFather)
TELEGRAM_API_ID=21740783
TELEGRAM_API_HASH="a5dc7fec8302615f5b441ec5e238cd46"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "7722665729:AAEYCyXSnFbRpswAOb7FEBjGx2X-3qKEdGg")
# Crunchyroll login credentials (from environment variables or hardcoded if needed)
CRUNCHYROLL_USERNAME = os.getenv("CRUNCHYROLL_USERNAME", "joevaas94@gmail.com")  # Replace with your username
CRUNCHYROLL_PASSWORD = os.getenv("CRUNCHYROLL_PASSWORD", "joevaas123")  # Replace with your password

# Optional: User-Agent for Crunchyroll API
CRUNCHYROLL_USER_AGENT = os.getenv("CRUNCHYROLL_USER_AGENT", "CrunchyrollBot/1.0")

# Paths to DRM decryption tools (set path to mp4decrypt, ffmpeg, and mkvmerge as needed)
MP4DECRYPT_PATH = "mp4decrypt"
FFMPEG_PATH = "ffmpeg"  # Adjust this path
MKVMERGE_PATH = os.getenv("MKVMERGE_PATH", "/usr/bin/mkvmerge")  # Adjust this path

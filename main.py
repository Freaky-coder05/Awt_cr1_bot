import logging
from pyrogram import Client, filters
from pyrogram.types import Message

from bot.downloader import download_series
from bot.utils import to_small_caps, validate_crunchyroll_url
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_TOKEN

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize Pyrogram Client
app = Client(
    "crunchyroll_bot",
    bot_token=TELEGRAM_TOKEN,
    api_id=TELEGRAM_API_ID,
    api_hash=TELEGRAM_API_HASH
)

# /start command
@app.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    welcome_message = (
        "Radhe Radhe, this is billa space @Billaspace & you are plugged into Billa crunchyroll bot, "
        "an advanced bot that downloads series and episodes from crunchyroll URL with >quality "
        "e.g., 240p, 360p, 720p, 1080p, hdrip> . Just paste a streaming link of content and desired quality. "
        "Billa will download it for you."
    )
    await message.reply_text(to_small_caps(welcome_message))

# Download command or direct message
@app.on_message(filters.text & filters.private)
async def download(client: Client, message: Message):
    try:
        parts = message.text.strip().split(' ')

        if len(parts) < 2:
            await message.reply_text(to_small_caps(
                "Please provide both the URL and desired quality "
                "(e.g., 'https://crunchyroll.com/series/xyz 720p')."))
            return

        url, selected_quality = parts[0], parts[1]

        if not validate_crunchyroll_url(url):
            await message.reply_text(to_small_caps("Invalid URL! Please provide a valid Crunchyroll series link."))
            return

        valid_qualities = ["240p", "360p", "480p", "720p", "1080p", "hdrip"]
        if selected_quality not in valid_qualities:
            await message.reply_text(to_small_caps(
                "Invalid quality! Please provide a valid quality (e.g., 240p, 720p, 1080p, hdrip)."))
            return

        # Start download
        download_series(url, selected_quality)
        await message.reply_text(to_small_caps(f"Download started for: {url} in {selected_quality} quality."))

    except Exception as e:
        logger.error(f"Error downloading: {e}")
        await message.reply_text(to_small_caps(f"An error occurred while processing your request: {str(e)}"))

# Run the bot
if __name__ == "__main__":
    app.run()

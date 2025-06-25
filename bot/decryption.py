import subprocess
import logging
import os
from config import MP4DECRYPT_PATH

logger = logging.getLogger(__name__)

def decrypt_drm(video_file: str) -> str | None:
    """
    Decrypts DRM-protected video using mp4decrypt.

    Args:
        video_file (str): Path to the encrypted input video file.

    Returns:
        str | None: Path to decrypted file, or None on failure.
    """
    try:
        if not video_file.endswith(".mp4"):
            raise ValueError("Input file must be an .mp4 file")

        decrypted_file = video_file.replace(".mp4", "_decrypted.mp4")

        cmd = [MP4DECRYPT_PATH, video_file, decrypted_file]
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.stderr:
            logger.warning(f"mp4decrypt stderr: {result.stderr.strip()}")

        if os.path.exists(decrypted_file):
            logger.info(f"✅ DRM decryption successful: {decrypted_file}")
            return decrypted_file
        else:
            logger.error(f"❌ Decrypted file not found: {decrypted_file}")
            return None

    except subprocess.CalledProcessError as e:
        logger.error(f"❌ mp4decrypt failed: {e.stderr or str(e)}")
        return None
    except Exception as e:
        logger.error(f"❌ Error during DRM decryption: {str(e)}")
        return None

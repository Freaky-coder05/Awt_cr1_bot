import requests
from uuid import uuid4
from config import CRUNCHYROLL_PASSWORD, CRUNCHYROLL_USERNAME, CRUNCHYROLL_USER_AGENT
from typing import Optional, Dict

# Constants
PUBLIC_TOKEN = "d2piMV90YThta3Y3X2t4aHF6djc6MnlSWlg0Y0psX28yMzRqa2FNaXRTbXNLUVlGaUpQXzU="
APP_VERSION = "3.59.0"
DEVICE_NAME = "RMX2170"
DEVICE_TYPE = "realme RMX2170"
DEVICE_ID = str(uuid4())

WIDEVINE_UUID = "urn:uuid:edef8ba9-79d6-4ace-a3c8-27dcd51d21ed"
PLAYREADY_UUID = "urn:uuid:9a04f079-9840-4286-ab92-e65be0885f95"

def get_api_headers(extra_headers: Optional[Dict] = None) -> Dict:
    """Generate standard API headers with optional overrides."""
    headers = {
        "Connection": "Keep-Alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": f"Crunchyroll/{APP_VERSION} Android/13 okhttp/4.12.0"
    }
    if extra_headers:
        headers.update(extra_headers)
    return headers

def authenticate_crunchyroll() -> str:
    """
    Authenticate with Crunchyroll and return the access token.
    """
    login_url = "https://beta-api.crunchyroll.com/auth/v1/token"
    headers = get_api_headers({
        "User-Agent": CRUNCHYROLL_USER_AGENT,
    })

    data = {
        "username": CRUNCHYROLL_USERNAME,
        "password": CRUNCHYROLL_PASSWORD,
        "grant_type": "password",
        "scope": "offline_access",
        "client_id": "mobile.android",
        "client_secret": "kGhbDajT_3E5L3l"  # known secret (subject to change by CR)
    }

    try:
        response = requests.post(login_url, data=data, headers=headers)
        response.raise_for_status()

        result = response.json()
        if "access_token" in result:
            print("✅ Login successful.")
            return result["access_token"]
        else:
            print("❌ Login failed:", result)
            raise ValueError("Access token not received.")
    except requests.exceptions.RequestException as req_err:
        print("❌ Request error:", req_err)
        raise
    except Exception as err:
        print("❌ Authentication error:", err)
        raise

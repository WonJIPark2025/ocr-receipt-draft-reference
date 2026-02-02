from pathlib import Path
import os
from dotenv import load_dotenv

# project root
BASE_DIR = Path(__file__).resolve().parents[1]

# load .env
load_dotenv(BASE_DIR / ".env")

# OCR engine selector
OCR_ENGINE = os.getenv("OCR_ENGINE", "google")

# Google Vision service account key path
GOOGLE_APPLICATION_CREDENTIALS = (
    BASE_DIR / "config" / "secrets" / "api_key.json"
)

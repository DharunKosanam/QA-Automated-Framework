import os
from dotenv import load_dotenv

load_dotenv()  # loads values from a local .env file if present


class Config:
    # Which app to test. You'll set the real VM URL in .env.
    BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:5000")

    # Login credentials (read from .env, never hard-coded here)
    EMAIL = os.getenv("APP_EMAIL", "")
    PASSWORD = os.getenv("APP_PASSWORD", "")

    # Run browser with no visible window? False locally = you watch it work.
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

    # How long Playwright waits for an element before failing (ms)
    TIMEOUT_MS = int(os.getenv("TIMEOUT_MS", "10000"))

    # Performance budget: a reply should arrive within this many seconds
    MAX_RESPONSE_SECONDS = float(os.getenv("MAX_RESPONSE_SECONDS", "8"))


config = Config()

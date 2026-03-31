"""Load environment and app settings. See `.env.example` for tunable variables."""

import os

from dotenv import load_dotenv

load_dotenv()


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        return int(raw)
    except ValueError:
        # Unparseable env value: keep startup forgiving by using the default.
        return default


APP_TITLE = os.getenv("APP_TITLE", "Python AI Starter Template")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MAX_INPUT_CHARS = _env_int("MAX_INPUT_CHARS", 500)
MAX_REQUESTS_PER_SESSION = _env_int("MAX_REQUESTS_PER_SESSION", 10)
MAX_OUTPUT_TOKENS = _env_int("MAX_OUTPUT_TOKENS", 100)

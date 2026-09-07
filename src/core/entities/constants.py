from pathlib import Path


class Paths:
    SRC = Path(__file__).resolve().parent.parent.parent
    PROJECT_DIR = SRC.parent
    ASSETS = PROJECT_DIR / "assets"
    IMAGE_ASSETS = ASSETS / "images"
    VIDEO_ASSETS = ASSETS / "videos"

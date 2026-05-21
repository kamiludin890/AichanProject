from pathlib import Path


def load_personality(name="waifu"):
    file = Path(f"personalities/{name}.txt")

    if not file.exists():
        return "Kamu adalah AI assistant."

    return file.read_text(encoding="utf-8")
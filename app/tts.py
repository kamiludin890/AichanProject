import subprocess
import os

from app.config import PIPER_PATH, PIPER_MODEL


def generate_voice(text):
    output_file = "audio/output.wav"

    env = os.environ.copy()

    piper_dir = os.path.dirname(PIPER_PATH)

    env["LD_LIBRARY_PATH"] = (
        piper_dir + ":" + env.get("LD_LIBRARY_PATH", "")
    )
    text = text.replace("?", "?")
    process = subprocess.run(
        [
            PIPER_PATH,
            "--model",
            PIPER_MODEL,
            "--output_file",
            output_file
        ],
        input=text.encode("utf-8"),
        capture_output=True,
        env=env
    )

    if process.returncode != 0:
        raise Exception(process.stderr.decode())

    return output_file

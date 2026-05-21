import subprocess
from app.config import PIPER_PATH, PIPER_MODEL


def generate_voice(text):
    output_file = "audio/output.wav"

    cmd = f'echo "{text}" | {PIPER_PATH} --model {PIPER_MODEL} --output_file {output_file}'

    subprocess.run(cmd, shell=True)

    return output_file
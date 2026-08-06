import subprocess
from pathlib import Path    

def convert_tex(tex_file, output_folder):
    subprocess.run([
    str(Path("tools") / "ktools" / "ktech.exe"),
    str(tex_file),
    str(output_folder)
    ])
from pathlib import Path

def find_tex_files(temp_folder):
    return list(temp_folder.rglob("*.tex"))


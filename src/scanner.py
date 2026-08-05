from pathlib import Path

def find_zip_files():
    data_folder = Path("data")
    zip_files = list(data_folder.glob("*.zip"))

    return zip_files
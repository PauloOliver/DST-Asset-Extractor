from src.scanner import find_zip_files
from src.extractor import extract_zip_file
from pathlib import Path

def main():
    #Finding all the zip files
    zip_files = find_zip_files()
    if not zip_files:
        print("No zip files found in the 'data' folder.")
    else:
        for file in zip_files:
            # Extract the current ZIP file
            print(f"Found zip file: {file.name}")
            temp_folder = Path(f"temp/{file.stem}")
            temp_folder.mkdir(parents=True, exist_ok=True) 
            extract_zip_file(file, temp_folder)

if __name__ == "__main__":
    main()
from src/scanner import find_zip_files

def main():
    zip_files = find_zip_files()

    if not zip_files:
        print("No zip files found in the 'data' folder.")

    else:
        for file in zip_files:
            print(f"Found zip file: {file.name}")

if __name__ == "__main__":
    main()
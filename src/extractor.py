import zipfile

def extract_zip_file(zip_file_path, extract_to_folder):
    with zipfile.ZipFile(zip_file_path) as zip_file:
        zip_file.extractall(extract_to_folder)
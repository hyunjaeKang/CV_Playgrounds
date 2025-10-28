import requests
import os

def download_file(url, destination_folder="downloads"):
    """
    Downloads a file from a given URL and saves it to a specified folder.

    Args:
        url (str): The URL of the file to download.
        destination_folder (str): The local folder to save the downloaded file.
                                  Defaults to "downloads".
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Extract filename from URL or use a default
    filename = url.split('/')[-1]
    if not filename:  # Handle cases where URL ends with a slash or has no explicit filename
        filename = "downloaded_file" # You might want to add a more robust filename generation

    file_path = os.path.join(destination_folder, filename)

    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"File '{filename}' downloaded successfully to '{os.path.abspath(file_path)}'")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
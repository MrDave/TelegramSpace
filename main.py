import requests
from pathlib import Path


def download_picture(url, path):
    filename = f"{path}/hubble.jpeg"

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, "wb") as file:
        file.write(response.content)


def main():
    Path("images/").mkdir(exist_ok=True)
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    path = "images"
    download_picture(url, path)

if __name__ == "__main__":

    main()

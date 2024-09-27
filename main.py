import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor


# downloading function
def download_with_aria2c(url):
    try:
        subprocess.run(['aria2c', '-l', '--continue', '--max-tries=3', '--check-certificate=false',
                        '--min-tls-version=TLSv1.2', url])
    except Exception as e:
        print(f"failed to download: {url}: {e}")


# manage downloading link
def download_links(file_path):
    with open(file_path, 'r') as f:
        links = f.read().splitlines()

    with ThreadPoolExecutor(max_workers=3) as executor:  # max parallel download
        executor.map(download_with_aria2c, links)


if __name__ == "__main__":
    download_links(sys.argv[1]) # get file to download from links

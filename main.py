import os
import requests
from bs4 import BeautifulSoup
def download_cat_images(url, folder):
    os.makedirs(folder, exist_ok=True)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    imgs = soup.find_all('img')
    for img in imgs:
        img_url = img['src']
        if 'cat' in img_url:
            if not img_url.startswith('https:'):
                img_url = f"https:{img_url}"
            response = requests.get(img_url)
            if response.status_code == 200:
                filename = os.path.join(folder, os.path.basename(img_url))
                with open(filename, 'wb') as f:
                    f.write(response.content)
                    print(f"Изображение {filename} успешно скачано!")
wiki_url = "https://en.wikipedia.org/wiki/Cat"
image_folder = "cat_images"
download_cat_images(wiki_url, image_folder)
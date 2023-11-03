import os
import requests
from urllib.parse import urlencode, urlparse
from save_tools import save_picture
import argparse
from dotenv import load_dotenv


def get_nasa_images(api_key):
    payload = {'api_key': 'api_key'}
    response = requests.get(f'https://api.nasa.gov/EPIC/api/natural/images?', params=payload)
    response.raise_for_status()
    return response.json()


def main():
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    if not api_key:
        print('API ключ не найден')
        return

    parser = argparse.ArgumentParser(description='Скачивание фотографий с NASA API')
    parser.add_argument('-f', '--folder', type=str, help='Путь к папке для сохранения фотографий', required=True)
    args = parser.parse_args()

    nasa_images = get_nasa_images(api_key)
    url_base = 'https://api.nasa.gov/EPIC/archive/natural/'

    for nasa_image in nasa_images:
        name_epic = nasa_image['image']
        date_epic = nasa_image['date']
        full_name = os.path.join(args.folder, f"{name_epic}.png")
        url_photo = f'{url_base}/{date_epic[:4]}/{date_epic[5:7]}/{date_epic[8:10]}/png/{name_epic}.png?',params=payload
        save_picture(args.folder, url_photo, full_name)


if __name__ == '__main__':
    main()
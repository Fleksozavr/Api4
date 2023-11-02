import os
import requests
from urllib.parse import urlparse
from save_tools import save_picture
import argparse


def get_nasa_images(api_key):
    response = requests.get(f'https://api.nasa.gov/EPIC/api/natural/images?{urllib.parse.urlencode(params)}')
    response.raise_for_status()
    return response.json()


def main(args):
    load_dotenv()
    params = {'api_key': api_key}
    epic_api_key = os.getenv('EPIC_API_KEY')
    urlbase = 'https://api.nasa.gov/EPIC/archive/natural/'
    folder = os.path.join(os.path.expanduser('~'), 'Desktop', 'Api4', 'Images')
    filename = 'epic'
    parser = argparse.ArgumentParser(description='Скачивание фотографий с NASA API')
    parser.add_argument('-k', '--api_key', type=str, help='API ключ для доступа к NASA API', required=True)
    parser.add_argument('-f', '--folder', type=str, help='Путь к папке для сохранения фотографий', required=True)
    args = parser.parse_args()
    nasa_images = get_nasa_images(args.api_key)

    for nasa_image in nasa_images:
        name_epic = nasa_image['image']
        date_epic = nasa_image['date']
        full_name = os.path.join(args.folder, f"{name_epic}.png")
        url_photo = f'{url_base}/{epic_date[:4]}/{date_epic[5:7]}/{date_epic[8:10]}/png/{date_epic}.png?{urllib.parse.urlencode(params)}'
        save_picture(args.folder, url_photo, full_name)


if __name__ == '__main__':
    main()
import argparse
import requests

from save_tools import save_picture, get_extension


def main():
    nasa_token = os.getenv('nasa_token')
    parser = argparse.ArgumentParser(description='Скачивает фотографии с сервиса NASA Astronomy Picture of the Day (APOD)')

    # parser.add_argument('--api_key', type=str, required=True,default=', help='API-ключ для доступа к сервису NASA')
    parser.add_argument('--count', type=int, default=30, help='Количество фотографий для скачивания')
    parser.add_argument('--folder', type=str, required=True, help='Путь к папке для сохранения фотографий')

    args = parser.parse_args()
    folder = args.folder
    count = args.count

    payload = {'count': count, 'api_key': nasa_token}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    filename = 'nasa_apod_'

    for index, api_response in enumerate(response.json(), 1):
        url = api_response['url']
        extension = get_extension(url)
        full_name = f'{filename}{index}{extension}'
        save_picture(folder, url, full_name)


if __name__ == '__main__':
    main()
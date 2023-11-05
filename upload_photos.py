import os
import random
import time
import argparse
from dotenv import load_dotenv
import telegram

def main():
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_channel_id = os.getenv('TELEGRAM_CHANNEL_ID')
    bot = telegram.Bot(token=telegram_token)

    parser = argparse.ArgumentParser(description='Отправка случайных фотографий в чат Telegram')
    parser.add_argument('--time',
                        type=int,
                        default=14400,
                        help='Интервал времени (в секундах) между отправкой случайных фотографий')
    parser.add_argument('--folder',
                        type=str,
                        default='folder',
                        help='Путь к папке, содержащей фотографии для отправки')
    parser.add_argument('--telegram_token',
                        type=str,
                        help='Токен бота Telegram')
    parser.add_argument('--telegram_channel_id',
                        type=str,
                        help='ID канала Telegram')
    args = parser.parse_args()
    folder = args.folder
    periodicity = args.time
    telegram_token = args.telegram_token or telegram_token
    telegram_channel_id = args.telegram_channel_id or telegram_channel_id

    while True:
        all_files = []
        for root, _, files in os.walk(folder):
            all_files.extend([os.path.join(root, file) for file in files])

        if not all_files:
            print(f'Папка {folder} не содержит файлов.')
            break

        random_file = random.choice(all_files)
        try:
            with open(random_file, 'rb') as file_obj:
                bot.send_document(chat_id=telegram_channel_id, document=file_obj)
            print(f'Отправлена фотография: {random_file}')
        except telegram.error.TelegramError as e:
            print(f'Произошла ошибка при отправке: {e}')

        time.sleep(periodicity)


if __name__ == '__main__':
    main()
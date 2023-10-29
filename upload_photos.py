import os
import random
import time
import argparse
from dotenv import load_dotenv
import telegram

def main():
    load_dotenv()
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
    bot = telegram.Bot(token=TELEGRAM_TOKEN)

    parser = argparse.ArgumentParser(description='Отправка случайных фотографий в чат Telegram')
    parser.add_argument('--time',
                        type=int,
                        default=14400,
                        help='Интервал времени (в секундах) между отправкой случайных фотографий')
    parser.add_argument('--folder',
                        type=str,
                        default='folder',
                        help='Путь к папке, содержащей фотографии для отправки')
    args = parser.parse_args()
    folder = args.folder
    periodicity = args.time

    while True:
        all_files = []
        for root, _, files in os.walk(folder):
            all_files.extend([os.path.join(root, file) for file in files])

        if not all_files:
            print(f'Папка {folder} не содержит файлов.')
            break

        random_file = random.choice(all_files)
        try:
            with open(random_file, 'rb') as file:
                bot.send_document(chat_id=TELEGRAM_CHANNEL_ID, document=file)
            print(f'Отправлена фотография: {random_file}')
        except telegram.error.TelegramError as e:
            print(f'Произошла ошибка при отправке: {e}')

        time.sleep(periodicity)


if __name__ == '__main__':
    main()
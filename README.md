# Космический Телеграм

Этот проект умеет скачивать фотографии с последнего запуска и рассылать их в телеграм-канал

## Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:

`pip install -r requirements.txt`

Перед запуском программы не забудьте склонировать проект или скачать его в архив. В папке с проектом не забудьте создать .env файл, где укажите ваши собственные токены Nasa и другие([создать токен](https://api.nasa.gov))

`NASA_API_TOKEN=ваш токен NASA`

## Использование

### Если хотите поменять название папки

Для того чтобы изменить название папки куда сохраняются фотографии, вам просто необходимо указать аргумент в запуске файла:

`python fetch_spacex_images.py --folder картинки`

## Как запустить файл fetch_epic_photo.py

Этот файл скачивает картинки последнего запуска NASA и сохранянет их в папку images Для скачивания картинок необходимо просто запустить файл:

`python fetch_epic_photo.py`

## Как запустить fetch_apod.py

Этот файл скачивает картинки последнего запуска NASA с указанным ваши кол-вом и сохраняет их в папку Images

Для скачивания картинок необходимо запустить файл, где в качестве аргумента вы укажите кол-во картинок, которое вам необходимо скачать:

`python fetch_apod.py --count 30`

Также вы можете запустить этот файл без аргумента, он будет скачивать 30 картинок по умолчанию:

`python fetch_spacex_images.py`

## Как запустить файл fetch_spacex_images.py

Этот файл скачивает картинки последнего запуска NASA с указанным вами id и сохраняет их в папку images
Для скачивания картинок необходимо запустить файл, где в качестве аргумента будет ваш id:

`python fetch_spacex_images.py --id (id)`

Также вы можете запустить этот файл без аргумента, он будет работать с id последнего запуска:

`python fetch_spacex_images.py`

## Как запутсить upload_photos.py

### Настройка Telegram

#### Получение токена

Скачайте, или войдите в [telegram](https://web.telegram.im) с помощью браузера. Затем вам нужно создать своего бота, с помощью уже имеющегося в телеграме бота [BotFather](https://t.me/BotFather), и получить API токен бота, например:

`958423683:AAEAtJ5Lde5YYfkjergber`

#### Создание, и настройка телеграм канала

После получения телеграм токена, и создания бота вам нужно будет его где-то применить, для этого нужно [создать](https://skillbox.ru/media/marketing/kak-sozdat-kanal-v-telegram-so-smartfona-i-s-desktopa-instruktsiya-so-skrinshotami/) телеграм канал, добавить, и назначить бота администратором.
Теперь, нужно получить chat id канала. Для этого нужно сделать несколько манипуляций:
1. Откройте чат в Telegram, для которого вы хотите узнать ID.
2. Напишите в этот чат любое сообщение.
3. Откройте браузер и перейдите по ссылке: https://api.telegram.org/bot<token>/getUpdates, где <token> - это токен вашего бота.
4. Найдите в ответе сервера объект "chat", который соответствует вашему чату. В этом объекте будет поле "id", которое и является ID вашего чата.
5. Полученное значение нужно добавить в переменную telegram_channel_id, например:

`telegram_channel_id = os.getenv('TELEGRAM_CHANNEL_ID')`

### Отправка фото

Для отправки фото в телеграм канал необходимо запустить файл, где в качестве аргумента будет указан ваша переодичность отправки фото:

`python upload_photos.py --time 14440`

Важно подметить что переодичность указывается в секундах

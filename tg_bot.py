import telebot

bot = telebot.TeleBot('6713450946:AAEe4RfMoeGRZx5In3WDiEPG7Iaov1aVHYA')

channel_id = '-1002040903992'
photo_caption = 'Фотография запуска SpaceX'

photo = open('C:\\Users\\user\\Desktop\\Api4\\Images\\nasa_apod_1.jpg', 'rb')
bot.send_photo(channel_id, photo)

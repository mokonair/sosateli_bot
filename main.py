import telebot
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
# BOT_TOKEN = '5943556153:AAF9X10z0_33vpHWClduIhweHJjcQpHDDGg'
bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)


@bot.message_handler(commands=['all'])
def all_tagger(message):
    bot.send_message(message.chat.id,
                     'ALL TAG: @arturstashin, @Ekhlaboy, @genatonk, @German_Tonkonog, @gonzotape, @GrimmViking, '
                     '@lii_mo_nad, @mokonair, @send_your_nudes, @suru_ru_ru')


@bot.message_handler(commands=['dota'])
def dota_tagger(message):
    bot.send_message(message.chat.id,
                     'DOTA TAG: @arturstashin, @gonzotape, @GrimmViking, @mokonair, @send_your_nudes, @suru_ru_ru')


bot.polling(none_stop=True, interval=0)
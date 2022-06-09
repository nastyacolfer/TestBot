import telebot
from telebot import types
import random

token = '5520079906:AAG633_q2e2C9UCe3fPTVnRUAjuHPr7c4JA'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    sticker = open('hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.add('Список', 'Что бы скушать?')
    bot.send_message(message.chat.id, "Шалом шаббат!", reply_markup=keyboard)


@bot.message_handler()
def menu(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    _id = message.chat.id

    if message.text == "Список":
        bot.send_message(_id, "Твой список продуктов:", parse_mode="html")

    elif message.text == "Что бы скушать?":
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.add("Выпечка", "Погрызть", "Сладкое", "Вернуться в меню")
        bot.send_message(_id, "Выбери категорию", reply_markup=keyboard)

    if message.text == "Сладкое":
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        bot.send_message(_id, "Может ты хочешь... ", parse_mode="html")
        sweets = ["Вафли", "Печенюхи", "Мюсли", "Мармелад", "Конфеты", "Шоколад"]

        ans = sweets[random.randint(0, len(sweets)-1)]
        bot.send_message(_id, ans.lower()+'?', parse_mode="html")
        link = "https://edadeal.ru/moskva/offers?search="+ans+"&title"+ans
        bot.send_message(_id, link, parse_mode="html")

    if message.text == "Вернуться в меню":
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Список', 'Что бы скушать?')
        bot.send_message(message.chat.id, "Шалом шаббат!", reply_markup=keyboard)


@bot.message_handler()
def category(message):
    _id = message.chat.id
    print("AAAAAAAA")
    if message.text == "Cладкое":
        print("ssssssssssssss")
        keyboard = telebot.types.ReplyKeyboardMarkup(True)

        bot.send_message(_id, "Может ты хочешь... ", parse_mode="html")
        sweets = ["Вафли", "Печенюхи", "Мюсли", "Мармелад", "Конфеты", "Шоколад"]

        ans = sweets[random.randint(0, len(sweets)-1)]
        bot.send_message(_id, ans.lower()+'?', parse_mode="html")
        link = "https://edadeal.ru/moskva/offers?search="+ans+"&title"+ans
        bot.send_message(_id, link, parse_mode="html")

    elif message.text == "Вернуться в меню":
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Список', 'Что бы скушать?')
        bot.send_message(message.chat.id, "Шалом шаббат!", reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "напиши чево собираешься купить\n", parse_mode="html")
    bot.send_message(message.chat.id, "если хочешь найти цены, начни сообщение с <b>хочу</b>", parse_mode="html")


@bot.message_handler()
def get_user_message(message):
    ph = str(message.text)
    check = ph.find("хочу")
    if check != -1:
        keyword = ph.split(" ")[1]
        text = "Ага, ищу "+keyword+"..."
        bot.send_message(message.chat.id, text, parse_mode="html")
        link = "https://edadeal.ru/moskva/offers?search="+keyword+"&title"+keyword
        bot.send_message(message.chat.id, link, parse_mode="html")
    else:
        bot.send_message(message.chat.id, "перехочеш, я еще не написала эту часть кода", parse_mode="html")


bot.polling(none_stop=True)

import telebot


token = '5520079906:AAG633_q2e2C9UCe3fPTVnRUAjuHPr7c4JA'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "шалом шаббат, долбоеб", parse_mode="html")
    sticker = open('hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "напиши чево собираешься купить\n", parse_mode="html")
    bot.send_message(message.chat.id, "если хочешь найти цены, начни сообщение с <b>хочу</b>", parse_mode="html")
    sticker = open('hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)


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

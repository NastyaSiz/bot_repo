import telebot

bot = telebot.TeleBot('TOKEN')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message) :
    bot.reply_to(message, f'Я бот. Приємно познайомитись, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message) :
    if message.text.lower() == 'привіт' :
        bot.send_message(message.from_user.id, 'Привіт!')
    else :
        bot.send_message(message.from_user.id, 'Не розумію тебе(')

bot.polling(none_stop=True)

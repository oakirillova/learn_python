
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
logging.basicConfig(format='%(asktime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    logging.info('Bot is getting started')

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling() #для запуска бота
    mybot.idle() #работать, пока мы не остановим бот


def greet_user(bot, update):
    text = 'Привет, дружок-пирожок!'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет, {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    print(user_text)
    update.message.reply_text(user_text)


main()

team1 = 0
team2 = 0

current_result = 1

while current_result != 0:
    current_result = int(input())
    if current_result > 0:
        team1 += current_result
    else:
        team2 -= current_result

if team1 > team2:
    print("quack quack")
else:
    print("quack")

#сумма результатов команды 1


















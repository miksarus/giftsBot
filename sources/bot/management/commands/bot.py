from os import error
from django.core.management.base import BaseCommand
from django.conf import settings

from telegram import Bot
from telegram import Update
from telegram.bot import log
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request

from bot.models import Message
from bot.models import Profile
from bot.predictions import get_prediction


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f"Произошла ошибка: {e}"
            print(error_message)
            raise e

    return inner


@log_errors
def do_echo(updater: Update, context: CallbackContext):
    chat_id = updater.message.chat_id
    text = updater.message.text

    p, is_new = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': updater.message.from_user.username,
        })
    m = Message(profile=p, text=text)
    m.save()

    reply_text = "Пока я умею только две вещи:\n/takechance - и тебе может повезти\n/count - счётчик сколько сообщений вы отправили"
    updater.message.reply_text(text=reply_text)


@log_errors
def do_count(updater: Update, context: CallbackContext):
    #print(updater)
    chat_id = updater.message.chat_id
    p, is_new = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': updater.message.from_user.username,
        })
    count = Message.objects.filter(profile=p).count()

    updater.message.reply_text(
        text=f"От вас было отправлено {count} сообщений", )


@log_errors
def do_takechance(updater: Update, context: CallbackContext):
    chat_id = updater.message.chat_id
    
    p, is_new = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': updater.message.from_user.username,
        })

    reply_text = get_prediction()
    updater.message.reply_text(text=reply_text)


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        # 1 -- правильное подключение
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
            base_url=settings.PROXY_URL,
        )
        #print(bot.get_me())

        # 2 -- обработка сообщений
        updater = Updater(
            bot=bot,
            use_context=True,
        )

        command1_handler = CommandHandler('takechance', do_takechance)
        updater.dispatcher.add_handler(command1_handler)

        command_handler = CommandHandler('count', do_count)
        updater.dispatcher.add_handler(command_handler)

        message_handler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_handler)

        # 3 -- запустить бесконечную обработку входящих сообщений
        updater.start_polling()
        updater.idle()

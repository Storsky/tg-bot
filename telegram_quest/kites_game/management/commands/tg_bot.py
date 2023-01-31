from django.core.management.base import BaseCommand
from telebot import TeleBot, types
from kites_game.models import *

BOT_TOKEN='5606225088:AAHVjbzthYmLbdgdnW5U5TTj5bZ3PJSLFmE'
bot = TeleBot(BOT_TOKEN, threaded=False)


class Command(BaseCommand):
    help = 'Implemented bot to Django'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()
        


    


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    try:
        player = Player.objects.get(chat_id= message.chat.id)
    except Player.DoesNotExist:
        player = Player(chat_id= message.chat.id)
        player.save()
    for trigger in player.chapter_on.from_thread.all():
        btn = types.KeyboardButton(trigger.action)
        if trigger.action == 'Далее':
            player.next_chapter = trigger.to_thread
        markup.add(btn)

    player.save()
    bot.send_photo(message.chat.id,
                    player.chapter_on.image)
    bot.send_message(message.chat.id,
                    player.chapter_on.text,
                     reply_markup=markup)

@bot.message_handler(commands=['restart'])
def restart(message):
    chat_id = message.chat.id
    bot.send_message(message.chat.id,
                    '/start для начала игры')
    player = Player.objects.get(chat_id= chat_id)                
    player.chapter_on = Thread.objects.get(id=1)
    player.next_chapter = 2
    player.save()

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    player = Player.objects.get(chat_id= message.chat.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Далее':
        player.chapter_on = player.next_chapter
        player.save()
    else:
        try:
            choice_thread = player.chapter_on.from_thread.filter(action = message.text)
            player.chapter_on = choice_thread[0].to_thread
            player.save()
        except NameError:
            bot.send_message(message.from_user.id,
                    recent_thread.text,
                    reply_markup=markup)

    
    recent_thread = player.chapter_on
    for trigger in recent_thread.from_thread.all():
        btn = types.KeyboardButton(trigger.action)
        if trigger.action == 'Далее':
            player.next_chapter = trigger.to_thread
        markup.add(btn)
    player.save()
    try:
        bot.send_photo(message.from_user.id,
                        recent_thread.image)
    except ValueError: pass
    bot.send_message(message.from_user.id,
                    recent_thread.text,
                    reply_markup=markup)
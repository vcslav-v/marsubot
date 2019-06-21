from tele_bot_tools import *
from tools import *
from app import models
from app import bot
from app import db
from set import *


@bot.message_handler(commands=['start'])
def hi_msg(msg):
    """
    Стартовое сообщение дополнительно кодируется xxx*, где xxx команда, а * любая доп
    информация
    """

    try:
        command = msg.text[7:10] # ищем комманду в стартовом сообщении
    except:
        command = '000' # если сообщение не кодировано, скидываем в вариант по умолчанию

    if command == 'dwn': # команда на скачивание продукта
        try:
            productId = int(msg.text[10:])
            msgGo, addTag, remTag = msg_dwn_usr(productId)
            productData = models.product.query.filter_by(Id = productId).first()
            productFileId = productData.FileIdTelega
            new_user(msg.from_user.id)
            poster(bot, msg.chat.id, msgGo, addTag=addTag, remTag=remTag, doc=productFileId)
        except Exception as e:
            poster(bot, msg.chat.id, addTag)
    else:
        productFileId = 0

    if command == '000':
        msgStart = msg_start
        tfExUser = new_user(msg.from_user.id)
        if tfExUser == 'exUser':

            poster(bot, msg.chat.id, msgContinue)
        else:
            poster(bot, msg.chat.id, msgStart)

@bot.message_handler(content_types=['photo'])
def photo(msg):
    poster(bot, msg.chat.id, msg)

@bot.message_handler(content_types=['document'])
def doc(msg):
    poster(bot, msg.chat.id, msg)


@bot.message_handler(content_types=['text'])
def any_messages(msg):
    poster(bot, msg.chat.id, 'message!')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    pass
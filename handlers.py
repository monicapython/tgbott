from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters

updater = Updater(5432348694:AAG9n83ZyE3BRt8uLd_ygb51SwgelROyiUM)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))

dp.add_handler(MessageHandler(Filters.chat_type.private, forward_to_chat))

dp.add_handler(MessageHandler(Filters.chat(-836711289) &amp;amp; Filters.reply, forward_to_user))

def start(update, context):
    update.message.reply_text(Hey! How you doin?)

    user_info = update.message.from_user.to_dict()

    context.bot.send_message(
        chat_id=-836711289,
        text=f"? Connected {user_info}.",
    )
    
def forward_to_chat(update, context):
    update.message.forward(chat_id=-836711289)
    
 def forward_to_user(update, context):
    user_id = update.message.reply_to_message.forward_from.id
    context.bot.copy_message(
        message_id=update.message.message_id,
        chat_id=user_id,
        from_chat_id=update.message.chat_id
    )

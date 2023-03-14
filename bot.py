import os
import telegram
from telegram.ext import Updater, CommandHandler

updater = Updater(token=os.environ['6279749316:AAGtRyvmdGS6ZcG_lFy3ygAO-B2BsH-RDVo'])
dispatcher = updater.dispatcher
bot = telegram.Bot(token=os.environ['6279749316:AAGtRyvmdGS6ZcG_lFy3ygAO-B2BsH-RDVo'])
def download(update, context):
    video_url = context.args[0]
    os.system(f"youtube-dl {video_url}")
    video_file = max(os.listdir('.'), key=os.path.getctime)
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(video_file, 'rb'))

download_handler = CommandHandler('download', download)
dispatcher.add_handler(download_handler)

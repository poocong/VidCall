# . 
from pyrogram import filters, Client
from pyrogram.types import Message
import os
import psutil
import time
from datetime import datetime


def humanbytes(size):
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"



@Client.on_message(filters.command('ping') & ~filters.private & ~filters.channel)
async def ping(_, message):
   total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    start = datetime.now()
    response = await message.reply_text(
        ">> Pong!"
    )
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await response.edit_text(f"**Pong!**\n`⚡{resp} ms`\n\n<b><u>Music System Stats:</u></b>\nDisk Space:{total}\nUsed:{used}({disk_usage}%\nFree:{free}\n\nRam Usage:{cpu_usage}%\nCPU Usage:{cpu_usage}%")

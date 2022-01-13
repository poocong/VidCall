# . 
from pyrogram import filters, Client
from pyrogram.types import Message
import os
import shutil
import psutil
from sys import version
import time
from utils.sys_stats import humanbytes
from datetime import datetime


@Client.on_message(filters.command('ping') & ~filters.private & ~filters.channel)
async def ping(_, message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = f"{psutil.cpu_percent()} %"
    ram_usage = f"{psutil.virtual_memory().percent} %"
    start = datetime.now()
    response = await message.reply_text(
        ">> Pong!"
    )
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await response.edit_text(f"**Pong!**`⚡{resp} ms`\n\n<b><u>Music System Stats:</u></b>\nRAM:{ram_usage}\nCPU:{cpu_usage}\nUsed:{used}({disk_usage}")

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
    start = datetime.now()
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = f"{psutil.cpu_percent()} %"
    ram_usage = f"{psutil.virtual_memory().percent} %"
    response = await message.reply_text(
        ">> Pong!"
    )
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await response.edit_text(f"""**Pong!**`⚡{resp} ms`
     
<b><u>Music System Stats:</u></b>
RAM:{ram_usage}
CPU:{cpu_usage}
Used:{used}({disk_usage}""")

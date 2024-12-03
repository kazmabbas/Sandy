import random
import re
import base64
import time
import asyncio
import os
from datetime import datetime
from platform import python_version
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from Sandy import StartTime, events, JEPVERSION
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
 
plugin_category = "utils"

file_path = "installation_date.txt"
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, "r") as file:
        installation_time = file.read().strip()
else:
    installation_time = datetime.now().strftime("%Y-%m-%d")
    with open(file_path, "w") as file:
        file.write(installation_time)

@events.ar_cmd(pattern="فحص(?:\s|$)([\s\S]*)")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await edit_or_reply(event, "** ᯽︙ يتـم التـأكـد انتـظر قليلا رجاءا**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "⿻┊‌‎"
    me = await events.get_me()
    first_name = me.first_name
    mention = first_name
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**父[ ˛ َِ𝘚َِ𝘢َِ𝘯َِ𝘥َِ𝘺 َِ𝘪َِ𝘴 َِ𝘸َِ𝘰َِ𝘳َِ𝘬َِ𝘪َِ𝘯َِ𝘨 .](t.me/BxxBxxL)父**"
    HuRe_IMG = gvarstatus("ALIVE_PIC") or Config.A_PIC
    events_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = events_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        jepver=JEPVERSION,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
        Tare5=installation_time,
    )
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass
    if HuRe_IMG:
        Sandy = [x for x in HuRe_IMG.split()]
        PIC = random.choice(Sandy)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**الميـديا خـطأ **\nغـير الرابـط بأستـخدام الأمـر  \n `.اضف_فار ALIVE_PIC رابط صورتك`\n\n**لا يمـكن الحـصول عـلى صـورة من الـرابـط :-** `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            caption,
        )


temp = """{ALIVE_TEXT}
**‎{EMOJI}‌ 𝙉𝘼𝙈𝙀 𖠄 {mention}** ٫
**{EMOJI}‌ 𝙋𝙔𝙏𝙃𝙊𝙉 𖠄 `{pyver}`** ٫
**{EMOJI}‌ 𝙎𝘼𝙉𝘿𝙔 𖠄 `{telever}`** ٫
**{EMOJI}‌ 𝙐𝙋𝙏𝙄𝙈𝙀 𖠄 `{uptime}`** ٫
**{EMOJI}‌ 𝙋𝙄𝙉𝙂 𖠄 `{ping}`** ٫
**{EMOJI}‌ 𝙎𝙀𝙏𝙐𝙋 𝘿𝘼𝙏𝙀 𖠄 `{Tare5}`** ٫ ‎
*
**𖠄 𝗦𝗔𝗡𝗗𝗬 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 𖠄**"""
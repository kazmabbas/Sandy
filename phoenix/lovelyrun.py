from telethon import events
import Sandy.client
from Sandy.lovely import Lovely
import time
lovely = Lovely()
client = Sandy.client.client


@events.register(events.NewMessage)
async def lovelyrun(event):
    if '.lovely' in event.raw_text:
        time.sleep(0.3)
        for d in lovely.lovely:
            time.sleep(0.3)
            await event.edit(d)

from telethon import events
import Sandy.client
import asyncio
client = Sandy.client.client

@events.register(events.NewMessage(outgoing=True, pattern=".spam ?(.*)"))
async def delayspam(e):
    try:
        args = e.text.split(" ", 3)
        dark = float(args[1])
        count = int(args[2])
        msg = str(args[3])
    except BaseException:
        return await e.edit("**Ishlatish :** spam <each time> <count> <message>")
    await e.delete()
    try:
        for i in range(count):
            await e.respond(msg)
            await asyncio.sleep(dark)
    except Exception as u:
        await e.respond(f"**Hatolik :** `{u}`")

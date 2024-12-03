from telethon import events
import Sandy.client
import time
client = Sandy.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.alive'))
async def alive(event):
		client = event.client
		me = await client.get_me()
		username = me.username
		img = await client.download_profile_photo(username)
		time.sleep(0.5)
		await event.respond(f"""**Foydalanuvchi:** @{username}
**Sandy Userbot:** https://t.me/i0i0ii

**Developer:** @i0i0ii
			
v.1.2.0

📥 INSTALL 

$ `pkg update && pkg upgrade`

$ `apt update && apt upgrade`

$ `pkg install git`

$ `pkg install python`

$ `git clone https://github.com/1mrxe1/usefinal`

$ `python setup.py`

$ `python main.py`""", file=img)
		await event.message.delete()

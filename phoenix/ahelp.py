from telethon import events

import Sandy.client
client = Sandy.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".ahelp"))
async def ahelp(event):
	client.parse_mode = "html"
	await event.delete()
	messagelocation = event.to_id
	await event.client.send_message(messagelocation, ("""
<b>ANIMATSIONS MENU</b>

[01] Monster art - .monster
[02] Pig art - .pig
[03] Killer art - .killer
[04] Gun art - .gun
[05] Dog art - .dog
[06] BIG hello - .hello
[07] Hello my friend art - .hmf
[08] Couple art - .couple
[09] Superme art - .sup
[10] Welcome text - .welc
[11] Snake art - .asnake
[12] Cat art - .cat
[13] Bye text - .bye
[14] Shitos art - .shitos
[15] Dislike bigf - .dislike
[16] HYPNO - .hypno
[17] squ - .squ
[18] Kiler - .kiler
[19] Train anim - .train
[20] Alien anim - .rocket
[21] Heart anim - .hart
[22] Raped anim - .raped
[23] FNL - .fnl
[24] Monkey anim - .monkey
[25] Hands anim - .hands
[26] Count number - .count
[27] BIG F - .kf
[28] F - .f {text}
[29] BIG oof - .bigoff
[30] Flower - .flower {text}
[31] Hearts anim - .vheart {text}
[32] Love you anim - .luvart {text}
[33] I love you art - .iloveu

<b>Developer:</b> @I0I0II 
<b>Channel:</b> @CNN0N
"""))

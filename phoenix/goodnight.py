from telethon import events
import Sandy.client
client = Sandy.client
import random

gn = ["""
┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█
┌▀█╔══╗╔══╗╔══╗╔══╗▀█
┌▀█║╔═╣║╔╗║║╔╗║╚╗╗║▀█
┌▀█║╚╗║║╚╝║║╚╝║╔╩╝║▀█
┌▀█╚══╝╚══╝╚══╝╚══╝▀█
┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█
┌▀█░░░░░░░░░░░░░░░░▀█
┌▀█░░█▌▌█▐▀▐░▌▀█▀░░▀█
┌▀█░░█▐▌█▐▐▐▀▌░█░░░▀█
┌▀█░░█░▌█▐█▐░▌░█░░░▀█
┌▀█░░░░░░░░░░░░░░░░▀█
┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█ 
""",
"""
🌙.     *       ☄️      
🌟   .  *       .         
                       *   .      🛰     .        ✨      *
  .     *   SLEEP WELL        🚀     
      .              . . SWEET DREAMS 🌙
. *       🌏 GOOD NIGHT         *
                     🌙.     *       ☄️      
🌟   .  *       .         
                       *   .      🛰     .        ✨      *
"""]

@events.register(events.NewMessage(pattern=".gn"))
async def goodnight(event):
  ggn = random.choice(gn)
  return await event.edit(ggn)
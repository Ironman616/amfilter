# Don't Remove Credit @AmRobots_Bots
# Subscribe YouTube Channel For Amazing Bot @AmRobotsTech
# Ask Doubt on telegram @Am_Robots


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

import requests 

import os


API = "https://apis.xditya.me/lyrics?song="

@Client.on_message(filters.text & filters.command(["lyrics"]))
async def sng(bot, message):
    amrobots = await bot.ask(chat_id=message.from_user.id, text="Now send me your song name.")
    if amrobots.text:
        mee = await amrobots.reply_text("`Searching 🔎`")
        song = amrobots.text
        chat_id = message.from_user.id
        rpl = lyrics(song)
        await mee.delete()
        try:
            await mee.delete()
            await bot.send_message(chat_id, text = rpl, reply_to_message_id = message.id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs ", url = f"t.me/AmRobots_Bots")]]))
        except Exception as e:                            
            await amrobots.reply_text(f"I Can't Find A Song With `{song}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url = f"t.me/AmRobots_Bots")]]))
    else:
        await amrobots.reply_text("Send me only text Buddy.")


def search(song):
    r = requests.get(API + song)
    find = r.json()
    return find
       
def lyrics(song):
    fin = search(song)
    text = f'**🎶 Sᴜᴄᴄᴇꜱꜰᴜʟʟy Exᴛʀᴀᴄᴛᴇᴅ Lyɪʀɪᴄꜱ Oꜰ {song}**\n\n'
    text += f'`{fin["lyrics"]}`'
    text += '\n\n\n**Made By Artificial Intelligence**'
    return text



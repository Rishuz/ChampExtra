import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from ChampuMusic import app
from ChampuMusic.utils.database import add_served_chat, get_assistant


start_txt = """**
<blockquote>✪ 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗥𝗶𝘀𝗵𝘂 𝗥𝗲𝗽𝗼𝘀 ✪</blockquote>

➲ ᴇᴀsʏ ʜᴇʀᴏᴋᴜ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ✰  
➲ ɴᴏ ʙᴀɴ ɪssᴜᴇs ✰  
➲ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰  
➲ 𝟸𝟺/𝟽 ʟᴀɢ-ғʀᴇᴇ ✰

► sᴇɴᴅ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍs!
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{app.username}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ʀɪsʜᴜ", url="https://t.me/Ur_rishu_143"),
          InlineKeyboardButton("ʀɪsʜᴜ", url="https://t.me/ur_support07"),
          ],
               [
                InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/rishu1286"),

],
[
              InlineKeyboardButton("ᴍᴜsɪᴄ", url=f"https://github.com/RishuBot/Rishu_Music"),
              InlineKeyboardButton("sᴛʀɪɴɢ", url=f"https://github.com/RishuBot/RishuStringHack"),
              ],
              [
       
InlineKeyboardButton("ᴄʜᴀᴛʙᴏᴛ", url=f"https://github.com/RishuBot/RishuChatBot"),
]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo=config.START_IMG_URL,
        caption=start_txt,
        reply_markup=reply_markup
    )




@app.on_message(
    filters.command(
        ["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


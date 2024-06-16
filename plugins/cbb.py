




from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🤖 My Creator :</b> <a href='https://t.me/Urr_Sanjii'>𝐒ᴀɴJɪ 𝐒ᴀᴍᴀ</a> \n<b>📝 Language :</b> <a href='https://python.org'>Python 3</a> \n<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram {__version__}</a> \n<b>📢 Support :</b> <a href='https://t.me/Request4anime'>𝐁ᴏᴛ 𝐒ᴜᴘᴘᴏʀᴛ</a> \n<b>🧑‍💻 Developer :</b> <a href='tg://user?id={OWNER_ID}'>𝐙ᴏʀᴏ 𝐒ᴀᴍᴀ</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass







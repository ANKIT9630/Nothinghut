#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>∞۝Aⲛⲕⲓⲧ۝∞</a>\n○ Creator : <a href='https://t.me/Saurav3BV6SA9LLElon7Musk'>꧁༒༺☠︎☬ S҉₳𝖀𝕽₳V҉☠︎☬༒꧂</a>\n○ Channel: @defenderofthemultiverse Group : @thewarriorsreal</b>",
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

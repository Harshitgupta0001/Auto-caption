from pyrogram import Client, filters, errors, types
from pyrogram.types import *
@Client.on_callback_query()
async def cb_handler(bot, query: CallbackQuery):
     if query.data == "about":
        await query.message.edit_text(text="hii")

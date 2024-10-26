


@Client.on_callback_query()
async def cb_handler(bot, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
    elif query.data == "about":
        buttons1 = [[
            InlineKeyboardButton('🔙 back', callback_data='start'),
            InlineKeyboardButton('🔒 Cʟᴏsᴇ', callback_data='close_data')
        ]]
        await bot.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
        )
        reply_markup = InlineKeyboardMarkup(buttons1)
        await query.message.edit_text(
            text="hii",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

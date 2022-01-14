#@blinderTG

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from telegraph import upload_file

@Client.on_message(filters.command(["ttmedia", "tgraph", "telegraph"]))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("ᎡᎬᏢᏞᎽ Ͳϴ Ꭺ ՏႮᏢᏢϴᎡͲᎬᎠ ᎷᎬᎠᏆᎪ ҒᏆᏞᎬ🧑‍💻")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Not supported!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            f"<b>Link:-</b>\n\n <code>https://telegra.ph{response[0]}</code>",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🔗ϴᏢᎬΝ ᏞᏆΝᏦ", url=f"https://telegra.ph{response[0]}"),
                    InlineKeyboardButton(text="🔄ՏᎻᎪᎡᎬ ᏞᏆΝᏦ", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
                ],
                [InlineKeyboardButton(text="🚫 ᏟᏞϴՏᎬ", callback_data="close_data")]
            ]
        )
    )
    finally:
        os.remove(download_location)

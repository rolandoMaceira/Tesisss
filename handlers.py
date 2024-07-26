# handlers.py
from pyrogram import Client, filters
from ai21_api import get_ai21_response

async def handle_message(client, message):
    if message.text.startswith("/start"):
        await message.reply("Hola, soy tu bot!")
    else:
        bot_response = get_ai21_response(message.text)
        if bot_response:
            await message.reply(bot_response)
        else:
            await message.reply("Lo siento, no puedo generar una respuesta en este momento.")

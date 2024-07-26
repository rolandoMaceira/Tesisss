# bot.py
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import handle_message

# Crea un cliente Pyrogram
client = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define el manejador de mensajes
client.add_handler(MessageHandler(handle_message, filters.text))

# Inicia el bot
client.run()

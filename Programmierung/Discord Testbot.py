# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)

###https://realpython.com/how-to-make-a-discord-bot-python/ 
###https://semicolon.dev/python/how-to-fix-modulenotfounderror-no-module-named 

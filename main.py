import os

import discord
from dotenv import load_dotenv
from spore_bot import SporeBot

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True  # ← THIS is the key fix

bot = SporeBot(intents=intents)

token = os.getenv("DISCORD_TOKEN")
print(f"Token loaded: {token}")
bot.run(token)
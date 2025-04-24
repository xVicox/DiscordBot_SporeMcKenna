import discord

class SporeBot(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f"{self.user} has sprouted in the mycelial network! 🍄")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if "mushroom" in message.content.lower():
            await message.channel.send("🍄 *The spores are listening...*")

import random
import re
import discord
import json

class SporeBot(discord.Client):
    """
    A Discord bot that responds to mushroom-related keywords with facts and quotes.

    The bot uses a JSON file (responses.json) containing categorized responses that are
    triggered when users message contains specific keywords.
    """

    def __init__(self, *, intents: discord.Intents):
        """Initializes the SporeBot client and loads response data. """

        super().__init__(intents=intents)

        # Loading the responses.json into a dictionary
        with open('responses.json', 'r') as file:
            self._json_responses = json.load(file)

    async def on_ready(self):
        """Callback when the bot successfully connects to Discord."""

        print(f"{self.user} has sprouted in the mycelial network! 🍄")

    async def on_message(self, message):
        """Processes incoming messages and sends responses when keywords are detected.

        Args:
            message (discord.Message): The message object received from Discord.

            Behavior:
            1. Ignores messages from self to prevent loops
            2. Handles /help command
            3. Normalizes message content (lowercase, removes punctuation)
            4. Checks each word against keyword lists in responses.json
            5. For magic_mushrooms category, randomly selects between facts/quotes
            6. Sends a random response from the matched category
        """

        # Bot will not respond to its own messages
        if message.author == self.user:
            return

        # Preparing the user messages for processing
        message_content = message.content.lower()
        # Using regular expressions to handle special characters in messages
        message_words = re.sub(r"[^\w\s]", "", message_content).split()

        # Handling /help command
        if message.content == "/help":
            help_list = self._json_responses["commands"]["/help"]
            formatted_help = "\n".join(help_list)

            embed = discord.Embed(
                title="📘 Help Menu",
                description = formatted_help,
                color = discord.Color.blue()
            )

            await message.channel.send(embed=embed)
            return

        # Picking the random response
        for word in message_words:
            for category, category_data in self._json_responses.items():
                if word in category_data["keywords"]:
                    if category == "magic_mushrooms":
                        response_type = random.choice(["facts", "quotes"])
                        response = random.choice(category_data[response_type])
                    else:
                        response = random.choice(category_data["facts"])

                    await message.channel.send(f"{response}")
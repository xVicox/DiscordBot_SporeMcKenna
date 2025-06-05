import os
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
        self._user_id = None

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
            3. Handles /pic command
            4. Handles /mute & /unmute commands
            5. Normalizes message content (lowercase, removes punctuation)
            6. Checks each word against keyword lists in responses.json
            7. For magic_mushrooms category, randomly selects between facts/quotes
            8. Sends a random response from the matched category
        """

        # Catching user data on every post
        self._user_id = message.author.id
        user_username = message.author
        print(f"Author: {user_username} : ID: {self._user_id}")

        # Bot will not respond to its own messages
        if message.author == self.user:
            return

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

        # Muting the bot for the user
        if message.content == "/mute":
            if SporeBot.mute_user(self._user_id):
                await message.channel.send("🔇 Spore McKenna is now muted.")

        # Unmuting the bot
        if message.content == "/unmute":
            if not SporeBot.is_user_muted(self._user_id):
                await message.channel.send("👂 Spore McKenna is listening to you.")
            if SporeBot.unmute_user(self._user_id):
                await message.channel.send("🔊 Spore McKenna is unmuted.")

        if SporeBot.is_user_muted(self._user_id):
            return

        # Handling image responses aka. /pic command, bot picks a random picture from the gallery and posts it
        if message.content == "/pic":
            folder_path = "resources/pics"
            # List only .jpg files
            image_files = [file for file in os.listdir(folder_path)
                           if (file.lower().endswith(".jpg")
                               or file.lower().endswith(".jpeg"))]

            if image_files:
                chosen_img = random.choice(image_files)
                latin_name_only, extension = os.path.splitext(chosen_img)
                img_path = os.path.join(folder_path, chosen_img)
                file = discord.File(img_path, filename=chosen_img)
                info_text = self._json_responses["gallery"][latin_name_only]
                embed = discord.Embed(
                    title=f"🍄 Random mushroom: *{latin_name_only}*",
                    description=info_text,
                    color=discord.Color.dark_green()
                )
                embed.set_image(url=f"attachment://{chosen_img}")
                await message.channel.send(embed=embed, file=file)

            else:
                await message.channel.send("No images found in the gallery.")
            return

        # Handles textual responses
        else:
            # Preparing the user messages for processing
            message_content = message.content.lower()
            # Using regular expressions to handle special characters in messages
            message_words = re.sub(r"[^\w\s]", "", message_content).split()
            # Picking the random response
            for word in message_words:
                for category, category_data in self._json_responses.items():
                    # checks for "keywords" key in the responses.json dictionary
                    keywords = category_data.get("keywords")
                    if keywords and word in keywords:
                        if category == "magic_mushrooms":
                            response_type = random.choice(["facts", "quotes"])
                            response = random.choice(category_data[response_type])
                        else:
                            response = random.choice(category_data["facts"])
                        await message.channel.send(f"{response}")
                        return

    @staticmethod
    def is_user_muted(user_id):
        """
        Checks if a user is muted by looking up their user ID in a text file.

        Args:
            user_id (int or str): The Discord user ID to check.

        Returns:
            bool: True if the user is muted (i.e., their ID is in the file),
                  False otherwise or if the file does not exist.
        """
        try:
            with open("resources/muted_users.txt", "r", encoding="UTF-8") as file:
                for line in file:
                    if str(user_id) == line.strip():
                        return True # User is already muted
            return False
        except FileNotFoundError:
            return False

    @staticmethod
    def mute_user(user_id):
        """
            Adds a user's ID to the muted users list if they are not already muted.

            Args:
                user_id (int or str): The Discord user ID to mute.

            Returns:
                bool: True if the user was successfully muted,
                      False if the user was already muted or if an error occurred.
            """
        try:
            if SporeBot.is_user_muted(user_id):
                return False # User is already muted
            else:
                with open("resources/muted_users.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{user_id}\n")
                return True
        except FileNotFoundError:
            return False

    @staticmethod
    def unmute_user(user_id):
        """
            Removes a user's ID from the muted users list if they are currently muted.

            Args:
                user_id (int or str): The Discord user ID to unmute.

            Returns:
                bool: True if the user was successfully unmuted,
                      False if the user was not muted or if an error occurred.
            """
        try:
            if SporeBot.is_user_muted(user_id):
                with open ("resources/muted_users.txt", "r", encoding="UTF-8") as file:
                    lines = file.readlines()
                with open("resources/muted_users.txt", "w", encoding="UTF-8") as file:
                    for line in lines:
                        if line.strip() != str(user_id):
                            file.write(line)
                return True
            else: return False
        except FileNotFoundError:
            return False
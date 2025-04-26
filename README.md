# 🍄 SporeBot

A Discord bot that responds to mushroom-related terms with educational facts and psychedelic quotes. Perfect for mycology enthusiasts and consciousness explorers!

## Features
- **Keyword-triggered responses**: Replies when users mention mushroom-related terms
- **Two response modes**:
  - `educational`: Scientific facts about fungi
  - `magic_mushrooms`: Psychedelic quotes and facts
- **Smart filtering**: Ignores punctuation and bot's own messages

## Setup
1. Install requirements:
   ```bash
   pip install discord.py python-dotenv

2. Add your Discord token to .env:
   ```bash
   DISCORD_TOKEN=your_token_here

4. Run the bot
   ```bash
   python main.py

## Customization
Edit responses.json to add new keywords/responses

Modify on_message in spore_bot.py to change reply logic

## Example interaction
User: Have you heard about psilocybin?
Bot: "Psilocybin is the psychoactive compound found in magic mushrooms."

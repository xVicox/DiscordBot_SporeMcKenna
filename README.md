# 🍄 Spore McKenna Bot

**Spore McKenna** is a Discord bot designed for mushroom lovers. It shares mushroom facts, responds to specific keywords, sends mushroom pictures, and accepts user-submitted photos for review. It also supports user muting and scheduled daily mushroom posts.

---

## 📦 Features

- Responds to mushroom-related keywords with facts or quotes.
- Sends random mushroom images with `/pic` command.
- Accepts user-submitted images using `/submit_pic` and replies in DMs.
- Scheduled "Mushroom of the Day" post at a fixed time.
- Allows users to mute/unmute bot responses.
- Replies directly to messages (quotes them).
- Ignores DMs and only responds in server channels.

---

## ⚙️ Requirements

- Python 3.8+
- `discord.py` library
- A valid Discord bot token

---

## 📁 Project Structure

```
.
├── spore_bot.py
├── responses.json
└── resources/
    ├── pics/
    │   ├── [gallery images]
    │   └── submitted/
    │       └── [user-submitted images]
    └── muted_users.txt
```

---

## 🧠 Bot Commands

| Command         | Description |
|----------------|-------------|
| `/help`         | Displays the help menu using data from `responses.json`. |
| `/pic`          | Sends a random mushroom image from the gallery with info. |
| `/submit_pic`   | Accepts a `.jpg`, `.jpeg`, or `.png` image and saves it. |
| `/mute`         | Mutes the bot for the user (no keyword responses). |
| `/unmute`       | Unmutes the bot for the user. |

---

## 📝 Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install -U discord.py
   ```

2. **Run the bot:**
   In your main script (not shown here), add something like:
   ```python
   intents = discord.Intents.default()
   intents.messages = True
   bot = SporeBot(intents=intents)
   bot.run("YOUR_BOT_TOKEN")
   ```

3. **Prepare required files and folders:**
   - `responses.json`: Contains keyword mappings, quotes, facts, and help text.
   - `resources/pics`: Folder with `.jpg` or `.jpeg` mushroom images.
   - `resources/pics/submitted`: Where user-submitted images will be saved.
   - `resources/muted_users.txt`: Stores muted user IDs.

4. **Configure daily post channel:**
   Replace the channel ID in `on_ready()`:
   ```python
   channel_id = 1379376364435542079
   ```

---

## 🛡️ Notes

- The bot ignores DMs to prevent unintended behavior.
- Users with DMs disabled won’t get confirmation messages for `/submit_pic`.
- Submitted images are saved with the user’s Discord tag as a prefix.
- `responses.json` must match the expected format.

---



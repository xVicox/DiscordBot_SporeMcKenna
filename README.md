# 🍄 SporeBot

**SporeBot** is a Discord bot designed for mushroom lovers, mycologists, and curious psychonauts. It reacts to mushroom-related keywords, shares random educational facts or psychedelic quotes, and now includes a rich gallery experience with daily posts and user submissions.

---

## 🌟 Features

- **Keyword-triggered responses**  
  Replies to mushroom-related terms with:
  - `educational`: Scientific facts about fungi  
  - `magic_mushrooms`: Psychedelic quotes and facts  

- **Smart filtering**  
  Ignores punctuation and messages from other bots.

- **Gallery integration**  
  - `/pic`: Sends a random mushroom image with info.  
  - **Mushroom of the Day**: Automatically posts one image daily at a specified time.

- **User submission system**  
  - `/submit_pic`: Users can submit their own mushroom photos.  
  - Images are not posted publicly—submissions are acknowledged via DM and reviewed manually.

---

## 🔧 Setup

1. **Install requirements:**
   ```bash
   pip install discord.py python-dotenv

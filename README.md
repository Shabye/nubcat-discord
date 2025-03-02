# NubCat Discord Bot
Discord Bot to handle different Maplestory 1 data and tools

## Setup Instructions

1. Make sure you have Python 3.8 or higher installed
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your Discord bot token:
   ```
   DISCORD_TOKEN=your_bot_token_here
   ```

4. Run the bot:
   ```bash
   python src/bot.py
   ```

## Available Commands
- `!hello` - Get a friendly greeting from the bot
- `!ping` - Check the bot's latency

## Development
To get started with development:
1. Create a new Discord application and bot at [Discord Developer Portal](https://discord.com/developers/applications)
2. Get your bot token and add it to the `.env` file
3. Invite the bot to your server using the OAuth2 URL generator in the Developer Portal

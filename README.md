# NubCat Discord Bot
Discord Bot to handle different Maplestory 1 data and tools

![Version](https://img.shields.io/badge/version-1.2.0-blue.svg)

## Features
- HEXA Matrix progression tracking and calculations
- Boss information and blue dot requirements
- Discord timestamp generation
- Interactive command responses with buttons

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

### HEXA Matrix Commands
- `/hexaprogress` - Track progress of all HEXA Matrix nodes with interactive category views
  - Shows Origin, Mastery, Enhancement, and Common skill progress
  - Includes time to max calculations and daily fragment goals
  - Features color-coded progress bars (green for completed nodes)
- `/hexalevel [level]` - Look up HEXA Matrix level requirements
- `/progress [category] [level]` - Calculate remaining fragments for a specific category

### Boss Information
- `/bluedot [boss]` - Get boss information including:
  - 5% blue dot damage requirement
  - Total boss HP
  - Level and AF/SaC requirements
  - Green safe phase timing (if applicable)

### Utility Commands
- `/time [options]` - Generate Discord timestamps in various formats
- `/ping` - Check the bot's latency

## Development
To get started with development:
1. Create a new Discord application and bot at [Discord Developer Portal](https://discord.com/developers/applications)
2. Get your bot token and add it to the `.env` file
3. Invite the bot to your server using the OAuth2 URL generator in the Developer Portal

## Recent Updates
- Added green progress bars for completed nodes (100%)
- Renamed VI Skills category to Origin
- Added time to max calculations with various daily fragment rates
- Improved progress visualization with interactive category buttons

## Changelog

### [1.2.0] - 2024-03-02
- Added green progress bars for 100% completion
- Renamed VI Skills to Origin throughout the bot
- Added time to max calculations with daily rates (12/35/60/100)
- Enhanced progress visualization with interactive category buttons

### [1.1.0] - 2024-03-02
- Added green safe phase information to boss data
- Enhanced bluedot command with phase information
- Improved number formatting to include quadrillion (Q)

### [1.0.0] - 2024-03-02
- Initial release
- HEXA Matrix progression tracking
- Boss information and blue dot requirements
- Discord timestamp generation
- Basic utility commands

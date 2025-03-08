# NubCat Discord Bot
Discord Bot to handle different Maplestory 1 data and tools

![Version](https://img.shields.io/badge/version-1.2.4-blue.svg)

## Features
- HEXA Matrix progression tracking and calculations
- Boss crystal price calculations
- Utility commands
- Random meow responses to rotating target users

### HEXA Matrix Commands
- `/hexaprogress [origin] [mastery1] [mastery2] [enhance1] [enhance2] [enhance3] [enhance4] [common]` - Calculate fragment requirements for all skill nodes
- `/progress [category] [level] [target_level]` - Calculate remaining fragment requirements and show progress for a specific category

### Boss Commands
- `/bluedot [boss]` - Show boss crystal price for current week

### Utility Commands
- `/time [options]` - Generate Discord timestamps in various formats
- `/roll` - Roll a random number between 1-100
- `/ping` - Check the bot's latency
- `/inhouse` - Create an ARAM custom game lobby

### Fun Features
- Random meow responses to a randomly selected user (changes every 2 hours)

## Development
To get started with development:
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your Discord bot token
4. Run the bot: `python src/bot.py`

## Changelog

### [1.2.4] - 2024-03-07
- Added rotating target user system for meow responses
- Target user changes randomly every 2 hours
- Only selects from non-bot users in the server

### [1.2.3] - 2024-03-06
- Added `/inhouse` command for League of Legends ARAM custom games

### [1.2.1] - 2024-03-02
- Added `/roll` command for generating random numbers between 1-100

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

import os
import discord
import random
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from data.hexa_progression import HEXA_PROGRESSION

# Load environment variables
load_dotenv()

# Bot setup with all intents
intents = discord.Intents.all()  # Enable all intents
bot = commands.Bot(command_prefix='!', intents=intents)

# List of varied meow responses
MEOW_RESPONSES = [
    "meow 🐱",
    "mrrrow! 😺",
    "meeeeeow 😸",
    "purrrr 😽",
    "*stretches* meoooow 🐈",
    "mew! 😺",
    "nyaa~ 🐱",
    "*rolls over* meow! 😸",
    "*tilts head* mrrp? 😺",
    "meow meow! 🐈",
    "*blinks slowly* meeeow 😽",
    "*paws at you* mrow! 🐱",
    "purrrrrrr... meow! 😺",
    "*wiggles tail* meow! 🐈",
    "miau! 😸"
]

# Boss data for blue dot calculations
BOSS_DATA = {
    "normal_lotus": {
        "name": "Normal Lotus",
        "level": 210,
        "af": 0,
        "hp": 1500000000000,  # 1.5T
        "green_safe": "P2 33%"
    },
    "normal_damien": {
        "name": "Normal Damien",
        "level": 210,
        "af": 0,
        "hp": 5000000000000,  # 5T
        "green_safe": "50%"
    },
    "normal_slime": {
        "name": "Normal Slime",
        "level": 220,
        "af": 0,
        "hp": 1200000000000  # 1.2T
    },
    "easy_lucid": {
        "name": "Easy Lucid",
        "level": 230,
        "af": 360,
        "hp": 12000000000000,  # 12T
        "green_safe": "P2 100%"
    },
    "easy_will": {
        "name": "Easy Will",
        "level": 235,
        "af": 560,
        "hp": 13000000000000,  # 13T
        "green_safe": "P2 33%"
    },
    "normal_lucid": {
        "name": "Normal Lucid",
        "level": 230,
        "af": 760,
        "hp": 24000000000000,  # 24T
        "green_safe": "P2 100%"
    },
    "normal_will": {
        "name": "Normal Will",
        "level": 250,
        "af": 760,
        "hp": 25000000000000,  # 25T
        "green_safe": "P2 33%"
    },
    "normal_gloom": {
        "name": "Normal Gloom",
        "level": 255,
        "af": 730,
        "hp": 26000000000000,  # 26T
        "green_safe": "50%"
    },
    "normal_darknell": {
        "name": "Normal Darknell",
        "level": 265,
        "af": 850,
        "hp": 30000000000000,  # 30T
        "green_safe": "50%"
    },
    "hard_lotus": {
        "name": "Hard Lotus",
        "level": 230,
        "af": 0,
        "hp": 33000000000000,  # 33T
        "green_safe": "P2 33%"
    },
    "hard_damien": {
        "name": "Hard Damien",
        "level": 210,
        "af": 0,
        "hp": 36000000000000,  # 36T
        "green_safe": "50%"
    },
    "hard_lucid": {
        "name": "Hard Lucid",
        "level": 230,
        "af": 360,
        "hp": 118000000000000,  # 118T
        "green_safe": "P2 84%"
    },
    "hard_will": {
        "name": "Hard Will",
        "level": 250,
        "af": 760,
        "hp": 126000000000000,  # 126T
        "green_safe": "P2 33%"
    },
    "normal_vhilla": {
        "name": "Normal Von Hilla",
        "level": 250,
        "af": 900,
        "hp": 88000000000000,  # 88T
        "green_safe": "50%"
    },
    "chaos_slime": {
        "name": "Chaos Slime",
        "level": 250,
        "af": 0,
        "hp": 90000000000000  # 90T
    },
    "chaos_gloom": {
        "name": "Chaos Gloom",
        "level": 255,
        "af": 730,
        "hp": 126000000000000,  # 126T
        "green_safe": "50%"
    },
    "hard_darknell": {
        "name": "Hard Darknell",
        "level": 265,
        "af": 850,
        "hp": 130000000000000,  # 130T
        "green_safe": "50%"
    },
    "hard_vhilla": {
        "name": "Hard Von Hilla",
        "level": 250,
        "af": 900,
        "hp": 176000000000000,  # 176T
        "green_safe": "50%"
    },
    "black_mage": {
        "name": "Black Mage",
        "level": 275,
        "af": 1320,
        "hp": 470000000000000,  # 470T
        "green_safe": "P3 63%"
    },
    "normal_seren": {
        "name": "Normal Seren",
        "level": 270,
        "af": 200,
        "hp": 208000000000000,  # 208T
        "green_safe": "P2 80%"
    },
    "hard_seren": {
        "name": "Hard Seren",
        "level": 275,
        "af": 200,
        "hp": 484000000000000,  # 484T
        "green_safe": "P2 67%"
    },
    "easy_kalos": {
        "name": "Easy Kalos",
        "level": 270,
        "af": 200,
        "hp": 357000000000000,  # 357T
        "green_safe": "P2 68%"
    },
    "easy_kaling": {
        "name": "Easy Kaling",
        "level": 275,
        "af": 230,
        "hp": 921000000000000,  # 921T
        "green_safe": "P3 87%"
    },
    "normal_kalos": {
        "name": "Normal Kalos",
        "level": 280,
        "af": 300,
        "hp": 1000000000000000,  # 1Q
        "green_safe": "P2 73%"
    },
    "extreme_lotus": {
        "name": "Extreme Lotus",
        "level": 285,
        "af": 0,
        "hp": 1800000000000000,  # 1.8Q
        "green_safe": "P2 33%"
    },
    "normal_kaling": {
        "name": "Normal Kaling",
        "level": 285,
        "af": 330,
        "hp": 4000000000000000,  # 4Q
        "green_safe": "P3 88%"
    },
    "extreme_black_mage": {
        "name": "Extreme Black Mage",
        "level": 285,
        "af": 1320,
        "hp": 4800000000000000,  # 4.8Q
        "green_safe": "P3 63%"
    },
    "chaos_kalos": {
        "name": "Chaos Kalos",
        "level": 285,
        "af": 330,
        "hp": 6000000000000000,  # 6Q
        "green_safe": "P2 63%"
    },
    "normal_limbo": {
        "name": "Normal Limbo",
        "level": 285,
        "af": 500,
        "hp": 6500000000000000  # 6.5Q
    },
    "extreme_seren": {
        "name": "Extreme Seren",
        "level": 285,
        "af": 200,
        "hp": 8000000000000000,  # 8Q
        "green_safe": "P2 37%"
    },
    "hard_limbo": {
        "name": "Hard Limbo",
        "level": 285,
        "af": 500,
        "hp": 14000000000000000  # 14Q
    },
    "hard_kaling": {
        "name": "Hard Kaling",
        "level": 285,
        "af": 350,
        "hp": 14000000000000000,  # 14Q
        "green_safe": "P3 76%"
    },
    "extreme_kalos": {
        "name": "Extreme Kalos",
        "level": 285,
        "af": 470,
        "hp": 24300000000000000,  # 24.3Q
        "green_safe": "P2 69%"
    }
}

def format_number(number):
    """Format large numbers into readable format with Q/T/B/M"""
    if number >= 1000000000000000:  # Quadrillion
        return f"{number/1000000000000000:.1f}Q"
    elif number >= 1000000000000:  # Trillion
        return f"{number/1000000000000:.1f}T"
    elif number >= 1000000000:  # Billion
        return f"{number/1000000000:.1f}B"
    elif number >= 1000000:  # Million
        return f"{number/1000000:.1f}M"
    else:
        return f"{number:,}"

@bot.event
async def on_ready():
    print('----------------------------------------')
    print(f'Bot Instance Started')
    print(f'Bot is ready! Logged in as {bot.user}')
    print(f'Bot ID: {bot.user.id}')
    print(f'Bot is in {len(bot.guilds)} servers')
    for guild in bot.guilds:
        print(f'- {guild.name} (id: {guild.id})')
    print('Syncing slash commands...')
    await bot.tree.sync()
    print('Slash commands synced!')
    print('----------------------------------------')

@bot.tree.command(name="ping", description="Check the bot's latency")
async def ping(interaction: discord.Interaction):
    """Check the bot's latency"""
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f'🏓 Pong! Latency is {latency}ms')

@bot.tree.command(name="roll", description="Roll a random number between 1-100")
async def roll(interaction: discord.Interaction):
    """Generate a random number between 1 and 100"""
    result = random.randint(1, 100)
    await interaction.response.send_message(f'🎲 You rolled: **{result}**')

@bot.tree.command(name="hexalevel", description="Look up HEXA Matrix level progression information")
async def hexalevel(interaction: discord.Interaction, level: int):
    """Look up information about HEXA Matrix level requirements"""
    if level < 0 or level > 30:
        await interaction.response.send_message("Level must be between 0 and 30!", ephemeral=True)
        return
        
    data = HEXA_PROGRESSION[level]
    
    embed = discord.Embed(
        title=f"HEXA Matrix Level {level} Requirements",
        color=0x00ff00
    )
    
    # VI Skills
    embed.add_field(
        name="Origin",
        value=f"Sol Erda: {data.vi_sol_erda}\nFragments: {data.vi_fragments}\nTotal Erda: {data.vi_erda_total}\nTotal Fragments: {data.vi_frag_total}",
        inline=False
    )
    
    # Mastery
    embed.add_field(
        name="Mastery",
        value=f"Sol Erda: {data.mastery_sol_erda}\nFragments: {data.mastery_fragments}\nTotal Erda: {data.mastery_erda_total}\nTotal Fragments: {data.mastery_frag_total}",
        inline=True
    )
    
    # Enhancement
    embed.add_field(
        name="Enhancement",
        value=f"Sol Erda: {data.enhance_sol_erda}\nFragments: {data.enhance_fragments}\nTotal Erda: {data.enhance_erda_total}\nTotal Fragments: {data.enhance_frag_total}",
        inline=True
    )
    
    # Common
    embed.add_field(
        name="Common",
        value=f"Sol Erda: {data.common_sol_erda}\nFragments: {data.common_fragments}\nTotal Erda: {data.common_erda_total}\nTotal Fragments: {data.common_frag_total}",
        inline=True
    )
    
    await interaction.response.send_message(embed=embed)

def create_progress_bar(current, maximum, length=20):
    """Creates a visual progress bar with emojis and detailed percentage"""
    filled = int((current / maximum) * length)
    percentage = (current / maximum) * 100
    
    # Use green squares if progress is 100%, blue squares otherwise
    fill_emoji = "🟩" if percentage >= 100 else "🟦"
    bar = fill_emoji * filled + "⬜" * (length - filled)
    
    return f"{bar}\n`{percentage:.2f}%` ({current:,}/{maximum:,})"

@bot.tree.command(name="progress", description="Calculate remaining fragment requirements and show progress for a specific category")
@app_commands.choices(category=[
    app_commands.Choice(name="Origin", value="vi"),
    app_commands.Choice(name="Mastery", value="mastery"),
    app_commands.Choice(name="Enhancement", value="enhance"),
    app_commands.Choice(name="Common", value="common")
])
async def progress(interaction: discord.Interaction, category: str, current_level: int):
    """Calculate remaining fragment requirements and show progress for HEXA Matrix categories"""
    if current_level < 0 or current_level > 30:
        await interaction.response.send_message("Level must be between 0 and 30!", ephemeral=True)
        return

    # Get max level (30) data
    max_data = HEXA_PROGRESSION[30]
    current_data = HEXA_PROGRESSION[current_level]
    
    # Map category to attribute prefixes and colors
    category_map = {
        "vi": ("Origin", "vi", 0x3498db),  # Blue
        "mastery": ("Mastery", "mastery", 0xe74c3c),  # Red
        "enhance": ("Enhancement", "enhance", 0x2ecc71),  # Green
        "common": ("Common", "common", 0xf1c40f)  # Yellow
    }
    
    display_name, prefix, color = category_map[category]
    
    # Get current and max values for fragments only
    current_frags = getattr(current_data, f"{prefix}_frag_total")
    max_frags = getattr(max_data, f"{prefix}_frag_total")
    
    # Calculate remaining and daily estimates for 6 months and 1 year
    remaining_frags = max_frags - current_frags
    daily_frags_6month = round(remaining_frags / 180, 1) if remaining_frags > 0 else 0  # 180 days
    daily_frags_1year = round(remaining_frags / 365, 1) if remaining_frags > 0 else 0   # 365 days
    
    # Create embed with category-specific color
    embed = discord.Embed(
        title=f"{display_name} Progress | Level {current_level} → 30",
        color=color
    )
    
    # Add fragments progress bar
    embed.add_field(
        name="💎 Fragments Progress",
        value=create_progress_bar(current_frags, max_frags),
        inline=False
    )
    
    # Add detailed requirements
    embed.add_field(
        name="📊 Detailed Requirements",
        value=f"**Remaining Fragments:** {remaining_frags:,}\n"
              f"**Daily Fragments (6-month goal):** {daily_frags_6month:,}/day\n"
              f"**Daily Fragments (1-year goal):** {daily_frags_1year:,}/day",
        inline=False
    )
    
    # Add next level requirements if not max level
    if current_level < 30:
        next_data = HEXA_PROGRESSION[current_level + 1]
        next_frags = getattr(next_data, f"{prefix}_fragments")
        
        embed.add_field(
            name="⏭️ Next Level Requirements",
            value=f"**Fragments:** {next_frags:,}",
            inline=False
        )
    
    # Add milestone levels info
    milestones = [10, 20, 30]
    milestone_info = []
    for milestone in milestones:
        if current_level < milestone:
            milestone_data = HEXA_PROGRESSION[milestone]
            frags_needed = getattr(milestone_data, f"{prefix}_frag_total") - current_frags
            milestone_info.append(f"**Level {milestone}:**\n"
                                f"Need {frags_needed:,} Fragments")
    
    if milestone_info:
        embed.add_field(
            name="🎯 Milestone Goals",
            value="\n\n".join(milestone_info),
            inline=False
        )
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(
    name="hexaprogress",
    description="Calculate HEXA Matrix fragment requirements for all skill nodes"
)
async def hexaprogress(
    interaction: discord.Interaction,
    origin: int,
    mastery1: int,
    mastery2: int,
    enhance1: int,
    enhance2: int,
    enhance3: int,
    enhance4: int,
    common: int
):
    """Calculate fragment requirements for all HEXA Matrix skill nodes"""
    # Validate all levels
    for level in [origin, mastery1, mastery2, enhance1, enhance2, enhance3, enhance4, common]:
        if level < 0 or level > 30:
            await interaction.response.send_message(f"All levels must be between 0 and 30!", ephemeral=True)
            return

    max_data = HEXA_PROGRESSION[30]
    
    # Store all the data needed for different views
    class HexaView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=180)  # 3 minute timeout
            self.value = None

        @discord.ui.button(label="Summary", style=discord.ButtonStyle.primary, emoji="📊")
        async def summary(self, interaction: discord.Interaction, button: discord.ui.Button):
            # Calculate total fragments needed
            vi_current = HEXA_PROGRESSION[origin]
            vi_remaining_frags = max_data.vi_frag_total - vi_current.vi_frag_total
            
            mastery_total_remaining = sum(
                max_data.mastery_frag_total - HEXA_PROGRESSION[level].mastery_frag_total
                for level in [mastery1, mastery2]
            )
            
            enhance_total_remaining = sum(
                max_data.enhance_frag_total - HEXA_PROGRESSION[level].enhance_frag_total
                for level in [enhance1, enhance2, enhance3, enhance4]
            )
            
            common_current = HEXA_PROGRESSION[common]
            common_remaining_frags = max_data.common_frag_total - common_current.common_frag_total
            
            total_remaining_frags = (vi_remaining_frags + 
                                   mastery_total_remaining +
                                   enhance_total_remaining +
                                   common_remaining_frags)

            # Calculate total fragments used and total possible fragments
            total_used = (vi_current.vi_frag_total +
                         sum(HEXA_PROGRESSION[level].mastery_frag_total for level in [mastery1, mastery2]) +
                         sum(HEXA_PROGRESSION[level].enhance_frag_total for level in [enhance1, enhance2, enhance3, enhance4]) +
                         common_current.common_frag_total)
            
            total_possible = (max_data.vi_frag_total +
                            max_data.mastery_frag_total * 2 +
                            max_data.enhance_frag_total * 4 +
                            max_data.common_frag_total)
            
            embed = discord.Embed(
                title="HEXA Matrix Progress - Summary",
                color=0x3498db
            )
            
            embed.add_field(
                name="📊 Overall Progress",
                value=f"**Total Progress:**\n{create_progress_bar(total_used, total_possible)}\n\n"
                      f"**Total Fragments Used:** {total_used:,}\n"
                      f"**Total Fragments Remaining:** {total_remaining_frags:,}\n",
                inline=False
            )
            
            embed.add_field(
                name="📈 Daily Goals",
                value=f"**Daily Fragments (6-month goal):** {round(total_remaining_frags/180):,}/day\n"
                      f"**Daily Fragments (1-year goal):** {round(total_remaining_frags/365):,}/day\n",
                inline=False
            )
            
            embed.add_field(
                name="⏳ Time to Max",
                value=f"**At 12/day (Daily):** {round(total_remaining_frags/12):,} days\n"
                      f"**At 35/day:** {round(total_remaining_frags/35):,} days\n"
                      f"**At 60/day:** {round(total_remaining_frags/60):,} days\n"
                      f"**At 100/day:** {round(total_remaining_frags/100):,} days\n",
                inline=False
            )
            
            embed.add_field(
                name="📋 Category Breakdown",
                value=f"**Origin:** {vi_remaining_frags:,} remaining\n"
                      f"**Mastery:** {mastery_total_remaining:,} remaining\n"
                      f"**Enhancement:** {enhance_total_remaining:,} remaining\n"
                      f"**Common:** {common_remaining_frags:,} remaining\n",
                inline=False
            )
            
            await interaction.response.edit_message(embed=embed, view=self)

        @discord.ui.button(label="Origin", style=discord.ButtonStyle.primary, emoji="🔷")
        async def origins(self, interaction: discord.Interaction, button: discord.ui.Button):
            vi_current = HEXA_PROGRESSION[origin]
            vi_remaining_frags = max_data.vi_frag_total - vi_current.vi_frag_total
            
            embed = discord.Embed(
                title="HEXA Matrix Progress - Origin",
                color=0x3498db
            )
            
            embed.add_field(
                name=f"🔷 Origin (Level {origin})",
                value=f"**Progress to Max:**\n{create_progress_bar(vi_current.vi_frag_total, max_data.vi_frag_total)}\n"
                      f"Remaining: {vi_remaining_frags:,} Fragments",
                inline=False
            )
            
            await interaction.response.edit_message(embed=embed, view=self)

        @discord.ui.button(label="Mastery", style=discord.ButtonStyle.danger, emoji="🔸")
        async def mastery(self, interaction: discord.Interaction, button: discord.ui.Button):
            embed = discord.Embed(
                title="HEXA Matrix Progress - Mastery",
                color=0xe74c3c
            )
            
            mastery_data = [
                ("🔸 Mastery 1", mastery1),
                ("🔸 Mastery 2", mastery2)
            ]
            
            mastery_total_remaining = 0
            for name, level in mastery_data:
                current = HEXA_PROGRESSION[level]
                remaining_frags = max_data.mastery_frag_total - current.mastery_frag_total
                mastery_total_remaining += remaining_frags
                
                embed.add_field(
                    name=f"{name} (Level {level})",
                    value=f"**Progress to Max:**\n{create_progress_bar(current.mastery_frag_total, max_data.mastery_frag_total)}\n"
                          f"Remaining: {remaining_frags:,} Fragments",
                    inline=False
                )
            
            embed.add_field(
                name="Total Remaining",
                value=f"Total Mastery Fragments Remaining: {mastery_total_remaining:,}",
                inline=False
            )
            
            await interaction.response.edit_message(embed=embed, view=self)

        @discord.ui.button(label="Enhancement", style=discord.ButtonStyle.success, emoji="💠")
        async def enhancement(self, interaction: discord.Interaction, button: discord.ui.Button):
            embed = discord.Embed(
                title="HEXA Matrix Progress - Enhancement",
                color=0x2ecc71
            )
            
            enhance_data = [
                ("💠 Enhancement 1", enhance1),
                ("💠 Enhancement 2", enhance2),
                ("💠 Enhancement 3", enhance3),
                ("💠 Enhancement 4", enhance4)
            ]
            
            enhance_total_remaining = 0
            for name, level in enhance_data:
                current = HEXA_PROGRESSION[level]
                remaining_frags = max_data.enhance_frag_total - current.enhance_frag_total
                enhance_total_remaining += remaining_frags
                
                embed.add_field(
                    name=f"{name} (Level {level})",
                    value=f"**Progress to Max:**\n{create_progress_bar(current.enhance_frag_total, max_data.enhance_frag_total)}\n"
                          f"Remaining: {remaining_frags:,} Fragments",
                    inline=False
                )
            
            embed.add_field(
                name="Total Remaining",
                value=f"Total Enhancement Fragments Remaining: {enhance_total_remaining:,}",
                inline=False
            )
            
            await interaction.response.edit_message(embed=embed, view=self)

        @discord.ui.button(label="Common", style=discord.ButtonStyle.secondary, emoji="💎")
        async def common(self, interaction: discord.Interaction, button: discord.ui.Button):
            common_current = HEXA_PROGRESSION[common]
            common_remaining_frags = max_data.common_frag_total - common_current.common_frag_total
            
            embed = discord.Embed(
                title="HEXA Matrix Progress - Common",
                color=0xf1c40f
            )
            
            embed.add_field(
                name=f"💎 Common Skills (Level {common})",
                value=f"**Progress to Max:**\n{create_progress_bar(common_current.common_frag_total, max_data.common_frag_total)}\n"
                      f"Remaining: {common_remaining_frags:,} Fragments",
                inline=False
            )
            
            await interaction.response.edit_message(embed=embed, view=self)

    # Calculate initial summary view data
    vi_current = HEXA_PROGRESSION[origin]
    vi_remaining_frags = max_data.vi_frag_total - vi_current.vi_frag_total
    
    mastery_total_remaining = sum(
        max_data.mastery_frag_total - HEXA_PROGRESSION[level].mastery_frag_total
        for level in [mastery1, mastery2]
    )
    
    enhance_total_remaining = sum(
        max_data.enhance_frag_total - HEXA_PROGRESSION[level].enhance_frag_total
        for level in [enhance1, enhance2, enhance3, enhance4]
    )
    
    common_current = HEXA_PROGRESSION[common]
    common_remaining_frags = max_data.common_frag_total - common_current.common_frag_total
    
    total_remaining_frags = (vi_remaining_frags + 
                           mastery_total_remaining +
                           enhance_total_remaining +
                           common_remaining_frags)

    # Calculate total fragments used and total possible fragments
    total_used = (vi_current.vi_frag_total +
                 sum(HEXA_PROGRESSION[level].mastery_frag_total for level in [mastery1, mastery2]) +
                 sum(HEXA_PROGRESSION[level].enhance_frag_total for level in [enhance1, enhance2, enhance3, enhance4]) +
                 common_current.common_frag_total)
    
    total_possible = (max_data.vi_frag_total +
                    max_data.mastery_frag_total * 2 +
                    max_data.enhance_frag_total * 4 +
                    max_data.common_frag_total)

    # Create initial embed with summary view
    initial_embed = discord.Embed(
        title="HEXA Matrix Progress - Summary",
        color=0x3498db
    )
    
    initial_embed.add_field(
        name="📊 Overall Progress",
        value=f"**Total Progress:**\n{create_progress_bar(total_used, total_possible)}\n\n"
              f"**Total Fragments Used:** {total_used:,}\n"
              f"**Total Fragments Remaining:** {total_remaining_frags:,}",
        inline=False
    )
    
    initial_embed.add_field(
        name="📈 Daily Goals",
        value=f"**Daily Fragments (6-month goal):** {round(total_remaining_frags/180):,}/day\n"
              f"**Daily Fragments (1-year goal):** {round(total_remaining_frags/365):,}/day",
        inline=False
    )
    
    initial_embed.add_field(
        name="⏳ Time to Max",
        value=f"**At 12/day (Daily):** {round(total_remaining_frags/12):,} days\n"
              f"**At 35/day:** {round(total_remaining_frags/35):,} days\n"
              f"**At 60/day:** {round(total_remaining_frags/60):,} days\n"
              f"**At 100/day:** {round(total_remaining_frags/100):,} days",
        inline=False
    )
    
    initial_embed.add_field(
        name="📋 Category Breakdown",
        value=f"**Origin:** {vi_remaining_frags:,} remaining\n"
              f"**Mastery:** {mastery_total_remaining:,} remaining\n"
              f"**Enhancement:** {enhance_total_remaining:,} remaining\n"
              f"**Common:** {common_remaining_frags:,} remaining",
        inline=False
    )

    # Send initial message with view
    await interaction.response.send_message(embed=initial_embed, view=HexaView())

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself to prevent loops
    if message.author == bot.user:
        return

    # Check if the message is from the specific user
    if message.author.id == 117641187254337537:
        # Pick a random meow response
        meow = random.choice(MEOW_RESPONSES)
        await message.channel.send(meow)
    
    # Process commands (this is needed to make sure commands still work)
    await bot.process_commands(message)

@bot.tree.command(
    name="time",
    description="Generate Discord timestamps (use without parameters for current time)"
)
@app_commands.choices(style=[
    app_commands.Choice(name="Short Time (HH:mm)", value="t"),
    app_commands.Choice(name="Long Time (HH:mm:ss)", value="T"),
    app_commands.Choice(name="Short Date (DD/MM/YYYY)", value="d"),
    app_commands.Choice(name="Long Date (DD Month YYYY)", value="D"),
    app_commands.Choice(name="Short Date/Time", value="f"),
    app_commands.Choice(name="Long Date/Time", value="F"),
    app_commands.Choice(name="Relative Time", value="R")
])
async def time(
    interaction: discord.Interaction,
    year: int = None,
    month: int = None,
    day: int = None,
    hour: int = None,
    minute: int = None,
    style: str = "f"
):
    """Generate a Discord timestamp for a specific date and time"""
    try:
        # Create datetime and convert to Unix timestamp
        from datetime import datetime
        
        # If any of year, month, or day is None, use current time
        if year is None or month is None or day is None:
            dt = datetime.now()
        else:
            # Use provided date with current time if hour/minute not specified
            current_time = datetime.now()
            hour = hour if hour is not None else current_time.hour
            minute = minute if minute is not None else current_time.minute
            dt = datetime(year, month, day, hour, minute)
            
        timestamp = int(dt.timestamp())
        formatted = f"<t:{timestamp}:{style}>"
        
        # Send just the formatted timestamp
        await interaction.response.send_message(formatted)
        
    except ValueError as e:
        await interaction.response.send_message(
            "❌ Invalid date/time.",
            ephemeral=True
        )

@bot.tree.command(
    name="bluedot",
    description="Get blue dot (5%) damage requirement and level/AF requirements for bosses"
)
@app_commands.choices(boss=[
    app_commands.Choice(name="Hard Lotus", value="hard_lotus"),
    app_commands.Choice(name="Hard Damien", value="hard_damien"),
    app_commands.Choice(name="Hard Lucid", value="hard_lucid"),
    app_commands.Choice(name="Hard Will", value="hard_will"),
    app_commands.Choice(name="Normal Von Hilla", value="normal_vhilla"),
    app_commands.Choice(name="Chaos Slime", value="chaos_slime"),
    app_commands.Choice(name="Chaos Gloom", value="chaos_gloom"),
    app_commands.Choice(name="Hard Darknell", value="hard_darknell"),
    app_commands.Choice(name="Hard Von Hilla", value="hard_vhilla"),
    app_commands.Choice(name="Black Mage", value="black_mage"),
    app_commands.Choice(name="Normal Seren", value="normal_seren"),
    app_commands.Choice(name="Hard Seren", value="hard_seren"),
    app_commands.Choice(name="Easy Kalos", value="easy_kalos"),
    app_commands.Choice(name="Easy Kaling", value="easy_kaling"),
    app_commands.Choice(name="Normal Kalos", value="normal_kalos"),
    app_commands.Choice(name="Extreme Lotus", value="extreme_lotus"),
    app_commands.Choice(name="Normal Kaling", value="normal_kaling"),
    app_commands.Choice(name="Chaos Kalos", value="chaos_kalos"),
    app_commands.Choice(name="Normal Limbo", value="normal_limbo"),
    app_commands.Choice(name="Hard Limbo", value="hard_limbo"),
    app_commands.Choice(name="Hard Kaling", value="hard_kaling"),
])
async def bluedot(interaction: discord.Interaction, boss: str):
    """Get blue dot requirement and requirements for a specific boss"""
    if boss not in BOSS_DATA:
        await interaction.response.send_message("Invalid boss selection.", ephemeral=True)
        return

    boss_info = BOSS_DATA[boss]
    blue_dot_damage = boss_info["hp"] * 0.05  # 5% damage requirement

    embed = discord.Embed(
        title=f"{boss_info['name']} Information",
        color=0x3498db
    )

    embed.add_field(
        name="💙 Blue Dot Requirement (5%)",
        value=f"**Damage Needed:** {format_number(blue_dot_damage)}\n"
              f"**Total Boss HP:** {format_number(boss_info['hp'])}",
        inline=False
    )

    embed.add_field(
        name="📊 Entry Requirements",
        value=f"**Level Requirement:** {boss_info['level']}\n"
              f"**AF/SaC Requirement:** {boss_info['af'] if boss_info['af'] > 0 else 'None'}",
        inline=False
    )

    if "green_safe" in boss_info:
        embed.add_field(
            name="🟢 Green Safe",
            value=f"**at:** {boss_info['green_safe']}",
            inline=False
        )

    await interaction.response.send_message(embed=embed)

# Run the bot
if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN')) 
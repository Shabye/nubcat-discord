import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from data.hexa_progression import HEXA_PROGRESSION

# Load environment variables
load_dotenv()

# Bot setup with all intents
intents = discord.Intents.all()  # Enable all intents
bot = commands.Bot(command_prefix='!', intents=intents)

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
        name="VI Skills",
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
    bar = "🟦" * filled + "⬜" * (length - filled)
    percentage = (current / maximum) * 100
    return f"{bar}\n`{percentage:.2f}%` ({current:,}/{maximum:,})"

@bot.tree.command(name="progress", description="Calculate remaining requirements and show progress for a specific category")
@app_commands.choices(category=[
    app_commands.Choice(name="VI Skills", value="vi"),
    app_commands.Choice(name="Mastery", value="mastery"),
    app_commands.Choice(name="Enhancement", value="enhance"),
    app_commands.Choice(name="Common", value="common")
])
async def progress(interaction: discord.Interaction, category: str, current_level: int):
    """Calculate remaining requirements and show progress for HEXA Matrix categories"""
    if current_level < 0 or current_level > 30:
        await interaction.response.send_message("Level must be between 0 and 30!", ephemeral=True)
        return

    # Get max level (30) data
    max_data = HEXA_PROGRESSION[30]
    current_data = HEXA_PROGRESSION[current_level]
    
    # Map category to attribute prefixes and colors
    category_map = {
        "vi": ("VI Skills", "vi", 0x3498db),  # Blue
        "mastery": ("Mastery", "mastery", 0xe74c3c),  # Red
        "enhance": ("Enhancement", "enhance", 0x2ecc71),  # Green
        "common": ("Common", "common", 0xf1c40f)  # Yellow
    }
    
    display_name, prefix, color = category_map[category]
    
    # Get current and max values
    current_erda = getattr(current_data, f"{prefix}_erda_total")
    current_frags = getattr(current_data, f"{prefix}_frag_total")
    max_erda = getattr(max_data, f"{prefix}_erda_total")
    max_frags = getattr(max_data, f"{prefix}_frag_total")
    
    # Calculate remaining and daily estimates (assuming 1 week to max)
    remaining_erda = max_erda - current_erda
    remaining_frags = max_frags - current_frags
    daily_erda = round(remaining_erda / 7, 1) if remaining_erda > 0 else 0
    daily_frags = round(remaining_frags / 7, 1) if remaining_frags > 0 else 0
    
    # Create embed with category-specific color
    embed = discord.Embed(
        title=f"{display_name} Progress | Level {current_level} → 30",
        color=color
    )
    
    # Add progress bars with more detail
    embed.add_field(
        name="🔹 Sol Erda Progress",
        value=create_progress_bar(current_erda, max_erda),
        inline=False
    )
    
    embed.add_field(
        name="💎 Fragments Progress",
        value=create_progress_bar(current_frags, max_frags),
        inline=False
    )
    
    # Add detailed requirements
    embed.add_field(
        name="📊 Detailed Requirements",
        value=f"**Remaining Sol Erda:** {remaining_erda:,}\n"
              f"**Remaining Fragments:** {remaining_frags:,}\n"
              f"**Daily Sol Erda needed:** {daily_erda:,}/day\n"
              f"**Daily Fragments needed:** {daily_frags:,}/day\n"
              f"*(Based on 7-day completion)*",
        inline=False
    )
    
    # Add next level requirements if not max level
    if current_level < 30:
        next_data = HEXA_PROGRESSION[current_level + 1]
        next_erda = getattr(next_data, f"{prefix}_sol_erda")
        next_frags = getattr(next_data, f"{prefix}_fragments")
        
        embed.add_field(
            name="⏭️ Next Level Requirements",
            value=f"**Sol Erda:** {next_erda:,}\n**Fragments:** {next_frags:,}",
            inline=False
        )
    
    # Add milestone levels info
    milestones = [10, 20, 30]
    milestone_info = []
    for milestone in milestones:
        if current_level < milestone:
            milestone_data = HEXA_PROGRESSION[milestone]
            erda_needed = getattr(milestone_data, f"{prefix}_erda_total") - current_erda
            frags_needed = getattr(milestone_data, f"{prefix}_frag_total") - current_frags
            milestone_info.append(f"**Level {milestone}:**\n"
                                f"Need {erda_needed:,} Sol Erda\n"
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
    description="Calculate HEXA Matrix progress for all skill nodes"
)
async def hexaprogress(
    interaction: discord.Interaction,
    vi_skill: int,
    mastery1: int,
    mastery2: int,
    enhance1: int,
    enhance2: int,
    enhance3: int,
    enhance4: int,
    common: int
):
    """Calculate progress for all HEXA Matrix skill nodes"""
    # Validate all levels
    for level in [vi_skill, mastery1, mastery2, enhance1, enhance2, enhance3, enhance4, common]:
        if level < 0 or level > 30:
            await interaction.response.send_message(f"All levels must be between 0 and 30!", ephemeral=True)
            return

    max_data = HEXA_PROGRESSION[30]
    
    # Create the main embed
    embed = discord.Embed(
        title="HEXA Matrix Progress Overview",
        description="Progress tracking for all skill nodes",
        color=0x3498db
    )

    # VI Skills Progress
    vi_current = HEXA_PROGRESSION[vi_skill]
    vi_remaining_erda = max_data.vi_erda_total - vi_current.vi_erda_total
    vi_remaining_frags = max_data.vi_frag_total - vi_current.vi_frag_total
    
    embed.add_field(
        name="🔷 VI Skills (Level " + str(vi_skill) + ")",
        value=f"**Progress to Max:**\n{create_progress_bar(vi_current.vi_erda_total, max_data.vi_erda_total)}\n"
              f"Remaining: {vi_remaining_erda:,} Sol Erda, {vi_remaining_frags:,} Fragments",
        inline=False
    )

    # Mastery Progress
    mastery_data = [
        ("🔸 Mastery 1", mastery1),
        ("🔸 Mastery 2", mastery2)
    ]
    
    for name, level in mastery_data:
        current = HEXA_PROGRESSION[level]
        remaining_erda = max_data.mastery_erda_total - current.mastery_erda_total
        remaining_frags = max_data.mastery_frag_total - current.mastery_frag_total
        
        embed.add_field(
            name=f"{name} (Level {level})",
            value=f"**Progress to Max:**\n{create_progress_bar(current.mastery_erda_total, max_data.mastery_erda_total)}\n"
                  f"Remaining: {remaining_erda:,} Sol Erda, {remaining_frags:,} Fragments",
            inline=False
        )

    # Enhancement Progress
    enhance_data = [
        ("💠 Enhancement 1", enhance1),
        ("💠 Enhancement 2", enhance2),
        ("💠 Enhancement 3", enhance3),
        ("💠 Enhancement 4", enhance4)
    ]
    
    for name, level in enhance_data:
        current = HEXA_PROGRESSION[level]
        remaining_erda = max_data.enhance_erda_total - current.enhance_erda_total
        remaining_frags = max_data.enhance_frag_total - current.enhance_frag_total
        
        embed.add_field(
            name=f"{name} (Level {level})",
            value=f"**Progress to Max:**\n{create_progress_bar(current.enhance_erda_total, max_data.enhance_erda_total)}\n"
                  f"Remaining: {remaining_erda:,} Sol Erda, {remaining_frags:,} Fragments",
            inline=False
        )

    # Common Progress
    common_current = HEXA_PROGRESSION[common]
    common_remaining_erda = max_data.common_erda_total - common_current.common_erda_total
    common_remaining_frags = max_data.common_frag_total - common_current.common_frag_total
    
    embed.add_field(
        name=f"💎 Common Skills (Level {common})",
        value=f"**Progress to Max:**\n{create_progress_bar(common_current.common_erda_total, max_data.common_erda_total)}\n"
              f"Remaining: {common_remaining_erda:,} Sol Erda, {common_remaining_frags:,} Fragments",
        inline=False
    )

    # Calculate totals
    total_remaining_erda = (vi_remaining_erda + 
                          2 * remaining_erda +  # For 2 mastery nodes
                          4 * remaining_erda +  # For 4 enhancement nodes
                          common_remaining_erda)
    
    total_remaining_frags = (vi_remaining_frags + 
                           2 * remaining_frags +  # For 2 mastery nodes
                           4 * remaining_frags +  # For 4 enhancement nodes
                           common_remaining_frags)

    # Add total requirements
    embed.add_field(
        name="📊 Total Requirements",
        value=f"**Total Remaining:**\n"
              f"Sol Erda: {total_remaining_erda:,}\n"
              f"Fragments: {total_remaining_frags:,}\n\n"
              f"**Daily Requirements (7-day goal):**\n"
              f"Sol Erda per day: {round(total_remaining_erda/7):,}\n"
              f"Fragments per day: {round(total_remaining_frags/7):,}",
        inline=False
    )

    await interaction.response.send_message(embed=embed)

# Run the bot
if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN')) 
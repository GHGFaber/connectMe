import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load environment variables from the specified .env file
dotenv_path = '/Users/rut/Documents/GitHub/connectMe/env'
load_dotenv(dotenv_path)

# Retrieve the token from the environment variable
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up intents
intents = discord.Intents.default()
intents.members = True  # See members of the server
intents.message_content = True  # Read message content
intents.reactions = True  # Track reactions

# Set up bot with command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# In-memory storage for user profiles and reaction data
profiles = {}
reaction_data = {}

# Mapping emojis to their respective categories and values
region_emojis = {'🦁': 'Africa', '🦅': 'The Americas', '🐉': 'Asia', '🏰': 'Europe'}
language_emojis = {'🇬🇧': 'English', '🇺🇸': 'English', '🇮🇳': 'Hindi', '🇪🇸': 'Spanish', '🇲🇽': 'Spanish', '🇨🇳': 'Chinese'}
skill_emojis = {'🌱': 'Beginner', '🌿': 'Intermediate', '🌳': 'Advanced'}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='profile_setup', help='Starts the process of setting up a profile with reactions')
async def profile_setup(ctx):
    profile = {}

    # Ask for Region
    region_msg = await ctx.send("React with your region:\n🦁 - Africa\n🦅 - The Americas\n🐉 - Asia\n🏰 - Europe")
    for emoji in region_emojis:
        await region_msg.add_reaction(emoji)

    # Wait for Region reaction
    def check_region(reaction, user):
        return user == ctx.author and str(reaction.emoji) in region_emojis and reaction.message.id == region_msg.id

    reaction, user = await bot.wait_for('reaction_add', check=check_region)
    profile['Region'] = region_emojis[str(reaction.emoji)]

    # Ask for Language
    language_msg = await ctx.send("React with the language you speak:\n🇬🇧 / 🇺🇸 - English\n🇮🇳 - Hindi\n🇪🇸 / 🇲🇽 - Spanish\n🇨🇳 - Chinese")
    for emoji in language_emojis:
        await language_msg.add_reaction(emoji)

    # Wait for Language reaction
    def check_language(reaction, user):
        return user == ctx.author and str(reaction.emoji) in language_emojis and reaction.message.id == language_msg.id

    reaction, user = await bot.wait_for('reaction_add', check=check_language)
    profile['Language'] = language_emojis[str(reaction.emoji)]

    # Ask for Skill Level
    skill_msg = await ctx.send("React with your skill level:\n🌱 - Beginner\n🌿 - Intermediate\n🌳 - Advanced")
    for emoji in skill_emojis:
        await skill_msg.add_reaction(emoji)

    # Wait for Skill Level reaction
    def check_skill(reaction, user):
        return user == ctx.author and str(reaction.emoji) in skill_emojis and reaction.message.id == skill_msg.id

    reaction, user = await bot.wait_for('reaction_add', check=check_skill)
    profile['Skill Level'] = skill_emojis[str(reaction.emoji)]

    profiles[ctx.author.id] = profile
    await ctx.send("Profile created successfully!")
    print(profiles)

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    message_id = reaction.message.id

    if message_id not in reaction_data:
        return

    emoji = str(reaction.emoji)
    if user.id not in reaction_data[message_id]:
        reaction_data[message_id][user.id] = []

    if emoji not in reaction_data[message_id][user.id]:
        reaction_data[message_id][user.id].append(emoji)

    print(f"User {user.name} reacted with {emoji}")

@bot.event
async def on_reaction_remove(reaction, user):
    if user.bot:
        return

    message_id = reaction.message.id

    if message_id not in reaction_data:
        return

    emoji = str(reaction.emoji)
    if user.id in reaction_data[message_id] and emoji in reaction_data[message_id][user.id]:
        reaction_data[message_id][user.id].remove(emoji)

    print(f"User {user.name} removed reaction {emoji}")
    
bot.run(TOKEN)
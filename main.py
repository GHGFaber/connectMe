import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up intents
intents = discord.Intents.default()
intents.members = True  # See members of the server
intents.message_content = True  # Read message content

# Set up bot with command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# In-memory storage for user profiles and team requests
profiles = {}
team_requests = []

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='make', help='Starts the process of making a profile')
async def make_profile(ctx):
    await ctx.send("Let's create your profile. Please answer the following questions:")

    questions = [
        "What is your name?",
        "Which region are you from?",
        "What is your skill level (beginner/intermediate/advanced)?",
        "What languages do you speak?",
    ]

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    profile = {}
    for question in questions:
        await ctx.send(question)
        msg = await bot.wait_for('message', check=check)
        profile[question] = msg.content

    profiles[ctx.author.id] = profile
    await ctx.send("Profile created successfully!")

@bot.command(name='find', help='Finds a team based on profile and situation-specific info')
async def find_team(ctx):
    await ctx.send("Let's find you a team. Please answer the following questions:")

    questions = [
        "Which game are you looking to play?",
        "How many people do you need in your team?",
    ]

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    team_request = {'user_id': ctx.author.id}
    for question in questions:
        await ctx.send(question)
        msg = await bot.wait_for('message', check=check)
        team_request[question] = msg.content

    team_requests.append(team_request)
    await ctx.send("Team request received. Finding a team for you now...")

    # Here, you can implement the logic to match profiles with team requests
    # For simplicity, this example just prints the current profiles and requests
    print("Profiles:", profiles)
    print("Team Requests:", team_requests)

bot.run(TOKEN)

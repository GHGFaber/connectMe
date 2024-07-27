# bot.py
import os

from dotenv import load_dotenv




import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():



@bot.command(name='profile', help='Starts the process of making a profile')
async def make_profile(ctx):
    """
    Starts the process of making a profile for the user. Guide users on specifc info needed and maybe a self intro.
    Profile info should be something that stays the same. We could set up a questionaire for the user and they answer by reacting. 
    Stuff like language, region, rank, 

    Args:
        ctx: context of the command. Usually the channel 
    """
    await ctx.send("Making profile")


@bot.command(name='find_team')
async def find_team(ctx):
    """
    Uses profile and situation-specific info to find a team. Info we need includes 


    Args:
        ctx: context of the command. Usually the channel 
    """
    await ctx.send("Finding you a team. Hang tight!")



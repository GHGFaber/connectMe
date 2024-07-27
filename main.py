# bot.py
import os
import random
from dotenv import load_dotenv
import requests
import json


import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():


# Begin the process of making a profile for the user. Definitely need language(s). Maybe a self-intro? 
@bot.command(name='profile', help='Starts the process of making a profile')
async def make_profile(ctx):
    await ctx.send("Making profile")

@bot.command(name='find_team')
async def find_team(ctx):
    await ctx.send("Finding you a team. Hang tight!")



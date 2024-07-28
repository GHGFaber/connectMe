from discord.ext import commands
from asyncpg import Pool
import discord 

# The __all__ variable specifies the public symbols that the module exports, 
# and it should be a list or tuple of strings representing the names of the objects to be imported when from module import * is used.
__all__ = (
    "Bot",
)

# Override base class constructor and methods 
class Bot(commands.Bot):
    def __init__(self, db: Pool, **kwargs):
        super().__init__(**kwargs)
        self.db = db
    
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")

    # @bot.command(name='profile', help='Starts the process of making a profile')
    # async def make_profile(ctx):
    #     """
    #     Starts the process of making a profile for the user. Guide users on specifc info needed and maybe a self intro.
    #     Profile info should be something that stays the same. We could set up a questionaire for the user and they answer by reacting. 
    #     Stuff like language, region, rank, 

    #     Args:
    #         ctx: context of the command. Usually the channel 
    #     """


    #     await ctx.send("Making profile")


    # @bot.command(name='find')
    # async def find_team(ctx):
    #     """
    #     Uses profile and situation-specific info to find a team. Info we need includes 
    #     1. which game
    #     2. number of people needed 

    #     Args:
    #         ctx: context of the command. Usually the channel 
    #     """
    #     await ctx.send("Finding you a team. Hang tight!")


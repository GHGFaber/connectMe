from discord.ext import commands
from asyncpg import Pool
import discord 
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
import logging

logging.basicConfig(level=logging.INFO)

# The __all__ variable specifies the public symbols that the module exports, 
# and it should be a list or tuple of strings representing the names of the objects to be imported when from module import * is used.
__all__ = (
    "Bot",
)


# Add your commands by doing self.add_command(self.(name of function defition of command))
# See example below 
# Override base class constructor and methods 
class Bot(commands.Bot):
    def __init__(self, db: Pool, **kwargs):
        super().__init__(**kwargs)
        self.add_command(self.profile)
        self.db = db

    async def __aenter__(self):
        await self.start(TOKEN)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
    
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        try:
            print('Performing setup tasks...')
            logging.info("setup_hook started...")
            # Connect to database
            async with self.db.acquire() as conn:
                logging.info("db_connected")
                with open("sql/schemas.sql", 'r') as sql:
                    logging.info("reading sql")
                    await conn.execute(sql.read())
                    logging.info("sql read finished!")
            # Initialize variables
            print('Setup complete!')
        except Exception as e:
            logging.info("ERROR")
            print(e)




    # Remember decorator 
    @commands.command()
    async def profile(ctx):
        """
        Starts the process of making a profile for the user. Guide users on specifc info needed and maybe a self intro.
        Profile info should be something that stays the same. We could set up a questionaire for the user and they answer by reacting. 
        Stuff like language, region, rank, 

        Args:
            ctx: context of the command. Usually the channel 
        """


        await ctx.send("Making profile")


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


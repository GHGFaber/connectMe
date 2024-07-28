from discord.ext import commands
from core import Bot
import discord

class CrudOperation(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = Bot

    # call these functions when you have the data ready 
    async def create(self):
        await self.bot.db.execute(
            # SQL statement to insert profile information 
        )
        print("row_added")

        async def update(self):
        await self.bot.db.execute(
            # SQL statement to update profile information 
        )


    async def read(self):
        await self.bot.db.execute(
            # SQL statement to read profile information 
        )


    async def delete(self):
        await self.bot.db.execute(
            # SQL statement to delete profile information 
        )
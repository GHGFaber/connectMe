from discord.ext import commands
from core import Bot
import discord

class CrudOperation(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = Bot

    @commands.command()
    async def create(self, ctx: commands.Context):
        await self.bot.db.execute(
            
        )

    @commands.command()
    async def update(self, ctx: commands.Context):

    @commands.command()
    async def read(self, ctx: commands.Context):

    @commands.command()
    async def delete(self, ctx: commands.Context):

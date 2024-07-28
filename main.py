# bot.py
import os

from dotenv import load_dotenv


from asyncpg.pool import create_pool

from discord.ext import commands
import discord

from core import Bot
from asyncio import run
from asyncpg import create_pool
from discord import Intents 
from config import HOST, PORT, PASSWORD, USER, DATABASE_NAME

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = Intents.default()
intents.members = True # see members of the server

async def main():
    async with create_pool(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE_NAME
    ) as pool: 
        async with Bot(
            db=pool,
            command_prefix='!',
            intent=intents
        ) as bot:
            
            await bot.start(token=TOKEN)



if __name__ == '__main__':
    run(main())



# async def create_db_pool():
#     bot.pg_con = await asyncpg.create_pool(database="user", user="Postgres", password=os.getenv('PG_PWD'))



# @bot.setup_hook
# async def setup():
#     print('Performing setup tasks...')
#     # Connect to database
#     with open("sql/schemas.sql", 'r') as sql:
#         await bot.pg_con.execute(sql.read())
#     # Initialize variables
#     print('Setup complete!')

# @bot.event
# async def on_ready():
#     bot.pg_con.execute("CREATE TABLE IF NOT EXISTS user (user_id VARCHAR(32) NOT NULL, server_id VARCHAR(32) NOT NULL, language VARCHAR(32) NOT NULL, region VARCHAR(32) NOT NULL, rank INTEGER NULL)")





# bot.loop.run_until_complete(create_db_pool())



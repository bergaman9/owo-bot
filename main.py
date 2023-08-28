import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
import datetime, time
from datetime import datetime
import asyncio


load_dotenv()
token = getenv("TOKEN")

class Bot(commands.Bot):

    def __init__(self) -> None:
        intents = discord.Intents.all()
        intents.message_content = True
        intents.members = True

        super().__init__(command_prefix=".", intents=intents, help_command=None)

bot = Bot()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f'{len(bot.guilds)} server'))
    await bot.tree.sync()
    count = len(bot.guilds)
    print(f'Logged on as {count}, your bot {bot.user}!')
    global startTime
    startTime = time.time()

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command()
async def uptime(ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time() - startTime))))
    embed = discord.Embed(title="Uptime", description=uptime, color=ctx.author.color)
    await ctx.send(embed=embed)

async def cogs_load():
    for fn in os.listdir("./cogs"):
        if fn.endswith(".py"):
            await bot.load_extension(f"cogs.{fn[:-3]}")

async def main():
    await cogs_load()
    await bot.start(token)

asyncio.run(main())

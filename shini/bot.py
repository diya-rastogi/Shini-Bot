import discord
import os
import random
import time
import asyncio
import requests
import mysql.connector
import json
import logging
import urllib.request
import sys
import asyncdagpi
from requests import get
from discord import Game
from discord import Embed
from datetime import datetime, timedelta
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('SHINI_BOT')

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=">", help_command=None, intents=intents, case_insensitive=True)


@bot.command()
@commands.check_any(commands.is_owner())
async def reload(ctx, *, cog=None):
    async with ctx.typing():
        if cog == None:
            reloadingcog=discord.Embed(
                title = "Reloading cogs!",
                url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLahKLy8pQdCM0SiXNn3EfGIXX19QGzUG3",
                description = "Have fun"
            )
            reloadingcog.set_thumbnail(url="https://cdn.discordapp.com/emojis/608230959464185879.gif?v=1")
            for ext in os.listdir(".\\cogs"):
                if ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        bot.unload_extension(f"cogs.{ext[:-3]}")
                        bot.load_extension(f"cogs.{ext[:-3]}")
                        reloadingcog.add_field(
                            name = f"Reloading {ext}",
                            value = "Done.",
                            inline=False
                        )
                    except Exception as e:
                        reloadingcog.add_field(
                            name = f"Couldn't reload {ext}",
                            value = e,
                            inline=False
                        )
                    await asyncio.sleep(0.5)
            cogsreload = await ctx.send(embed=reloadingcog)
            await asyncio.sleep(5)
            await ctx.message.delete()
            await cogsreload.delete()
        else:
            if cog in os.listdir(".\\cogs"):
                if cog.endswith(".py") and not cog.startswith("_"):
                    try:
                        bot.unload_extension(f"cogs.{cog[:-3]}")
                        bot.load_extension(f"cogs.{cog[:-3]}")
                        cogreload = await ctx.send(f"Reloaded {cog}!")
                        await asyncio.sleep(5)
                        await ctx.message.delete()
                        await cogreload.delete()
                    except Exception as e:
                        await ctx.send(f"Couldn't reload because of {e} :(")

@reload.error
async def clear_error_05(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Only the owner can do that!")

@bot.command()
async def shutdown(ctx):
    await bot.logout()
    #if ctx.message.author.id == 678280991256739840:
      #print("shutdown")
    #try:
    #    await bot.logout()
    #except:
    #    print("EnvironmentError")
    #    bot.clear()
    #else:
    #  await ctx.send("You do not own this bot!")

async def change_presence():
    await bot.wait_until_ready()

    statuses = ["Being a good girl",">help"]

    while not bot.is_closed():
        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Game(status))
        await asyncio.sleep(15)

for cog in os.listdir(".\\cogs"):
    if cog.endswith(".py") and not cog.startswith("_"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} cannot be loaded: ")
            raise e


bot.loop.create_task(change_presence())
bot.run(TOKEN, bot=True)

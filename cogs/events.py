import discord
import asyncio
from discord.ext import commands

messages = joined = 0

async def update_stats(self):
    await self.bot.wait_until_ready()
    global messages, joined

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Logged in")

    intents = discord.Intents.default()
    intents.members = True

def setup(bot):
    bot.add_cog(Events(bot))
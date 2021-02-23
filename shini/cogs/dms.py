import discord
import random
from discord.ext import commands 

class Dms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        response_dms = [
            "Go get a friend and DM them, hmph.",
            "Are you too free? Get a job and stop DMing a bot.",
            "Please use commands in the guild.",
            "Here, watch this `https://www.youtube.com/watch?v=oHg5SJYRHA0`",
            "Ugh, so like, stop bugging me?",
            "Wassuh, what do you want? If you want something from me you can use the commands in the guild.",
            "Try using `/help` in the guild."
        ]
        if isinstance(message.channel, discord.channel.DMChannel) and message.author != self.bot.user:
            await message.channel.send(random.choice(response_dms))


def setup(bot):
    bot.add_cog(Dms(bot))
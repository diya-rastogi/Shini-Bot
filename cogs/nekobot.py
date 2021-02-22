import asyncio
import discord
from nekobot import NekoBotAsync
from discord.ext import commands


class Neko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx, *, member: discord.Member = None):
        if member is None:
            member = ctx.author    
        if isinstance(ctx.channel, discord.DMChannel):
            return
        api = NekoBotAsync()
        #img = member.avatar_url
        img = (await api.get_image("neko")).message
        hello = "magik: {}".format(await api.magik(img))
        await ctx.send(hello)
        await api.close()

def setup(bot):
    bot.add_cog(Neko(bot))
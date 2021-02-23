import discord
import asyncio
from discord.ext import commands

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    snipe_message_content = None
    snipe_message_author = None
    snipe_message_id = None

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        global snipe_message_content
        global snipe_message_author
        global snipe_message_id

        snipe_message_content = message.content
        snipe_message_author = message.author
        snipe_message_id = message.id
        await asyncio.sleep(60)

        if message.id == snipe_message_id:
            snipe_message_author = None
            snipe_message_content = None
            snipe_message_id = None

    @commands.command()
    async def snipe(self, message):
        if snipe_message_content==None:
            await message.channel.send("Theres nothing to snipe.")
        else:
            embed = discord.Embed(color=65280, description=f"{snipe_message_content}")
            embed.set_author(name= f"<@{snipe_message_author}>")
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/795346887955709982.png?v=1")
            await message.channel.send(embed=embed)
            await message.delete()
            return

def setup(bot):
    bot.add_cog(Logs(bot)) 
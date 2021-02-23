import discord
import asyncio
from discord import Embed
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed = discord.Embed(color=ctx.author.color, title="Shini help:", description="Use >help <command name> for extended help.")

        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/734293425595219970/f98dbeea6796c8ede16ae65e19b73f5d.png?size=4096")

        embed.set_footer()

        embed.add_field(name = "Moderation", value= "`Kick, Ban, Unban, Mute, Unmute, Purge`")
        embed.add_field(name = "Fun", value= "`Say, 8ball, TDS, Urban Dictionary, Snipe, Meme, Food`")
        embed.add_field(name = "Information", value= "`Leaderboard, Avatar, User Information, Spotify Stats`")
        embed.add_field(name = "Functionality", value= "`Ping, Weather, Covid Statistics`")
        

        help_com = await ctx.send(embed=embed)
        await asyncio.sleep(30)
        await help_com.delete()
        await ctx.message.delete()


 # MODERATION: KICK, BAN, UNBAN, MUTE, UNMUTE, PURGE

    @help.command(aliases = ["Kick"])
    async def kick(self, ctx):
        embed = discord.Embed(color=ctx.author.color, title="Shini Help: __Kick Command__", description="Kicks a user from the guild.")
        embed.add_field(name="Syntax", value="```<prefix>kick <member tag/id>```")
        embed.add_field(name="Aliases", value="None")
        embed.set_footer(text="Can only be used if you have admin permissions.")

        help_com = await ctx.send(embed=embed)
        await asyncio.sleep(30)
        await help_com.delete()
        await ctx.message.delete()

    @help.command(aliases = ["Ban"])
    async def ban(self, ctx):
        embed = discord.Embed(color=ctx.author.color, title="Shini Help: __Ban Command__", description="Bans a user from the guild.")
        embed.add_field(name="Syntax", value="```<prefix>ban <member tag/id>```")
        embed.add_field(name="Aliases", value="None")
        embed.set_footer(text="Can only be used if you have admin permissions.")

        help_com = await ctx.send(embed=embed)
        await asyncio.sleep(30)
        await help_com.delete()
        await ctx.message.delete()

    @help.command(aliases = ["Unban"])
    async def unban(self, ctx):
        embed = discord.Embed(color=ctx.author.color, title="Shini Help: __Unban Command__", description="Unbans a user from the guild.")
        embed.add_field(name="Syntax", value="```<prefix>unban <member tag/id>```")
        embed.add_field(name="Aliases", value="None")
        embed.set_footer(text="Can only be used if you have admin permissions.")

        help_com = await ctx.send(embed=embed)
        await asyncio.sleep(30)
        await help_com.delete()
        await ctx.message.delete()

    @help.command(aliases = ["Purge"])
    async def purge(self, ctx):
        embed = discord.Embed(color=ctx.author.color, title="Shini Help: __Purge Command__", description="Purges a number of messages from the channel.")
        embed.add_field(name="Syntax", value="```<prefix>purge <number of messages>```")
        embed.add_field(name="Aliases", value="```clear, cl```")
        embed.set_footer(text="Can only be used if you have admin permissions.")

        help_com = await ctx.send(embed=embed)
        await asyncio.sleep(30)
        await help_com.delete()
        await ctx.message.delete()

    @help.command(aliases = ["Unmute"])
    async def unmute(self, ctx):
        embed = discord.Embed(color=ctx.author.color, title="Shini Help: __Unmute Command__", description="Unmutes a user from the guild")
        embed.add_field(name="Syntax", value="```<prefix>unmute <member tag/id>```")
        embed.add_field(name="Aliases", value="None")
        embed.set_footer(text="Can only be used if you have admin permissions.")

        help_com = await ctx.send(embed=embed)
        await asyncio.sleep(30)
        await help_com.delete()
        await ctx.message.delete()

# FUN: SAY, 8BALL, TDS, URBAN DICTIONARY, SNIPE, MEME, FOOD

    @help.command(aliases = ["Say"])
    async def say(self, ctx):
        embed = discord.Embed(color=ctx.author.color, title="Shini Help: __Say Command__", description="The bot says what you say.")
        embed.add_field(name="Syntax", value="```<prefix>say <context>```")
        embed.add_field(name="Aliases", value="None")

        help_com = await ctx.send(embed=embed)
        await asyncio.sleep(30)
        await help_com.delete()
        await ctx.message.delete()

    @help.command(aliases = ["Eightball, 8Ball, 8ball"])
    async def eightball(self, ctx):
        embed = discord.Embed(color=ctx.author.color, title="Shini Help: __8ball Command__", description="Play 8ball using the bot.")
        embed.add_field(name="Syntax", value="```<prefix>8ball <question>```")
        embed.add_field(name="Aliases", value="```eightball```")

        help_com = await ctx.send(embed=embed)
        await asyncio.sleep(30)
        await help_com.delete()
        await ctx.message.delete()

    @help.command(aliases = ["TDS, Tds"])
    async def tds(self, ctx):
        embed = discord.Embed(color=ctx.author.color, title="Shini Help: __TDS Command__", description="Play TDS with friends using the bot. (No aliases)")
        embed.add_field(name="Syntax", value="```<prefix>tdsadd <member tag>```-Adds user; do not need to put member tag when you want to add yourself to the game.\n\n```<prefix>tdsremove <member tag>```-Removes user; do not need to put member tag when you want to remove yourself from the game.\n\n```<prefix>tdsclear```-Removes everyone from the game.\n\n```<prefix>roll```-Displays who asks who randomly.")

        help_com = await ctx.send(embed=embed)
        await asyncio.sleep(30)
        await help_com.delete()
        await ctx.message.delete()
"""
    @help.command(aliases = ["Say"])
    async def say(self, ctx):
        embed = discord.Embed(color=ctx.author.color, title="Shini Help: __Say Command__", description="The bot says what you say.")
        embed.add_field(name="Syntax", value="```<prefix>say <context>```")
        embed.add_field(name="Aliases", value="None")

        help_com = await ctx.send(embed=embed)
        await asyncio.sleep(30)
        await help_com.delete()
        await ctx.message.delete()

    @help.command(aliases = ["Say"])
    async def say(self, ctx):
        embed = discord.Embed(color=ctx.author.color, title="Shini Help: __Say Command__", description="The bot says what you say.")
        embed.add_field(name="Syntax", value="```<prefix>say <context>```")
        embed.add_field(name="Aliases", value="None")

        help_com = await ctx.send(embed=embed)
        await asyncio.sleep(30)
        await help_com.delete()
        await ctx.message.delete()

    @help.command(aliases = ["Say"])
    async def say(self, ctx):
        embed = discord.Embed(color=ctx.author.color, title="Shini Help: __Say Command__", description="The bot says what you say.")
        embed.add_field(name="Syntax", value="```<prefix>say <context>```")
        embed.add_field(name="Aliases", value="None")

        help_com = await ctx.send(embed=embed)
        await asyncio.sleep(30)
        await help_com.delete()
        await ctx.message.delete()

    @help.command(aliases = ["Say"])
    async def say(self, ctx):
        embed = discord.Embed(color=ctx.author.color, title="Shini Help: __Say Command__", description="The bot says what you say.")
        embed.add_field(name="Syntax", value="```<prefix>say <context>```")
        embed.add_field(name="Aliases", value="None")

        help_com = await ctx.send(embed=embed)
        await asyncio.sleep(30)
        await help_com.delete()
        await ctx.message.delete()

"""
"""
    @commands.command(aliases = ["seekhelp"])
    async def help(self, ctx):
        embed = discord.Embed(title="Here you go:",
        description="**FUNCTIONAL**\n- Ping (syntax: /ping) \n- Weather report (syntax: /weather `city`)\n\n**FUN**\n- Monkey see, monkey do (syntax: /say `anything`)\n- 8ball (syntax: /8ball `question` or /crystalball `question`) \n- Urban dictionary (syntax: /ud `a word`\n- Reply to mentions\n\n**MODERATION**\n- Purge messages (syntax: /purge `number`)\n- Ban users (syntax: /ban `@user` `reason`)\n- Unban users (syntax: /unban `username#usertag`)\n- Kick users (syntax: /kick `@user` `reason`)",
        url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLahKLy8pQdCM0SiXNn3EfGIXX19QGzUG3")
        await ctx.author.send(embed=embed)
        helpcom = await ctx.send(f"Commands have been dm'ed to you!")
        await asyncio.sleep(4)
        await helpcom.delete()
        await ctx.message.delete()
"""
def setup(bot):
    bot.add_cog(Help(bot))
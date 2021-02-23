import discord
import random
import asyncio
import json
import urllib
import mysql.connector
from discord import Embed
from discord.ext import commands
from pymongo import MongoClient

bot_channels = [812640276560478248]
talk_channels = [812374723395977220, 812397533758226434, 812644833318928445]

level = ["level1", "level2", "level3"]
levelnum = [1, 10, 20]

username = urllib.parse.quote_plus("diOdiO")
password = urllib.parse.quote_plus("DR@101992")
cluster = MongoClient("mongodb+srv://%s:%s@cluster0.alf6q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"%(username, password))

levelling = cluster["shini_bot"]["levelling"]

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_channels:
            stats = levelling.find_one({"id": message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"id": message.author.id, "xp": 1}
                    levelling.insert_one(newuser)
                else:
                    xp = stats["xp"] + 1
                    levelling.update_one({"id": message.author.id}, {"$set":{"xp":xp}})
                    lvl = 0
                    while True:
                        if xp < ((50*(lvl**2))+(50*(lvl-1))):
                            break
                        lvl +=1
                    xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                    if xp == 0:
                        await message.channel.send (f"Hello {message.author.mention}! You're so lifeless that you leveled up to *{lvl}* ! ")
                        for i in range(len(level)):
                            if lvl == levelnum[i]:
                                await message.authot.add_roles(discord.utils.get(message.authot.guild.roles, name = level[i]))
                                await message.channel.send()

    @commands.command()
    async def rank(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        if isinstance(ctx.channel, discord.DMChannel):
            return

        stats = levelling.find_one({"id": member.id})
        if stats is None:
            await ctx.channel.send("Contact diOdiO#7613 if this was not expected!")
        else:
            xp = stats["xp"]
            lvl = 0
            rank = 0
            while True:
                if xp < ((50*(lvl**2))+(50*(lvl-1))):
                    break
                lvl +=1
            xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
            boxes = int((xp/(200*((1/2)*lvl)))*20)
            rankings = levelling.find().sort("xp", -1)
            for x in rankings:
                rank += 1
                if stats["id"] == x["id"]:
                    break

            progress = (boxes * "●" + (20-boxes) * "-")
            rankem = discord.Embed(title=f"__{member.name}'s rank__")
            rankem.add_field(name="User", value=f"{member.name}#{member.discriminator}")
            rankem.add_field(name="XP", value=f"{xp}/{int(200*((1/2)*lvl))}")
            rankem.add_field(name="Rank", value=f"{rank}/{ctx.guild.member_count}")
            rankem.add_field(name="Progress", value=f"```{progress}```")
            rankem.set_thumbnail(url=member.avatar_url)
            rankem.set_footer(text = f"Requested by {ctx.author.name}", icon_url = ctx.author.avatar_url)
            await ctx.channel.send(embed=rankem)

def setup(bot):
    bot.add_cog(Levels(bot))
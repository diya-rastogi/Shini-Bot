import discord
import praw
import random
from datetime import datetime
from discord.ext import commands

class RedditMeme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):

        reddit = praw.Reddit(
            client_id = "EF42aEkYNqGFCA",
            client_secret = "LASrZ2cI6qxKUDkMtMId1aNc__VUpA",
            username = "shinibot",
            password = "DR@101992",
        user_agent = "python praw"
        )

        sub_red = reddit.subreddit("memes+blackpeopletwitter+memeeconomy+greentext+dankmemes+okbuddyretard+pewdiepiesubmissions+animemes+programmerhumor+dogelore+wholesomememes+roastme")
        all_subs = []
        hot = sub_red.hot()

        for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed(title = name, color = ctx.author.color, timestamp = datetime.utcnow())
        embed.set_image(url = url)
        embed.set_footer(text = f"Requested by {ctx.author.name}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases = ["foodporn"])
    async def food(self, ctx):

        reddit = praw.Reddit(
            client_id = "EF42aEkYNqGFCA",
            client_secret = "LASrZ2cI6qxKUDkMtMId1aNc__VUpA",
            username = "shinibot",
            password = "DR@101992",
        user_agent = "python praw"
        )

        sub_red = reddit.subreddit("food+cooking+foodporn")
        all_subs = []
        hot = sub_red.hot()

        for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed(title = name, color = ctx.author.color, timestamp = datetime.utcnow())
        embed.set_image(url = url)
        embed.set_footer(text = f"Requested by {ctx.author.name}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(RedditMeme(bot))
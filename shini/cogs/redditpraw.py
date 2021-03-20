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

        sub_red = reddit.subreddit("memes+dankmemes+blackpeopletwitter+memeeconomy+greentext+dankmemes+okbuddyretard+pewdiepiesubmissions+animemes+programmerhumor+dogelore+wholesomememes+roastme")
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
        await ctx.message.reply(embed=embed)

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
        
"""
    @commands.command()
    @commands.is_nsfw()
    async def test(self,ctx):

        reddit = praw.Reddit(
            client_id = "EF42aEkYNqGFCA",
            client_secret = "LASrZ2cI6qxKUDkMtMId1aNc__VUpA",
            username = "shinibot",
            password = "DR@101992",
        user_agent = "python praw"
        )

        subreddit = reddit.subreddit("hentai")
        all_subs = []

        top = subreddit.top(limit = 30)

        for submission in top:
            all_subs.append(submission)

        n = len(all_subs)
        x = random.sample(range(n), 10)
        
        filtered_subs = []

        for i in x:
            filtered_subs.append(all_subs[i])
        
        a = len(filtered_subs)
        for j in range(a):
            url = filtered_subs[j].url
            name = filtered_subs[j].name
            print(url)
            print(name)

            l = url.endswith(".gif")

            if l == True:

                embed = discord.Embed(title = name, color=discord.Color.gold())
                embed.set_image(url = url)
                embed.set_footer(text=f"Asked by a horny af person")

            else:

                url = url+".gif"
                
                embed = discord.Embed(title = name, color=discord.Color.gold())
                embed.set_image(url = url)
                embed.set_footer(text=f"Asked by a horny af person")
"""

def setup(bot):
    bot.add_cog(RedditMeme(bot))
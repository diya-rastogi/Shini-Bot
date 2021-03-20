import discord
import asyncio
import random
import requests
import logging
import urllib.request
import TenGiphPy
from PIL import Image, ImageDraw, ImageFilter
from requests import get
from discord.ext import commands   

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        responses = [
            ", stop tagging me.",
            ", go away fucktard.",
            ", are you too free?",
            ", man stop.",
            ", how are you?",
            ", hewwo :3",
            ", yes!",
            ", nO. :relieved:",
            ", uwu!",
            ", leo best boy <3",
            ", rax bess :kiss:"
        ]
        if not message.content.startswith(">"):
            for x in message.mentions:
                if (message.author == self.bot.user):
                    return
                if(x == self.bot.user):
                    await message.channel.send(f"{message.author.mention}{random.choice(responses)}")
        word = "neel"
        if word in message.content.lower():
            arg = message.content.lower()
            hmm = arg.replace("neel", "n*el")
            await message.delete()
            await message.channel.send(f"{message.author.mention}, you should have written: `{hmm}`")
        word2 = "cba"
        if message.author.id == 289379965101932544:
            if word2 in message.content.lower():
                await message.delete()
                await message.channel.send("chup reh randi")

    @commands.command()
    async def say(self, ctx, *, arg: commands.clean_content):
        for x in ctx.message.mentions:
            if(x == self.bot.user):
                await ctx.message.delete()
                await ctx.send("Please don't try to break me.")
                return
                
        await ctx.message.delete()
        await ctx.send(arg)
    
    @commands.command()
    async def slap(self, ctx, *, member:discord.Member = None):
        if member is None:
            await ctx.message.delete()
            await ctx.send(f"{ctx.author.mention}, who do I slap, your mom?")  
            return

        if member.id == self.bot.user.id:
            await ctx.message.delete()
            await ctx.send("Please don't try to break me.")
            return

        if isinstance(ctx.channel, discord.DMChannel):
            return

        responses = [
            "...grabs a gold block and flings it at {}'s face.",
            "...picks up a laptop and hits {} with it.",
            "...sent {} to /dev/null.",
            "...hurls a piece of rotten meat at {}.",
            "...threw {} off a building.",
            "...made {} a knuckle sandwich.",
            "...hurls a printer at {}.",
            "...whacks {} on the butt with a gold block.",
            "...grabs up a mau5head and slaps {} with it.",
            "...replaced all of {}'s music with Nickelback.",
            "...smacks {} around a bit with a baseball bat.",
            "...slaps {} in the chest with a lava bucket.",
            "...whacks {} in the face with a physics textbook.",
            "...sits on {}'s face while slamming a pair of trousers on the crotch",
            "...prods {} with an old television."
        ]
        mem = member.mention
        await ctx.message.delete()
        await ctx.send(f"{random.choice(responses).format(mem)}")

    @commands.command()
    async def islam(self, ctx):
        embed = discord.Embed(title="LAHAULA VILA QUWAT ILLA BILLA", description="```لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِٱللَّٰهِ ٱلْعَلِيِّ ٱلْعَظِيمِ‎```")
        embed.set_thumbnail(url="https://www.allahsword.com/images/la-hawla-wala-quwwata-illa-billah%402x.png")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command()
    async def hindu(self, ctx):
        embed = discord.Embed(title="JAI BHOLENATH", description="```ऊं भूर्भुव: स्व: तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि। धियो यो न: प्रचोदयात्।।```")
        embed.set_image(url="https://tfipost.com/wp-content/uploads/2019/05/MODI-2.png")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command()
    async def gif(self, ctx, *, giftag, member:discord.Member=None):
        t = TenGiphPy.Tenor(token="YZUNGG2MZWS7")
        gifurl = t.random(str(giftag))
        embed = discord.Embed(title="Here you go :3", color=0xdc143c)
        embed.set_image(url=f"{gifurl}")
        embed.set_footer(text = f"Requested by {ctx.author.name}", icon_url = ctx.author.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=embed)
    
    @gif.error
    async def tenor_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please give a valid argument to search.")
        else:
            raise error

    @commands.command(aliases=["borth"])
    async def aakash(self, ctx):
        responses = [
            "https://i.imgflip.com/j4h11.jpg",
            "https://data.whicdn.com/images/265221268/original.jpg",
            "https://memetemplatehouse.com/wp-content/uploads/2020/09/naughty-doge-dancing-meme-template.jpg",
            "https://i.pinimg.com/564x/6b/9e/25/6b9e25bb26ae1ed1df6ae2d30bd2e872.jpg",
            "https://i.imgflip.com/1bbkue.jpg",
            "https://memetemplatehouse.com/wp-content/uploads/2020/05/IMG_20200121_021814_compress13_compress18.jpg"
        ]
        embed = discord.Embed(title="You're stupid", description="```Happy day you came out of your mom’s vagina!```", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO")
        embed.set_image(url=f"{random.choice(responses)}")
        embed.set_footer(text = f"Requested by {ctx.author.name}", icon_url = ctx.author.avatar_url)
        user = ctx.bot.get_user(300111535647227905)
        await ctx.message.delete()
        await user.send(embed=embed)

    @commands.command(aliases=["nigga", "nig"])
    async def nigger(self, ctx):
        embed = discord.Embed(title="uwu")
        embed.set_image(url="https://assets.puzzlefactory.pl/puzzle/331/605/original.jpg")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def vip(self, ctx):

        ban = discord.Embed(title="Tangent should be banned", description="Very cringe and normie behaviour.")
        ban.set_thumbnail(url="https://cdn.discordapp.com/attachments/734294558933909557/786659523820912679/ban.png")
        await ctx.channel.send(embed=ban)

    @commands.command(aliases=["8ball", "crystalball"])
    async def eightball(self, ctx, *, question: commands.clean_content=None):
        answers = [
            "As I see it,- yes.",
            "Ask again later.",
            "Better not tell you now",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don’t count on it.",
            "It is certain.",
            "It is decidedly so.",
            "Most likely.",
            "My reply is no.",
            "My sources say no.",
            "Outlook is not so good.",
            "Outlook is good.",
            "Reply hazy, try again.",
            "Signs point to yes.",
            "Very doubtful.",
            "Without a doubt.",
            "Yes.",
            "Yes, definitely.",
            "You may rely on it."
            ]

        if question==None:
            await ctx.send("That does not look like a question to me.")
        else:
            await ctx.send(f"Question: {question}\nAnswer: {random.choice(answers)}")


    global TDS
    TDS=[]

    #global ROLL
    ROLL=[]

    @commands.command()
    async def tds(self, ctx):
        global TDS
        await ctx.send(TDS)

    @commands.command()
    async def tdsremove(self, ctx,user :discord.Member=None):
        global TDS
        if user==None:
            user = ctx.author
        if user.name not in TDS:
            await ctx.send("Player is not present in the current game.")
        else:
            TDS.remove(user.name)
            await ctx.send(f"{user.name} has been removed from the game.")
        await ctx.send(f"Current Members Are: {TDS}")

    @commands.command()
    async def tdsclear(self, ctx):
        global TDS
        TDS=[]
        await ctx.send("All players removed from the game.")


    @commands.command()
    async def tdsadd(self, ctx,user: discord.Member=None):
        global TDS
        if user==None:
            user = ctx.author
        if user.name not in TDS:
            TDS.append(user.name)
            
        else:
            await ctx.send("User already added.")
            return
        
        await ctx.send(f"{user.mention} has been added to the game")
        await ctx.send(f"Current Members are {TDS}")

    @commands.command()
    async def roll(self, ctx):
        global TDS
        if len(TDS)<=1:
            msg2 = await ctx.send("`I know you are lonely but you cant play with yourself`")
            await asyncio.sleep(3)
            await msg2.delete()
            return
        msg1=await ctx.send("Now Rolling")
        choice1=random.choice(TDS)
        choice2=random.choice(TDS)
        while choice1==choice2:
            choice2=random.choice(TDS)
        contents=f"{choice1} ASKS {choice2}"
        embed = discord.Embed(title=contents,color=65280)
        
        await msg1.edit(content=None,embed=embed)

    @commands.command()
    async def ud(self, ctx, *,word):
        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        querystring = {"term":word}
        headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "36431a8cf8mshafa57acb3a557c5p164f7ajsnbedf49fc829d"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.json()

        try:
            definition = result["list"][0]["definition"]
            example = result["list"][0]["example"]
            if example == None:
                example = "No example found!"
            link = result["list"][0]["permalink"]
            urban=discord.Embed(title=f'{word}',url=f'{link}')
            urban.add_field(name="Description", value=f"```{definition}```", inline=False)
            urban.add_field(name="Example", value=f"```{example}```", inline=False)
            urban.set_thumbnail(url="https://cdn.discordapp.com/attachments/734294558933909557/787575367749599232/ezgif.com-gif-maker_4.gif")
            await ctx.send(embed=urban)
            
        except:
            await ctx.send("Not found!")

    @commands.command()
    async def tomato(self, ctx, *, member: discord.Member = None):
        if member is None:
            member = ctx.author    
        if isinstance(ctx.channel, discord.DMChannel):
            return

        im1 = Image.open(f"{member.avatar_url}")
        im2 = Image.open(".\\splat.png")
        back_im = im1.copy()
        back_im.paste(im2, (400, 100)) 
        await ctx.send(back_im)


def setup(bot):
    bot.add_cog(Fun(bot))

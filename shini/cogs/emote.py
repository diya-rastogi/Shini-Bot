from discord import utils
from discord.ext import commands
import discord

class Emote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def getemote(self, arg):
    
        emote = utils.get(self.bot.emojis, name = arg.strip(":"))

        if emote is not None:
            if emote.animated:
                pref = "a"
            else:
                pref = ""
            return f"<{pref}:{emote.name}:{emote.id}>"
        else:
            return None

    async def getinstr(self, content):
        l = []

        x = content.split(" ")
        count = content.split(":")

        if len(count) > 1:
            for item in x:
                if item.count(":") > 1:
                    hmm = ""
                    if item.startswith("<") and item.endswith(">"):
                        l.append(item)
                    else:
                        count = 0
                        for i in item:
                            if count == 2:
                                hmm2 = hmm.replace(" ", "")
                                l.append(hmm2)
                                hmm = ""
                                count = 0

                            if i != ":":
                                hmm += i
                            else:
                                if hmm == "" or count == 1:
                                    hmm += " : "
                                    count += 1
                                else:
                                    hmm2 = hmm.replace(" ", "")
                                    l.append(hmm2)
                                    hmm = ":"
                                    count = 1

                        hmm2 = hmm.replace(" ", "")
                        l.append(hmm2)
                else:
                    l.append(item)
        else:
            return content

        return l

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if ":" in message.content:
            msg = await self.getinstr(message.content)
            l = ""
            flag = False
            smth = message.content.split(":")
            if len(smth) > 1:
                for word in msg:
                    if word.startswith(":") and word.endswith(":") and len(word) > 1:
                        emote = await self.getemote(word)
                        if emote is not None:
                            flag = True
                            l += f" {emote}"
                        else:
                            l += f" {word}"
                    else:
                        l += f" {word}"

            else:
                l += msg
            

            if flag:
                webhooks = await message.channel.webhooks()
                webhook = utils.get(webhooks, name = "Shini Emote")
                if webhook is None:
                    webhook = await message.channel.create_webhook(name = "Shini Emote")

                await webhook.send(l, username = message.author.name, avatar_url = message.author.avatar_url)
                await message.delete()

def setup(bot):
    bot.add_cog(Emote(bot))
import discord
import random
import asyncio
import json
import mysql.connector
from discord import Embed
from discord.ext import commands

connection = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="DR@101992992101",
                                 database="discord_bot"
    )


class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        else:
            xp = random.randint(1,3)
            #print(message.author.name + " will receive " + str(xp) + "xp")
            cursor = connection.cursor()
            cursor.execute("SELECT xp FROM users WHERE user_id = " + str(message.author.id))
            result = cursor.fetchall()
            if (len(result) == 0):
                #print("User is not in the database, please add them first.")
                cursor.execute(f"INSERT INTO users VALUES( '{str(message.author.id)}' , '{str(xp)}', '{str(message.author.name)}' )")
                connection.commit()
                print("Inserted user.")

            else:
                newXP = result[0][0] + xp
                #print("New xp: " + str(newXP))
                cursor.execute(f"UPDATE users SET xp = {str(newXP)} WHERE user_id = {str(message.author.id)}")
                connection.commit()
                #print("Updated xp.")

            #await self.bot.process_commands(message)

    @commands.command(aliases = ["lb"])
    async def leaderboard(self, ctx):
        cursor = connection.cursor()
        cursor.execute("SELECT username, xp FROM users ORDER BY xp DESC")
        result = cursor.fetchall()

        final_result_dict = dict(result)
        #print(final_result)

        x="```py\n\n"
        ctr=1
        for i in final_result_dict.keys():
            x += f"{ctr}. {i} :  {final_result_dict[i]}xp\n\n"
            ctr+=1

        x += "```"
        #print(x)

        level_system = discord.Embed(title = "Here are the top users:", color=ctx.guild.me.top_role.color, description=x)
        await ctx.send(embed=level_system)
        connection.commit()

def setup(bot):
    bot.add_cog(Levels(bot))
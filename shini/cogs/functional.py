import discord
import asyncio
from discord import Embed
from discord.ext import commands
import requests
import time
import json
import logging
import urllib.request
from requests import get

api_key = "4220affa99f3d129532b03daf76b498d"
base_url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid="

class Functionals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ping(self, ctx):  
        await ctx.message.delete()
        await ctx.send(f"Pong! `{round(self.bot.latency * 1000)}` ms")


    @commands.command()
    async def weather(self, ctx, *, city: str):
        destination = city
        final_url = base_url + api_key + "&q=" + destination
        webUrl  = urllib.request.urlopen(final_url)
        data = webUrl.read()

        x = json.loads(data.decode())

        channel = ctx.message.channel

        if x["cod"] != "404":
            async with channel.typing():

                y = x["list"][0]["main"]

                temp_now = y.get("temp")
                temp_now_celsius  = str(round(temp_now - 273.15))
                pressure_now = y["pressure"]
                humidity_now = y["humidity"]
                z = x["list"][0]["weather"]
                desc = z[0]["description"]

                embed = discord.Embed(title=f"Weather at {destination}",
                                    color=ctx.guild.me.top_role.color)
                embed.add_field(name="Descripition", value=f"{desc}", inline=False)
                embed.add_field(name="Temperature(C)", value=f"{temp_now_celsius}°C", inline=False)
                embed.add_field(name="Humidity(%)", value=f"{humidity_now}%", inline=False)
                embed.add_field(name="Atm Pressure(hPa)", value=f"{pressure_now}hPa", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/734294558933909557/786630600395063316/bongo.gif")
                await channel.send(embed=embed)
        else:
            await channel.send("Data Unavailable")

    @commands.command()
    async def covid(self, ctx, *, country):
        url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"
        querystring = {"country":country}
        headers = {
    'x-rapidapi-key': "36431a8cf8mshafa57acb3a557c5p164f7ajsnbedf49fc829d",
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
    }
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.json()

        recovered = result["data"]["recovered"]
        deaths = result["data"]["deaths"]
        confirmed = result["data"]["confirmed"]
        lastChecked = result["data"]["lastChecked"]
        lastReported = result["data"]["lastReported"]

        covid = discord.Embed(title=f'{country}',
        color=0xf50000,
        url = "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public",
        description=f'**Recovered:**`{recovered}`\n**Deaths:** `{deaths}`\n**Confirmed Cases:** `{confirmed}`\n**Last checked:** `{lastChecked}`\n**Last reported:** `{lastReported}`')
        covid.set_thumbnail(url = "https://cdn.discordapp.com/attachments/734294558933909557/787721075433537576/covid.gif")
        await ctx.send(embed=covid)

def setup(bot):
    bot.add_cog(Functionals(bot))
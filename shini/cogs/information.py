import discord
import asyncio
from discord.ext import commands
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from discord import Spotify
from datetime import datetime
from datetime import timedelta
from asyncdagpi import Client, ImageFeatures

dagpi = Client("aYrsMkEB544LifNpp8prpXFB8bNqCoMYg0tIs7SrF5zi0zmQSqwR1LmB3VcsBARC")

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["info", "ui", "information"])
    async def userinfo(self, ctx, *, member: discord.Member = None):
        if member is None:
            member = ctx.author    
        if isinstance(ctx.channel, discord.DMChannel):
            return

        date_format = "%a, %d %B %Y, %I:%M %p"

        roles = [role for role in member.roles]

        info_user = discord.Embed(colour=member.color)
        info_user.set_author(name=f"User: {member}")
        info_user.set_thumbnail(url=member.avatar_url)

        info_user.add_field(name="ID:", value=member.id)
        info_user.add_field(name="Nickname:", value=member.display_name)

        info_user.add_field(name="Account created at:", value=member.created_at.strftime(date_format))
        info_user.add_field(name="Joined at:", value=member.joined_at.strftime(date_format))

        info_user.add_field(name=f" Roles ({len(roles)})", value = " ".join([role.mention for role in roles]))
        info_user.add_field(name="Top role:", value=member.top_role.mention)

        await ctx.send(embed=info_user)

    @commands.command(aliases = ["pfp"])
    async def avatar(self, ctx, *, member: discord.Member = None):
        if member is None:
            member = ctx.author    
        if isinstance(ctx.channel, discord.DMChannel):
            return

        u_avatar = discord.Embed(color=member.color)
        u_avatar.set_author(name=f"User: {member}")
        u_avatar.set_image(url=member.avatar_url)

        await ctx.send(embed=u_avatar)

    @commands.command(aliases = ["spot"])
    async def spotify(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        if isinstance(ctx.channel, discord.DMChannel):
            return
        
        spot = next((activity for activity in member.activities if isinstance(activity, discord.Spotify)), None)
        if spot is None:
            await ctx.send(f"{member.name} is not listening to Spotify!")
            return
        
        for activity in member.activities:
            if isinstance(activity, Spotify):

                delta = activity.duration

                embed = discord.Embed(color = activity.color)
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.add_field(name="Song", value=activity.title)
                embed.add_field(name="Artist", value=activity.artist)
                embed.add_field(name="Album", value=activity.album)
                embed.add_field(name="Track ID", value=f"`{activity.track_id}`")
                embed.add_field(name="Track Link", value=f"https://open.spotify.com/track/{activity.track_id}")
                embed.add_field(name="Song duration", value="{}:{:02d}".format(*divmod(delta.seconds, 60)))

                embed.set_author(name=member.name, url=f"https://open.spotify.com/track/{activity.track_id}", icon_url="https://cdn.discordapp.com/attachments/734294558933909557/800635142372589598/spotify-icon-green-logo-8.png")
                embed.set_footer(text = f"Requested by {ctx.author.name}", icon_url = ctx.author.avatar_url)
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
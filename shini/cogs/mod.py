import discord
import asyncio
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=["clear, cl"])
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit+1)
        clean = await ctx.send(f"{limit} messages have been deleted.")
        await asyncio.sleep(3)
        await clean.delete()

    @purge.error
    async def clear_error_00(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Be an admin first kiddo.")
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban (self, ctx, member:discord.Member=None, reason =None):

        if member == commands.has_permissions(ban_members=True):
            await ctx.message.delete()
            await ctx.channel.send("That person is an administrator!")

        elif member == None or member == ctx.message.author:
            await ctx.message.delete()
            await ctx.channel.send("What the heck man?! Use the command correctly!")
            return

        if reason == None:
            reason = "Get a life."

        await member.ban(reason = reason)
        #message = f"You have been banned from {ctx.guild.name} for {reason}"
        #await member.send(message)
        ban = discord.Embed(title="Action Taken", description="BAN")
        ban.add_field(name="Reason", value=f"{reason}", inline=False)
        ban.add_field(name="User affected", value=f"{member.name}#{member.discriminator}({member.id})", inline=False)
        ban.add_field(name="Channel", value=f"<#{ctx.message.channel.id}>", inline=False)
        ban.set_thumbnail(url=f"{member.avatar_url}")
        ban.set_footer(text = f"Action taken by {ctx.author.name}", icon_url = ctx.author.avatar_url)
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)

    @ban.error
    async def clear_error_01(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You lack adequate permissions to do that!")

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unban(self, ctx, member, *,reason=None):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if reason == None:
                reason = "Not specified."

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                unban = discord.Embed(title="Action Taken", description="UNBAN")
                unban.add_field(name="Reason", value=f"{reason}", inline=False)
                unban.add_field(name="User affected", value=f"{user.name}#{user.discriminator}({user.id})", inline=False)
                unban.add_field(name="Channel", value=f"<#{ctx.message.channel.id}>", inline=False)
                unban.set_thumbnail(url=f"{member.avatar_url}")
                unban.set_footer(text = f"Action taken by {ctx.author.name}", icon_url = ctx.author.avatar_url)
                await ctx.message.delete()
                await ctx.channel.send(embed=unban)
                return
            else:
                await ctx.send("The user is not banned!")

    @unban.error
    async def clear_error_02(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You lack adequate permissions to do that!")


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member=None, *, reason=None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("What the heck man?! Use the command correctly!")
            return
        if reason == None:
            reason = "Get a life."

        await member.kick(reason=reason)
        kick = discord.Embed(title="Action Taken", description="KICK")
        kick.add_field(name="Reason", value=f"{reason}", inline=False)
        kick.add_field(name="User affected", value=f"{member.name}#{member.discriminator}({member.id})", inline=False)
        kick.add_field(name="Channel", value=f"<#{ctx.message.channel.id}>", inline=False)
        kick.set_thumbnail(url=f"{member.avatar_url}")
        kick.set_footer(text = f"Action taken by {ctx.author.name}", icon_url = ctx.author.avatar_url)
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
    
    @kick.error
    async def clear_error_03(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You lack adequate permissions to do that!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member:discord.Member=None, *, reason=None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("What the heck man?! Use the command correctly!")
            return
        if reason == None:
            reason = "Please shut up."

        if not member.bot:
            muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.add_roles(muted_role)
            mute = discord.Embed(title="Action Taken", description="MUTE")
            mute.add_field(name="Reason", value=f"{reason}", inline=False)
            mute.add_field(name="User affected", value=f"{member.name}#{member.discriminator}({member.id})", inline=False)
            mute.add_field(name="Channel", value=f"<#{ctx.message.channel.id}>", inline=False)
            mute.set_thumbnail(url=f"{member.avatar_url}")
            mute.set_footer(text = f"Action taken by {ctx.author.name}", icon_url = ctx.author.avatar_url)
            await ctx.message.delete()
            await ctx.channel.send(member.mention, embed=mute)

        else:
            await ctx.channel.send("What the heck man?! Use the command correctly!")
    
    @mute.error
    async def clear_error_04(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You lack adequate permissions to do that!")

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unmute(self, ctx, member:discord.Member = None, *,reason=None):
        
        roles = [role for role in member.roles]
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")

        if member == None or member == ctx.message.author:
            await ctx.channel.send("What the heck man?! Use the command correctly!")
            return
        if reason == None:
            reason = "Not specified."

        if not member.bot:

            if muted_role in roles:
                await member.remove_roles(muted_role)
                unmute = discord.Embed(title="Action Taken", description="UNMUTE")
                unmute.add_field(name="Reason", value=f"{reason}", inline=False)
                unmute.add_field(name="User affected", value=f"{member.name}#{member.discriminator}({member.id})", inline=False)
                unmute.add_field(name="Channel", value=f"<#{ctx.message.channel.id}>", inline=False)
                unmute.set_thumbnail(url=f"{member.avatar_url}")
                unmute.set_footer(text = f"Action taken by {ctx.author.name}", icon_url = ctx.author.avatar_url)
                await ctx.message.delete()
                await ctx.channel.send(member.mention, embed=unmute)

            elif muted_role not in roles:
                await ctx.send("The user is not muted!")
        else:
            await ctx.channel.send("What the heck man?! Use the command correctly!")
            
    @mute.error
    async def clear_error_05(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You lack adequate permissions to do that!")


def setup(bot):
    bot.add_cog(Mod(bot))